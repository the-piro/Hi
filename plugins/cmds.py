import re
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from xtra import snd, Btn  

WELCOME = "Hello! I'm Echo Payments Bot."
IMG = "https://i.ibb.co/xK56gh8W/photo-2025-11-14-13-10-23-7572567765697953804.jpg"
EFCT = 5104841245755180586


@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    btn = Btn()
    btn.url_button("Repo", "https://github.com/XalFH/Echo-Payments-Bot")
    buttons = btn.build_menu()

    await snd(
        message,
        WELCOME,
        buttons=buttons,
        photo=IMG,
        message_effect_id=EFCT,
        has_spoiler=True
    )
