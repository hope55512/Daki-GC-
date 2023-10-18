import itertools
from collections.abc import Iterable
from typing import Generator, List, Union

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

import Exon.modules.sql.language_sql as sql
from Exon.langs import get_language, get_languages, get_string
from Exon.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Exon.modules.helper_funcs.decorators import Exoncallback, Exoncmd


def paginate(iterable: Iterable, page_size: int) -> Generator[List, None, None]:
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (
            itertools.islice(i1, page_size, None),
            list(itertools.islice(i2, page_size)),
        )
        if len(page) == 0:
            break
        yield page


def gs(chat_id: Union[int, str], string: str) -> str:
    try:
        lang = sql.get_chat_lang(chat_id)
        return get_string(lang, string)
    except:
        return "ᴍᴇ ɴᴏᴡ ʙᴜsʏ ᴡʜᴇɴ ғʀᴇᴇ ᴀᴅᴅ ᴛʜɪs "


@Exoncmd(command="language")
@user_admin
def set_lang(update: Update, _) -> None:
    chat = update.effective_chat
    msg = update.effective_message

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = []
    for code, name in get_languages().items():
        keyb.append(
            InlineKeyboardButton(
                text=name,
                callback_data=f"setLang_{code}",
            )
        )

    keyb = list(paginate(keyb, 2))
    keyb.append(
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴜs ɪɴ ᴛʀᴀɴsʟᴀᴛɪᴏɴs",
                url="https://github.com/Abishnoi69/ExonRobot",  # plz. Don't edit and change
            )
        ]
    )
    msg.reply_text(msg_text, reply_markup=InlineKeyboardMarkup(keyb))


@Exoncallback(pattern=r"setLang_")
@user_admin_no_reply
def lang_button(update: Update, _) -> None:
    query = update.callback_query
    chat = update.effective_chat

    query.answer()
    lang = query.data.split("_")[1]
    sql.set_lang(chat.id, lang)

    query.message.edit_text(
        gs(chat.id, "set_chat_lang").format(get_language(lang)[:-3])
    )
