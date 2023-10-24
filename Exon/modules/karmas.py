import asyncio

from pyrogram import filters
from telegram import ParseMode

from Exon import OWNER_ID,Abishnoi as pbot
from Exon.utils.errors import capture_err
from Exon.modules.no_sql.karma_db import (
    alpha_to_int,
    get_karma,
    get_karmas,
    int_to_alpha,
    is_karma_on,
    karma_off,
    karma_on,
    update_karma,
)

regex_upvote = r"^((?i)\+|\+\+|\+1|thx|thanx|thanks|🖤|❣️|💝|💖|💕|❤|💘|cool|good|👍|baby|mukesh|thank you|gud|thankyou|love|pro)$"
regex_downvote = r"^(\-|\-\-|\-1|👎|💔|noob|weak|fuck off|nub|gey|mf)$"


karma_positive_group = 3
karma_negative_group = 4


@pbot.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_upvote)
    & ~filters.via_bot
    & ~filters.bot,
    group=karma_positive_group,
)
@capture_err
async def upvote(_, message):
    if not await is_karma_on(message.chat.id):
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(
            "ᴡᴇʟʟ, ʜᴇ's ᴍʏ ᴏᴡɴᴇʀ. sᴏ ʏᴇᴀʜ, ʜᴇ ɪs ᴀʟᴡᴀʏs ʀɪɢʜᴛ ᴀɴᴅ ᴇᴠᴇʀʏᴏɴᴇ ᴋɴᴏᴡs ʜᴇ ɪs ᴀ ɢᴏᴏᴅ ᴘᴇʀsᴏɴ ᴛᴏᴏ."
        )
        return
    if message.reply_to_message.from_user.id == 6225939804:
        await message.reply_text(
            "ᴡᴇʟʟ, ꜱʜᴇ's ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴡᴀɪꜰᴜ. ꜱʜᴇ ʏᴇᴀʜ, ꜱʜᴇ ɪs ᴀʟᴡᴀʏs ʀɪɢʜᴛ."
        )
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    if current_karma:
        current_karma = current_karma["karma"]
        karma = current_karma + 1
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f"ɪɴᴄʀᴇᴍᴇɴᴛᴇᴅ ᴋᴀʀᴍᴀ ᴏғ \n{user_mention} ʙʏ 1.\n\n✨ **ᴛᴏᴛᴀʟ ᴩᴏɪɴᴛs :** {karma}"
    )


@pbot.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_downvote)
    & ~filters.via_bot
    & ~filters.bot,
    group=karma_negative_group,
)
@capture_err
async def downvote(_, message):
    if not is_karma_on(message.chat.id):
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(
            "ᴡᴛғ !, ʏᴏᴜ ᴅᴏɴ'ᴛ ᴀɢʀᴇᴇ ᴡɪᴛʜ ᴍʏ ᴏᴡɴᴇʀ. ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ɢᴏᴏᴅ ᴩᴇʀsᴏɴ."
        )
        return
    if message.reply_to_message.from_user.id == 6225939804:
        await message.reply_text(
            "ᴡᴛғ !, ʏᴏᴜ ᴅᴏɴ'ᴛ ᴀɢʀᴇᴇ ᴡɪᴛʜ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴡᴀɪꜰᴜ. ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ɢᴏᴏᴅ ᴩᴇʀsᴏɴ."
        )
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    if current_karma:
        current_karma = current_karma["karma"]
        karma = current_karma - 1
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f"ᴅᴇᴄʀᴇᴍᴇɴᴛᴇᴅ ᴋᴀʀᴍᴀ ᴏғ \n{user_mention} ʙʏ 1.\n\n**✨ ᴛᴏᴛᴀʟ ᴩᴏɪɴᴛs :** {karma}"
    )

@pbot.on_message(filters.command("karmastat") & filters.group)
@capture_err
async def karma(_, message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        m = await message.reply_text("Analyzing Karma...Will Take 10 Seconds")
        karma = await get_karmas(chat_id)
        if not karma:
            await m.edit("No karma in DB for this chat.")
            return
        msg = f"**Karma list of {message.chat.title}:- **\n\n"
        limit = 0
        karma_dicc = {}
        for i in karma:
            user_id = await alpha_to_int(i)
            user_karma = karma[i]["karma"]
            karma_dicc[str(user_id)] = user_karma
        karma_arranged = dict(
            sorted(karma_dicc.items(), key=lambda item: item[1], reverse=True)
        )
        if not karma_dicc:
            await m.edit("No karma in DB for this chat.")
            return
        for user_idd, karma_count in karma_arranged.items():
            if limit > 9:
                break
            try:
                user = await pbot.get_users(int(user_idd))
                await asyncio.sleep(0.8)
            except Exception:
                continue
            first_name = user.first_name
            if not first_name:
                continue
            username = user.username
            mention = f"[{first_name}](tg://user?id={user_idd})"
            msg += f"{karma_count} - {mention} \n"
            limit += 1
        await m.edit(msg)
    else:
        user_id = message.reply_to_message.from_user.id
        karma = await get_karma(chat_id, await int_to_alpha(user_id))
        karma = karma["karma"] if karma else 0
        await message.reply_text(f"**ᴛᴏᴛᴀʟ ᴩᴏɪɴᴛs :** {karma}")


@pbot.on_message(filters.command("karma") & ~filters.private)
@pbot.adminsOnly(permissions="can_change_info", is_both=True)
async def captcha_state(_, message):
    usage = "**Usage:**\n/karma [ON|OFF]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        await karma_on(message.chat.id)
        await message.reply_text("Enabled karma system.")
    elif state == "off":
        await karma_off(message.chat.id)
        await message.reply_text("Disabled karma system.")
    else:
        await message.reply_text(usage)


__help__ = """
ᴜᴘᴠᴏᴛᴇ - ᴜsᴇ ᴜᴘᴠᴏᴛᴇ ᴋᴇʏᴡᴏʀᴅs ʟɪᴋᴇ "+", "+1", "thanks", ᴇᴛᴄ. ᴛᴏ ᴜᴘᴠᴏᴛᴇ ᴀ ᴍᴇssᴀɢᴇ.
ᴅᴏᴡɴᴠᴏᴛᴇ - ᴜsᴇ ᴅᴏᴡɴᴠᴏᴛᴇ ᴋᴇʏᴡᴏʀᴅs ʟɪᴋᴇ "-", "-1", ᴇᴛᴄ. ᴛᴏ ᴅᴏᴡɴᴠᴏᴛᴇ ᴀ ᴍᴇssᴀɢᴇ.

*ᴄᴏᴍᴍᴀɴᴅs*

➢ `/karmastat`:- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴀᴛ ᴜsᴇʀ's  ᴋᴀʀᴍᴀ ᴘᴏɪɴᴛs

➢ `/karmastat`:- sᴇɴᴅ ᴡɪᴛʜᴏᴜᴛ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴋᴀʀᴍᴀ ᴘᴏɪɴᴛ ʟɪsᴛ of ᴛᴏᴘ 10

➢ `/karma` OFF|ON - ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴋᴀʀᴍᴀ sʏsᴛᴇᴍ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
"""


__mod_name__ = "Kᴀʀᴍᴀ"

from Exon.modules.language import gs


def get_help(chat):
    return gs(chat, "karma_help")