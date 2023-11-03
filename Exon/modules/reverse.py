import os
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from telegraph import upload_file


class GoogleReverseImageSearch:
    """
    A class for performing a reverse image search on Google.
    """

    GOOGLE_IMAGE_SEARCH_URL = "https://images.google.com/searchbyimage?safe=off&sbisrc=tg&client=app&image_url={img_url}"
    USER_AGENT = (
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 "
        "Mobile Safari/537.36"
    )

    def __init__(self) -> None:
        """
        Initialize the GoogleReverseImageSearch instance.
        """
        self._client = requests.Session()

    @staticmethod
    def _get_image_url(address: str):
        """
        Get the image URL, either from a file upload or directly if it's a URL.

        Returns:
            str: The image URL.
        """
        if os.path.isfile(address):
            assert (
                os.path.getsize(address) <= 5979648
            ), "File size must be less than 5.7 MB"
            return  f"https://graph.org{upload_file(address)[0]}"
        else:
            return address

    def reverse_search_image(self, address: str):
        """
        Perform a reverse image search on Google and retrieve results.

        Returns:
            dict: A dictionary containing search results, including 'similar' and 'output'.
        """
        img_url = self._get_image_url(address=address)
        response = self._client.get(
            url=self.GOOGLE_IMAGE_SEARCH_URL.format(img_url=img_url),
            headers={"User-agent": self.USER_AGENT},
        )
        soup = BeautifulSoup(response.text, "html.parser")
        result = {"similar": response.url, "output": ""}
        for best in soup.find_all("div", {"class": "r5a77d"}):
            output = best.get_text()
            result["output"] = unidecode(output)

        return result

    @staticmethod
    def get_requirements():
        return ["unidecode", "telegraph", "bs4", "requests"]


from pyrogram import filters
import requests
from Chizuru import pgram as app, TOKEN as bot_token
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# Constants
MAX_FILE_SIZE = 3145728
ALLOWED_MIME_TYPES = ["image/png", "image/jpeg"]
google_search = GoogleReverseImageSearch()


async def get_file_id_from_message(msg):
    message = msg.reply_to_message
    if not message:
        return None

    if message.document:
        if (
            int(message.document.file_size) > MAX_FILE_SIZE
            or message.document.mime_type not in ALLOWED_MIME_TYPES
        ):
            return None
        return message.document.file_id

    if message.sticker:
        if message.sticker.is_animated:
            if not message.sticker.thumbs:
                return None
            return message.sticker.thumbs[0].file_id
        else:
            return message.sticker.file_id

    if message.photo:
        return message.photo.file_id

    if message.animation:
        if not message.animation.thumbs:
            return None
        return message.animation.thumbs[0].file_id

    if message.video:
        if not message.video.thumbs:
            return None
        return message.video.thumbs[0].file_id

    return None


@app.on_message(filters.command(["pp", "grs", "reverse", "p"]))
async def reverse_image(_, msg):
    text = await msg.reply("**Wait a moment...**")
    file_id = await get_file_id_from_message(msg)

    if not file_id:
        return await text.edit("**Reply to supported media types!**")

    await text.edit("**â‡¢ Requesting Google Search...**")

    r = requests.post(
        f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    ).json()
    file_path = r["result"]["file_path"]
    img = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
    result = google_search.reverse_search_image(address=img)
    if not result["output"]:
        return await text.edit("Couldn't find anything")

    caption = f"[{result['output']}]({result['similar']})"
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Open Link", url=result["similar"])]]
    )

    await text.edit(caption, reply_markup=keyboard)
