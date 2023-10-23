import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

#Exon => Your Bots File Name
import Exon.modules.no_sql.users_db as sql
from Exon import DEV_USERS, OWNER_ID
from Exon import Abishnoi as pgram
from Exon.modules.no_sql.users_db import get_all_users
from asyncio import sleep
SUDOER = DEV_USERS + OWNER_ID

# get_arg function to retrieve an argument from a message
def get_arg(message):
    args = message.text.split(" ")
    if len(args) > 1:
        return args[1]
    else:
        return None

# Broadcast Function
@pgram.on_message(filters.command("sbroadcast"))
async def broadcast_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    texttt = message.text.split(" ")

    if user_id not in [OWNER_ID] + DEV_USERS:
        await message.reply_text(
            "You are not authorized to use this command. Only the owner and authorized users can use it."
        )
        return

    if len(texttt) < 2:
        return await message.reply_text(
            "<b>BROADCASTING COMMANDS</b>\n-user : broadcasting all user's DM\n-group : broadcasting all groups\n-all : broadcasting both\nEx: /broadcast-user"
        )

    if message.reply_to_message is None and not get_arg(message):
        return await message.reply_text(
            "<b>Please provide a message or reply to a message</b>"
        )

    tex = await message.reply_text("<code>Starting global broadcast...</code>")

    usersss = 0
    chatttt = 0
    uerror = 0
    cerror = 0
    chats = sql.get_all_chats() or []
    users = get_all_users()

    if "-all" in texttt:
        texttt.append("-user")
        texttt.append("-group")

    if "-user" in texttt:
        for chat in users:
            if message.reply_to_message:
                msg = message.reply_to_message
            else:
                msg = get_arg(message)
            try:
                if message.reply_to_message:
                    aa = await msg.copy(int(chat["_id"]),)
                else:
                    aa = await client.send_message(int(chat["_id"]), msg)

                usersss += 1
                await asyncio.sleep(0.3)
            except Exception:
                uerror += 1
                await asyncio.sleep(0.3)
    if "-group" in texttt:
        for chat in chats:
            if message.reply_to_message:
                msg = message.reply_to_message
            else:
                msg = get_arg(message)
            try:
                if message.reply_to_message:
                    aa = await msg.copy(int(chat["chat_id"]))
                else:
                    aa = await client.send_message(int(chat["chat_id"]))

                chatttt += 1
                await asyncio.sleep(0.3)
            except Exception:
                cerror += 1
                await asyncio.sleep(0.3)

    await tex.edit_text(
        f"<b>Message Successfully Sent</b> \nTotal Users: <code>{usersss}</code> \nFailed Users: <code>{uerror}</code> \nTotal GroupChats: <code>{chatttt}</code> \nFailed GroupChats: <code>{cerror}</code>"
    )



@pgram.on_cmd(["forward","fwd"] &SUDOER)
async def forward_type_broadcast(c: Client, m: Message):
    repl = m.reply_to_message
    if not repl:
        await m.reply_text("Please reply to message to broadcast it")
        return
    split = m.command

    chat = [i["chat_id"] for i in sql.get_all_chats()]
    user = [i["_id"] for i in get_all_users()]
    alll = chat + user
    if len(split) != 2:
        tag = "all"
    else:
        try:
            if split[0].lower() == "-u":
                tag = "user"
            elif split[0].lower() == "-c":
                tag = "chat"
            else:
                tag = "all"
        except IndexError:
            pass
    if tag == "chat":
        peers = chat
    elif tag == "user":
        peers = user
    else:
        peers = alll
    
    xx = await m.reply_text("Broadcasting...")

    failed = 0
    total = len(peers)
    for peer in peers:
        try:
            await repl.forward(int(peer))
            await sleep(0.1)
        except Exception:
            failed += 1
            pass
    txt = f"Broadcasted message to {total-failed} peers out of {total}\nFailed to broadcast message to {failed} peers"
    if not failed:
        txt = f"Broadcasted message to {total} peers"
    await m.reply_text(txt)
    try:
        await xx.delete()
    except Exception:
        pass
    return


# @pgram.on_cmd(["cforward","cfwd"] &SUDOER)
# async def forward_type_broadcast(c: Client, m: Message):
#     repl = m.reply_to_message
    if not repl:
        await m.reply_text("Please reply to message to broadcast it")
        return
    split = m.command

    chat = sql.get_all_chats()
    user = [i["chat_id"] for i in sql.get_all_chats()]
    alll = chat + user
    if len(split) != 2:
        tag = "all"
    else:
        try:
            if split[0].lower() == "-u":
                tag = "user"
            elif split[0].lower() == "-c":
                tag = "chat"
            else:
                tag = "all"
        except IndexError:
            pass
    if tag == "chat":
        peers = chat
    elif tag == "user":
        peers = user
    else:
        peers = alll
    
        xx = await m.reply_text("Broadcasting...")

        failed = 0
        total = len(peers)
        for peer in peers:
            try:
                await repl.forward(int(peer))
                await sleep(0.1)
            except Exception:
                failed += 1
                pass
        txt = f"Broadcasted message to {total-failed} peers out of {total}\nFailed to broadcast message to {failed} peers"
        if not failed:
            txt = f"Broadcasted message to {total} peers"
        await m.reply_text(txt)
        try:
            await xx.delete()
        except Exception:
            pass
        return