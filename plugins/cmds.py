import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

WELCOME = "Hello! I'm Echo Payments Bot."
IMG = "https://i.ibb.co/xK56gh8W/photo-2025-11-14-13-10-23-7572567765697953804.jpg"
EFCT = 5104841245755180586

btns = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Repo", url="https://github.com/XalFH/Echo-Payments-Bot")]]
)

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        IMG,
        caption=WELCOME,
        reply_markup=btns,
        message_effect_id=EFCT, 
        quote=True,
        has_spoiler=True
    )
