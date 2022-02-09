
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I ᴀᴍ 𝘽𝙤𝙩 𝘿𝙪𝙣𝙞𝙮𝙖 𝙈𝙪𝙨𝙞𝙘   
ʙᴏᴛ ʜᴀɴᴅʟᴇ ʙʏ [𝘽𝙤𝙩 𝘿𝙪𝙣𝙞𝙮𝙖](https://t.me/BotDuniya)
Thanks to add me 😇**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Handle", url="https://t.me/FriDayNetwork"
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐋𝐢𝐬𝐭🧰", url="https://telegra.ph/%F0%9D%98%BE%F0%9D%99%A4%F0%9D%99%A2%F0%9D%99%A2%F0%9D%99%96%F0%9D%99%A3%F0%9D%99%99%F0%9D%99%A8-%F0%9D%99%81%F0%9D%99%A4%F0%9D%99%A7-%F0%9D%98%BD%F0%9D%99%A4%F0%9D%99%A9-%F0%9D%98%BF%F0%9D%99%AA%F0%9D%99%A3%F0%9D%99%9E%F0%9D%99%AE%F0%9D%99%96-%F0%9D%98%BD%F0%9D%99%8A%F0%9D%99%8F-02-08-3"
                    )
                  ],[
                    InlineKeyboardButton(
                       " 𝐒𝐮𝐩𝐩𝐨𝐫𝐭👿", url="https://t.me/PmPermit"
                    ),
                    InlineKeyboardButton(
                        "𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url="https://t.me/BotDuniya"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
