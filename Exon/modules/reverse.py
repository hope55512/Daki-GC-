import os
import re
import urllib
import urllib.parse
import urllib.request
import requests
from bs4 import BeautifulSoup
from telegram import InputMediaPhoto, Update
from telegram.error import TelegramError
from telegram.ext import CallbackContext, CommandHandler, run_async
from Exon import dispatcher


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

@run_async
def reverse(update: Update, context: CallbackContext):
    try:
        if os.path.isfile("okgoogle.png"):
            os.remove("okgoogle.png")

        msg = update.effective_message
        chat_id = update.effective_chat.id
        bot, args = context.bot, context.args
        rtmid = msg.message_id
        imagename = "okgoogle.png"

        reply = msg.reply_to_message
        if reply:
            if reply.sticker:
                file_id = reply.sticker.file_id
            elif reply.photo:
                file_id = reply.photo[-1].file_id
            elif reply.document:
                file_id = reply.document.file_id
            else:
                msg.reply_text("Reply to an image or sticker to look up.")
                return
            image_file = bot.get_file(file_id)
            image_file.download(imagename)
            if args:
                lim = int(args[0]) if args[0].isdigit() else 2
            else:
                lim = 2
        elif args and not reply:
            splatargs = msg.text.split()
            if len(splatargs) >= 2:
                img_link = splatargs[1]
                lim = int(splatargs[2]) if len(splatargs) >= 3 and splatargs[2].isdigit() else 2
            else:
                msg.reply_text("/reverse <link> <amount of images to return>")
                return
            try:
                urllib.request.urlretrieve(img_link, imagename)
            except Exception as e:
                msg.reply_text(f"Error: {str(e)}")
                return
        else:
            msg.reply_markdown("Please reply to a sticker or an image to search it!\nYou can also search an image with a link: `/reverse [picturelink] <amount>`.")
            return

        try:
            search_url = "https://www.google.com/searchbyimage/upload"
            multipart = {"encoded_image": (imagename, open(imagename, "rb")), "image_content": ""}
            response = requests.post(search_url, files=multipart, allow_redirects=False)
            fetch_url = response.headers.get("Location")

            if response.status_code != 400:
                xx = bot.send_message(chat_id, "Image was successfully uploaded to Google.\nParsing it, please wait.", reply_to_message_id=rtmid)
            else:
                xx = bot.send_message(chat_id, "Google told me to go away.", reply_to_message_id=rtmid)
                return

            os.remove(imagename)
            match = parse_sauce(fetch_url + "&hl=en")
            guess = match.get("best_guess")
            if "override" in match and match["override"]:
                imgspage = match["override"]
            else:
                imgspage = match.get("similar_images")

            if guess and imgspage:
                xx.edit_text(f"[{guess}]({fetch_url})\nProcessing...", parse_mode="Markdown", disable_web_page_preview=True)
            else:
                xx.edit_text("Couldn't find anything.")
                return

            images = scam(imgspage, lim)
            if not images:
                xx.edit_text(f"[{guess}]({fetch_url})\n[Visually similar images]({imgspage})\nCouldn't fetch any images.", parse_mode="Markdown", disable_web_page_preview=True)
                return

            img_links = [InputMediaPhoto(media=str(link)) for link in images]

            bot.send_media_group(chat_id=chat_id, media=img_links, reply_to_message_id=rtmid)
            xx.edit_text(f"[{guess}]({fetch_url})\n[Visually similar images]({imgspage})", parse_mode="Markdown", disable_web_page_preview=True)
        except TelegramError as e:
            print(e)
        except Exception as exception:
            print(exception)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def parse_sauce(google_url):
    source = opener.open(google_url).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "override": "", "best_guess": ""}

    try:
        for bess in soup.find_all("a", class_="PBorbe"):
            url = "https://www.google.com" + bess.get("href")
            results["override"] = url
    except:
        pass

    for similar_image in soup.find_all("input", class_="gLFyf"):
        url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(similar_image.get("value"))
        results["similar_images"] = url

    for best_guess in soup.find_all("div", class_="r5a77d"):
        results["best_guess"] = best_guess.get_text()

    return results

def scam(imgspage, lim):
    single = opener.open(imgspage).read().decode("utf-8")

    if int(lim) > 10:
        lim = 10

    img_links = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, single, re.I | re.M)

    for img_link in oboi:
        counter += 1
        img_links.append(img_link)
        if counter >= int(lim):
            break

    return img_links

REVERSE_HANDLER = CommandHandler("reverse", reverse, pass_args=True)
dispatcher.add_handler(REVERSE_HANDLER)
