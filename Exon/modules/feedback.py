"""
MIT License

Copyright (c) 2022 ABISHNOI69

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi1m
#     UPDATE   :- Abishnoi_bots
#     GITHUB :- ABISHNOI69 ""

import random

from telegram import ParseMode
from telethon import Button

from Exon import OWNER_ID, SUPPORT_CHAT
from Exon import telethn as tbot

from ..events import register


@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    Exon = (
        "https://telegra.ph/file/b338214b85fee0c81aec5.jpg",
        "https://telegra.ph/file/8e6f8bad1d448e3398468.jpg",
        "https://telegra.ph/file/28296667cb727005c5f9e.jpg",
        "https://telegra.ph/file/ae35d8a131d0e175c0e49.jpg",
    )
    NATFEED = ("https://te.legra.ph/file/7b94977d85a9fd152081a.jpg",)
    BUTTON = [[Button.url("Go To Support Group", f"https://t.me/{SUPPORT_CHAT}")]]
    TEXT = "ᴛʜᴀɴᴋꜱ ꜰᴏʀ ʏᴏᴜʀ ꜰᴇᴇᴅʙᴀᴄᴋ, ɪ ʜᴏᴘᴇ ʏᴏᴜ ʜᴀᴘᴘʏ ᴡɪᴛʜ ᴏᴜʀ ꜱᴇʀᴠɪᴄᴇ."
    GIVE = "ɢɪᴠᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ ꜰᴏʀ ꜰᴇᴇᴅʙᴄᴋ ✨"
    logger_text = f"""
**ɴᴇᴡ ꜰᴇᴇᴅʙᴀᴄᴋ**

**ꜰʀᴏᴍ ᴜꜱᴇʀ:** {mention}
**ᴜꜱᴇʀɴᴀᴍᴇ:** @{e.sender.username}
**ᴜꜱᴇʀ ɪᴅ:** `{e.sender.id}`
**ꜰᴇᴇᴅʙᴀᴄᴋ:** `{e.text}`
"""
    if e.sender_id != OWNER_ID and not quew:
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=random.choice(NATFEED),
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(Exon),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(Exon), buttons=BUTTON)
