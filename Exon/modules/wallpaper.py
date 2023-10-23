import random
from random import randint

import requests
from pyrogram import enums
from pyrogram.types import Message

from Exon import Abishnoi, arq


@Abishnoi.on_cmd(["wallpaper"])
async def wallpaper(_, msg):
    if len(msg.command) < 2:
        await msg.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
        return
    else:
        pass

    query = (
        msg.text.split(None, 1)[1]
        if len(msg.command) < 3
        else msg.text.split(None, 1)[1].replace(" ", "%20")
    )

    if not query:
        await msg.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
    else:
        pass

    url = f"https://api.safone.me/wall?query={query}"
    re = requests.get(url).json()
    walls = re.get("results")
    if not walls:
        await msg.reply_text("ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ! ")
        return
    wall_index = randint(0, len(walls) - 1)
    wallpaper = walls[wall_index]
    wallpaper.get("imageUrl")
    preview = wallpaper.get("thumbUrl")
    title = wallpaper.get("title")
    try:
        await Abishnoi.send_chat_action(msg.chat.id, enums.ChatAction.UPLOAD_PHOTO)
        await msg.reply_photo(
            preview, caption=f"🔎 ᴛɪᴛʟᴇ - {title}"
        )
    # await msg.reply_document(pic, caption=f"🔎 ᴛɪᴛʟᴇ - {title} \n🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {msg.from_user.mention}")
    except Exception as error:
        await msg.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ.\n {error}")


@Abishnoi.on_cmd("wall")
async def wall(_, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ !")
    search = m.text.split(None, 1)[1]
    x = await arq.wall(search)
    y = x.result
    await m.reply_photo(random.choice(y).url_image)
    # await m.reply_document(random.choice(y).url_image)
