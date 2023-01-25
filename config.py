## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = "BAB6G19Ot8OLenItttpVUPMtxMwDOP5i0-M34L8c5vTxr4hABQBPhGJeBp3d6ww93cwaH1PvuU_f7F9zDavOcBLZwvcxC9jXYBXk0BpjQeIAcHumJy5FwFXGFI8wSp9PPCAx8tvWFOtQwXrH7M_VrB2a7h0LZlYjmBNgDLfLqpMCtuViuAYWkyXfUITzC8-JrIYVZgg2rWoIb6kMANrsjPFTvbFYQYvFE7lROrhnKnBLCBVe6MSth-gpOubTB-CE98FTv6S6-X2ORks1enx69e-7wQER-vv9yoUXteb1nEV_AZDPI3_LRyKTv40ISXxBpOeK-POIXHN5E2uPkgm0VfJUAAAAAUXgjJAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5941659598:AAFCJGzLnIYOBZz2fq2EiNgNolnFmuTphBk")
BOT_NAME = getenv("BOT_NAME", "『𖤍 Lêɠêɳ̃ᴅᴍᴜsɪᴄ࿐』➙ ꯭🇮🇳꯭")

API_ID = int(getenv("API_ID", "6296490"))
API_HASH = getenv("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://pankajsain:pankaj9024@cluster0.fdc33h6.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SexyyNeo")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "IPMUSIXBOT")
OWNER_ID = getenv("OWNER_ID", "5467311248" )
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Sexsuxassist")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FRIENDZVIBES")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FRIENDZVIBES")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5763920115").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/dd3c08bd6b1820b14a6d0.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/dd3c08bd6b1820b14a6d0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
