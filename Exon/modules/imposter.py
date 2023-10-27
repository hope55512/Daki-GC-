from pyrogram import filters
from pyrogram.types import Message

from Exon.utils.mongo import (
    add_userdata,
    usr_data,
    get_userdata,
    check_imposter,
    impo_on,
    impo_off,
)
from Exon import Abishnoi as app
from Exon.modules.helper_funcs.status import user_admin


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=1)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_imposter(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
➢ **Iᴍᴘᴏꜱᴛᴇʀ Dᴇᴛᴇᴄᴛᴇᴅ** :
━━━━━━━━━━━━━━━━━━━
➣ User: {message.from_user.mention}
➣ ID: {message.from_user.id}
━━━━━━━━━━━━━━━━━━━\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
➢ **Cʜᴀɴɢᴇᴅ UꜱᴇʀNᴀᴍᴇ**:
━━━━━━━━━━━━━━━━━━━
➣ FROM: {bef}
➣ TO: {aft}
━━━━━━━━━━━━━━━━━━━\n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
➢ **Cʜᴀɴɢᴇᴅ Fɪʀꜱᴛ Nᴀᴍᴇ**
━━━━━━━━━━━━━━━━━━━
➣ FROM: {bef}
➣ TO: {aft}
━━━━━━━━━━━━━━━━━━━\n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
➢ **Cʜᴀɴɢᴇᴅ Lᴀꜱᴛ Nᴀᴍᴇ**:
━━━━━━━━━━━━━━━━━━━
➣ FROM: {bef}
➣ TO: {aft}
━━━━━━━━━━━━━━━━━━━\n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo("https://te.legra.ph/file/335354fb0905b7274bb52.jpg", caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
@user_admin
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("Check help Section For Getting Help")
    if message.command[1] == "on":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("Imposter Mode Is Already Enabled")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"Successfully Enabled Imposter Mode For {message.chat.title}")
    elif message.command[1] == "off":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("Imposter Mode Is Already Disabled")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"Successfully Enabled Imposter Mode For {message.chat.title}")
    else:
        await message.reply("Check help Section For Getting Help")


from Exon.modules.language import gs


def get_help(chat):
    return gs(chat, "imposter_help")


__mod_name__ = "Iᴍᴘᴏꜱᴛᴇʀ 👁️‍🗨️"
__help__ = """
──「 Iᴍᴘᴏꜱᴛᴇʀ 」──

**➢ /imposter [on/off]** - Turn On The Watcher For Your Group Which Notifies About User Who Change Name or Username
"""
