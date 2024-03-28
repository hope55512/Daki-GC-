from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 19406037))
    API_HASH = getenv("API_HASH", "aa8cac013b63982efea11d1370b0151c")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", None)
    OWNER_ID = int(getenv("OWNER_ID", 5348193047))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "King_of_Ghoul")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Extraction_chats")
    UPDATE_CHAT = getenv("UPDATE_CHAT", "Extraction_chats")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1001968254210"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://eren:eren@cluster0.aor5rcv.mongodb.net/?retryWrites=true&w=majority",
    )
    DB_NAME = getenv("DB_NAME", "DakiV2")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://bgmlfvvgbowbzp:a055fa2034e80df36117e89cb43d7a8364ffdc1fbd61ac61ee09879ceec2c565@ec2-52-201-184-16.compute-1.amazonaws.com:5432/dc8322rjchfp6d"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
