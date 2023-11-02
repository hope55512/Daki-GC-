from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from Exon import BOT_NAME, BOT_USERNAME, OWNER_ID, SUPPORT_CHAT,Abishnoi as pbot


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"**ʜᴇʏ {message.from_user.mention},\n\n✨ɪ ᴀᴍ {BOT_NAME}**\n▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
    TEXT += f"➢ **ᴍʏ ᴍᴀsᴛᴇʀ :** [Kaneki](tg://user?id={OWNER_ID})\n\n"
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
        "https://telegra.ph/file/60367eeda9886bab0f7ef.jpg",
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "Alive"
