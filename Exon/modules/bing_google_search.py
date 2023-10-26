import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Exon import Abishnoi as app
from Exon import dispatcher
from Exon.modules.disable import DisableAbleCommandHandler
from search_engine_parser import GoogleSearch
import re
import urllib
import urllib.request

API_URL = "https://sugoi-api.vercel.app/search"


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

# @app.on_message(filters.command("google"))
# async def google_search(_,event):

#     webevent = await event.reply("🔎")
#     match = event.pattern_match.group(1)
#     page = re.findall(r"page=\d+", match)
#     try:
#         page = page[0]
#         page = page.replace("page=", "")
#         match = match.replace("page=" + page[0], "")
#     except IndexError:
#         page = 1
#     search_args = (str(match), int(page))
#     gsearch = GoogleSearch()
#     gresults = await gsearch.async_search(*search_args)
#     msg = ""
#     for i in range(len(gresults["links"])):
#         try:
#             title = gresults["titles"][i]
#             link = gresults["links"][i]
#             desc = gresults["descriptions"][i]
#             msg += f"➢[{title}]({link})\n**{desc}**\n\n"
#         except IndexError:
#             break
#     await webevent.edit(
#         "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
#     )

@app.on_message(filters.command("bing"))
async def bing_search(client: Client, message: Message):
    try:
        if len(message.command) == 1:
            await message.reply_text("Please provide a keyword to search.")
            return

        keyword = " ".join(
            message.command[1:]
        )  # Assuming the keyword is passed as arguments
        params = {"keyword": keyword}
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("No results found.")
            else:
                message_text = "🔎"
                for result in results[:7]:
                    title = result.get("title", "")
                    link = result.get("link", "")
                    message_text += f"{title}\n{link}\n\n"
                await message.reply_text(message_text.strip())
        else:
            await message.reply_text("Sorry, something went wrong with the search.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
 

__help__ = """
Tʜᴇ ᴍᴏᴅᴜʟᴇ ᴛʜᴀᴛ ʜᴇʟᴘ ʏᴏᴜ ꜱᴇᴀʀᴄʜ ᴀɴᴅ ɢᴇᴛ Qᴜᴇʀʏ ʀᴇꜱᴜʟᴛꜱ ꜰʀᴏᴍ ʙɪɴɢ ᴀɴᴅ ɢᴏᴏɢʟᴇ.

 ➢ /google*:* ᴛᴏ ɢᴇᴛ ꜱᴇᴀʀᴄʜ ʀᴇꜱᴜʟᴛꜱ ꜰʀᴏᴍ ɢᴏᴏɢʟᴇ.

 ➢ /bing*:* ᴛᴏ ɢᴇᴛ ꜱᴇᴀʀᴄʜ ʀᴇꜱᴜʟᴛꜱ ꜰʀᴏᴍ ʙɪɴɢ.

 ➢ /ud*:* ᴏ ꜱᴇᴀʀᴄʜ Qᴜᴇʀʏ  ᴏɴ ᴜʀʙᴀɴ ᴅᴇᴄᴛ.

 ➢ /wiki*:* ᴛ ᴛᴏ ꜱᴇᴀʀᴄʜ Qᴜᴇʀʏ ᴏɴ ᴡɪᴋɪᴘᴇᴅɪᴀ
"""

__mod_name__ = "Sᴇᴀʀᴄʜ 🔎"

from Exon.modules.language import gs


def get_help(chat):
    return gs(chat, "search_help")

