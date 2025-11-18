from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from xtra import snd, Btn  

WELCOME = "Hello! I'm Echo Payments Bot."
IMG = "https://i.ibb.co/HfJzg0yW/photo-2025-11-18-15-51-30-7574093630139269152.jpg"
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
