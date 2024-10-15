import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7812968882:AAGEw8FChwxTTTPd5wyYhfDYONEizak6vh4")
BOT_NAME = getenv("BOT_NAME", "Music Bix Bot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("20771536"))
API_HASH = getenv("d1ad0e46cda0bdd7f44001040b909e22")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicBixBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MusicBix")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MusicBixSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MusicBixOfficial")
OWNER_NAME = getenv("OWNER_NAME", "Badboyanim") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("6918300873")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://jaychonkar57:<db_password>@musicbixbot.m68no.mongodb.net/") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002411867438")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
