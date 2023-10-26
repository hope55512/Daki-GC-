

from pyrogram.types import CallbackQuery
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler

from Exon import BOT_NAME, OWNER_ID, OWNER_USERNAME, SUPPORT_CHAT,UPDATE_CHAT
from Exon import Abishnoi as pbot
from Exon import dispatcher,StartTime
import time
import Exon.modules.no_sql.users_db as sql

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@pbot.on_callback_query()
async def close(Client, cb: CallbackQuery):
    if cb.data == "close2":
        await cb.answer()
        await cb.message.delete()


# CALLBACKS


def ABG_about_callback(update, context):
    query = update.callback_query
    if query.data == "ABG_":
        uptime = get_readable_time((time.time() - StartTime))
        query.message.edit_text(
            text=f"๏ ɪ'ᴍ {BOT_NAME} ,ᴀ ᴘᴏᴡᴇʀғᴜʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ʙᴜɪʟᴛ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴇᴀsɪʟʏ."
            "\n\n➲ I scan ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs."
            "\n➲ I ᴄᴀɴ ɢʀᴇᴇᴛ ᴜsᴇʀs ᴡɪsh ᴄᴜsᴛᴏᴍɪᴢᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴀɴᴅ ᴇᴠᴇɴ sᴇᴛ ᴀ ɢʀᴏᴜᴘ's ʀᴜʟᴇs."
            "\n➲ I ʜᴀᴠᴇ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴛɪ-ғʟᴏᴏᴅ sʏsᴛᴇᴍ."
            "\n➲ I ᴄᴀɴ ᴡᴀʀɴ ᴜsᴇʀs ᴜɴsɪʟ ᴛʜᴇʏ ʀᴇᴀᴄʜ ᴍᴀx ᴡᴀʀɴx, ᴡɪᴛʜ ᴇᴀᴄʜ ᴘʀᴇᴅᴇғɪɴᴇᴅ ᴀᴄᴛɪᴏɴs sᴜᴄʜ ᴀs ʙᴀɴ, ᴍᴜᴛᴇ, ᴋɪᴄᴋ, ᴇᴛᴄ."
            "\n➲ I ʜᴀᴠᴇ ᴀ ɴᴏᴛᴇ ᴋᴇᴇᴘɪɴɢ sʏsᴛᴇᴍ, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴇᴠᴇɴ ᴘʀᴇᴅᴇᴛᴇʀᴍɪɴᴇᴅ ʀᴇᴘʟɪᴇs ᴏɴ ᴄᴇʀᴛᴀɪɴ ᴋᴇʏᴡᴏʀᴅs."
            "\n➲ I ᴄʜᴇᴄᴋ ғᴏʀ ᴀᴅᴍɪɴs ᴘᴇʀᴍɪssɪᴏɴs ʙᴇғᴏʀᴇ ᴇxᴇᴄᴜᴛɪɴɢ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴍᴏʀᴇ sᴛᴜғғs"
            "\n\n*─────────────────────*"
            f"\n*➣ ᴜᴩᴛɪᴍᴇ »* {uptime}"
            f"\n*➣ ᴜsᴇʀs »* {sql.num_users()}"
            f"\n*➣ ᴄʜᴀᴛs »* {sql.num_chats()}"
            "\n\n*ɪ ʀᴇᴄᴏᴍᴍᴇɴᴅ  ʏᴏᴜ ᴛᴏ  ᴊᴏɪɴ ᴍʏ ꜱᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ*"
            ,

            
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🚑 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                        InlineKeyboardButton(text="📘 Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHAT}"),
                    ],
                    [
                        InlineKeyboardButton(text=f"💻 Sᴛᴀᴛs", callback_data="stats_callback"),
                        InlineKeyboardButton(text="👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url=f"tg://user?id={OWNER_ID}")
                    ],
                    [
                        InlineKeyboardButton(
                            text="↩ Gᴏ Bᴀᴄᴋ", callback_data="start_back"
                        ),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_admin":
        query.message.edit_text(
            text=f"━━━━━━━ *ᴀᴅᴍɪɴ* ━━━━━━━\nʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ 𝙼ᴜsɪᴄ ᴍᴏᴅᴜʟᴇ\n⍟*ᴀᴅᴍɪɴ*\nᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs\n/pause/n»ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n/resume\n» ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.\n/skip ᴏʀ /next\n»sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.\n/end ᴏʀ /stop\n» ᴇɴᴅ ᴛʜᴇ ᴄᴜʀᴇᴇɴᴛ ᴏɴɢᴏɪɴ sᴛʀᴇᴀᴍ.\n⍟*ᴀᴜᴛʜ*\nᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴀᴜᴛʜ/ᴜɴᴀᴜᴛʜ ᴀɴʏ ᴜsᴇʀ\n• ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴄᴀɴ sᴋɪᴩ, ᴩᴀᴜsᴇ, ʀᴇsᴜᴍᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs./n/auth ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ\n» ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n/unauth ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ \n» ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.\n/authusers \n» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.\n⍟*ᴘʟᴀʏ*\nᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴩʟᴀʏ sᴏɴɢs\n/play <sᴏɴɢ ɴᴀᴍᴇ/ʏᴛ ᴜʀʟ>\n» sᴛᴀʀᴛs ᴩʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴏɴ ᴠᴄ.!",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🕹️", callback_data="source_"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ]
                ]
            ),
        )

    elif query.data == "ABG_notes":
        query.message.edit_text(
            text=f"<b>๏ sᴇᴛᴛɪɴɢ ᴜᴘ ɴᴏᴛᴇs</b>"
            f"\nʏᴏᴜ ᴄᴀɴ sᴀᴠᴇ ᴍᴇssᴀɢᴇ/ᴍᴇᴅɪᴀ/ᴀᴜᴅɪᴏ ᴏʀ ᴀɴʏᴛʜɪɴɢ ᴀs ɴᴏᴛᴇs"
            f"\nᴛᴏ ɢᴇᴛ ᴀ ɴᴏᴛᴇ sɪᴍᴘʟʏ ᴜsᴇ # ᴀᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ ᴀ ᴡᴏʀᴅ"
            f"\n\nʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ sᴇᴛ ʙᴜᴛᴛᴏɴs ғᴏʀ ɴᴏᴛᴇs ᴀɴᴅ ғɪʟᴛᴇʀs (ʀᴇғᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ)",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ", callback_data="ABG_")]]
            ),
        )
    elif query.data == "ABG_ai":
        query.message.edit_text(
            text=f"""
Hᴇʀᴇ Aʀᴇ Tʜᴇ Aɪ Mᴏᴅᴜʟᴇꜱ Lɪꜱᴛ Aᴠᴀɪʟᴀʙʟᴇ Iɴ Aɪ Hᴏꜱʜɪɴᴏ

    ➢ /ask , /chat*:* ᴛᴏ ɢᴇᴛ ꜱᴇᴀʀᴄʜ ʀᴇꜱᴜʟᴛꜱ ꜰʀᴏᴍ Cʜᴀᴛ Gᴘᴛ.

    ➢ /bard*:* ᴛᴏ ɢᴇᴛ ꜱᴇᴀʀᴄʜ ʀᴇꜱᴜʟᴛꜱ ꜰʀᴏᴍ Bᴀʀᴅ Aɪ.

    ➢ /rmbg*:* ᴛᴏ ʀᴇᴍᴏᴠᴇ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴏꜰ ᴛʜᴇ ᴀɴʏ ɪᴍᴀɢᴇ ᴛʜʀᴏᴜɢʜ Aɪ.

    ➢ /upscale*:* Tᴏ ɪɴᴄʀᴇᴀꜱᴇꜱ ᴛʜᴇ Qᴜᴀʟɪᴛʏ ᴏꜰ ᴀɴ ɪᴍᴀɢᴇ ᴛʜʀᴏᴜɢʜ Aɪ.

    ➢ /imagine , /draw*:* ɢᴇᴛ ᴛʜᴇ Aɪ ɢᴇɴᴇʀᴀᴛᴇᴅ ɪᴍᴀɢᴇꜱ ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ᴛʜᴇ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ
""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Gᴏ Bᴀᴄᴋ", callback_data="start_back")]]
            ),
        )
    elif query.data == "ABG_support":
        query.message.edit_text(
            text=f"*๏ {BOT_NAME} sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛs*"
            "\nᴊᴏɪɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ғᴏʀ sᴇᴇ ᴏʀ ʀᴇᴘᴏʀᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴏɴ Hᴏꜱʜɪɴᴏ",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🚑 Sᴜᴘᴘᴏʀᴛ", url=f"t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="📚 Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHAT}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="⤶  Gᴏ Bᴀᴄᴋ", callback_data="ABG_"),
                    ],
                ]
            ),
        )

    elif query.data == "ABG_credit":  # Credit  i hope edit nai hoga
        query.message.edit_text(
            text=f"━━━━━━━ *ᴄʀᴇᴅɪᴛ* ━━━━━━━"
            "\n🛡️ *ᴄʀᴇᴅɪᴛ ꜰᴏʀ Hᴏꜱʜɪɴᴏ ʀᴏʙᴏᴛ* 🛡️"
            "\n\nʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴀɴᴅ"
            f"\nꜱᴘᴏɴꜱᴏʀ ᴏꜰ [{BOT_NAME}](t.me/Exon_Robot)"
            "\n\nʜᴇ ꜱᴘᴇɴᴛ ᴀ ʟᴏᴛ ᴏꜰ ᴛɪᴍᴇ ꜰᴏʀ"
            f"\nᴍᴀᴋɪɴɢ [{BOT_NAME}](t.me/{OWNER_USERNAME}) ᴀ"
            "\nꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="AsuX_help"),
                        InlineKeyboardButton(text="🧑‍", callback_data="source_"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ᴀʙɪsʜɴᴏɪ", url="https://t.me/Abishnoi1M"
                        ),
                        InlineKeyboardButton(
                            text="ᴄʜᴀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"
                        ),
                    ],
                ]
            ),
        )


def Source_about_callback(update, context):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_text(
            text=f"""
*ʜᴇʏ,
 ᴛʜɪs ɪs {BOT_NAME} ,
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.*

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ : [ᴛᴇʟᴇᴛʜᴏɴ](https://github.com/LonamiWebs/Telethon)
[ᴩʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
ᴀɴᴅ ᴜsɪɴɢ [sǫʟᴀʟᴄʜᴇᴍʏ](https://www.sqlalchemy.org) ᴀɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) ᴀs ᴅᴀᴛᴀʙᴀsᴇ.

*ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :* [{BOT_NAME}](https://github.com/Abishnoi69/ExonRobot)


Hᴏꜱʜɪɴᴏ ʀᴏʙᴏᴛ ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ [ᴍɪᴛ ʟɪᴄᴇɴsᴇ](https://github.com/Abishnoi69/ExonRobot/blob/master/LICENSE).
© 2022 - 2023 [sᴜᴘᴘᴏʀᴛ](https://t.me/{SUPPORT_CHAT}) ᴄʜᴀᴛ, ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🏡", callback_data="start_back"),
                        InlineKeyboardButton(text="🛡️", callback_data="ABG_admin"),
                        InlineKeyboardButton(text="💳", callback_data="ABG_credit"),
                        InlineKeyboardButton(text="🧑‍", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="🖥️", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ꜱᴏᴜʀᴄᴇ",
                            url="https://github.com/Abishnoi69/ExonRobot",  # DON'T CHANGE
                        ),
                    ],
                ]
            ),
        )


about_callback_handler = CallbackQueryHandler(
    ABG_about_callback, pattern=r"ABG_", run_async=True
)

source_callback_handler = CallbackQueryHandler(
    Source_about_callback, pattern=r"source_", run_async=True
)


dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(source_callback_handler)
