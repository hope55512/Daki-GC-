import json
import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message

# REPO => Your Bots File Name
from Exon import Abishnoi as app

@app.on_message(filters.command("img"))
async def bingimg_search(client: Client, message: Message):
    await message.reply_text("The Command is depricated :(\nUse /bingimg and /googleimg to search on different platforms..")

# Command handler for the '/bingimg' command
@app.on_message(filters.command("bingimg"))
async def bingimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return message.reply_text(
            "Provide me a query to search!"
        )  # Return error if no query is provided

    search_message = message.reply_text(
        "🔎"
    )  # Display searching message

    # Send request to Bing image search API
    url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    await message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    search_message.delete()
    message.delete()


# Command handler for the '/googleimg' command
@app.on_message(filters.command("googleimg"))
async def googleimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return message.reply_text(
            "Provide me a query to search!"
        )  # Return error if no query is provided

    search_message = message.reply_text(
        "🔎"
    )  # Display searching message

    # Send request to Google image search API
    url = "https://sugoi-api.vercel.app/googleimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    await message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    search_message.delete()
    message.delete()

__help__ = """
ᴛʜᴇ ᴇꜰꜰᴇᴄᴛɪᴠᴇ ᴍᴏᴅᴜʟᴇ ᴛʜᴀᴛ ʜᴇʟᴘ ʏᴏᴜ ꜱᴇᴀʀᴄʜ ɪᴍᴀɢᴇꜱ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ʙɪɴɢ

 ➢ /googleimg*:* ᴛᴏ ɢᴇᴛ ʀᴇꜱᴜʟᴛᴇᴅ ɪᴍᴀɢᴇ ꜰʀᴏᴍ ɢᴏᴏɢʟᴇ.

 ➢ /bingimg*:* ᴛᴏ ɢᴇᴛ ʀᴇꜱᴜʟᴛᴇᴅ ɪᴍᴀɢᴇ ꜰʀᴏᴍ ʙɪɴɢ.
"""

__mod_name__ = "Iᴍɢ"