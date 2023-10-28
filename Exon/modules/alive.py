from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from Exon import BOT_NAME, BOT_USERNAME, OWNER_ID, SUPPORT_CHAT,Abishnoi as pbot

import random
PM_PHOTO = [
    "https://te.legra.ph/file/e833e8e51f8f141f05b89.jpg",
    "https://telegra.ph/file/f3f2fbc1f4fe27be928b0.jpg",
    "https://telegra.ph/file/fb2d9535da92eb4e1cce1.jpg",
    "https://telegra.ph/file/0549ae4812a41b4d76e9b.jpg",
    "https://telegra.ph/file/f6edd6a18ea0dea31ba5f.jpg",
    "https://telegra.ph/file/b6448fa7b7a1b7ff89faa.jpg",
    "https://telegra.ph/file/6e6c13e103826fedba7c6.jpg",
    "https://telegra.ph/file/e50b360220004444350fd.jpg",
]

@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"**ʜᴇʏ {message.from_user.mention},\n\n✨ɪ ᴀᴍ {BOT_NAME}**\n▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
    TEXT += f"➢ **ᴍʏ ᴍᴀsᴛᴇʀ :** [KIRA](tg://user?id={OWNER_ID})\n\n"
    TEXT += f"➢ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"➢ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"➢ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}`"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
        [
        InlineKeyboardButton(
            text="+ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ +",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    ]
    await message.reply_photo(
        {random.choice(PM_PHOTO)},
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "Alive"
