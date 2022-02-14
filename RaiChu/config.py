## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "14144870"))
API_HASH = getenv("API_HASH", "6da719b3f77df0ad9fd116c16856ae31")
OWNER_NAME = getenv("OWNER_NAME", "💘✨★✰𝙒𝙚𝙞 𝙒𝙪𝙭𝙞𝙖𝙣✰★✨💘")
ALIVE_NAME = getenv("ALIVE_NAME", "❥︎☯︎༱៚Dᴀʀᴋ⚕Sᴡᴏʀᴅ༗༱☯︎❥︎")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "ItzmeDarkSword")
BOT_USERNAME = getenv("BOT_USERNAME", "ItzmeDarkSwordbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "❥︎☯︎༱៚Dᴀʀᴋ⚕Sᴡᴏʀᴅ༗༱☯︎❥︎")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "itzmedarkswordsupportgroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "itzmedarkswordsupportchannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG","https://telegra.ph/file/a7ed67c650aaeb239c213.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/2f70d971d24b7ad3c10e7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/d7b65296dec4576d23ef1.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/84e59132f4b3512a1696e.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/0a408ad2a8e8d00f1ec59.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/13e375fc0f203bc077fa6.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/5007a36cb6d845ad19d3d.jpg")
