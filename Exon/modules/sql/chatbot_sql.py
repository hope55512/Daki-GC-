import threading

from sqlalchemy import Column, String

from Exon.modules.sql import BASE, SESSION


class HoshinoChats(BASE):
    __tablename__ = "Hoshino_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


HoshinoChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Hoshino(chat_id):
    try:
        chat = SESSION.query(HoshinoChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Hoshino(chat_id):
    with INSERTION_LOCK:
        Hoshinochat = SESSION.query(HoshinoChats).get(str(chat_id))
        if not Hoshinochat:
            Hoshinochat = HoshinoChats(str(chat_id))
        SESSION.add(Hoshinochat)
        SESSION.commit()


def rem_Hoshino(chat_id):
    with INSERTION_LOCK:
        Hoshinochat = SESSION.query(HoshinoChats).get(str(chat_id))
        if Hoshinochat:
            SESSION.delete(Hoshinochat)
        SESSION.commit()