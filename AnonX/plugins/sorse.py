
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "يا سورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/abc6b25ceb81316ab1e1e.jpg",
        caption=f"""╭──── • ✭ • ────╮

╭⎋ ⚝ ‹ [DeV SiMo](https://t.me/DaRrKNneSs_1) ›♪

  -⊚ ⚝ ‹ [DeV RoWeS](https://t.me/RQ_X0) ›♪
   
 ╰⊚‹ [SoUrCe StAr](https://t.me/S0URCE_STAR) ›♪

╰──── • ✭ • ────╯

✭ ᴛʜᴇ ʙᴇѕᴛ ѕᴏᴜʀᴄᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ ᴅᴇᴠ ʀᴏᴡᴇs ›", url=f"https://t.me/RQ_X0"), 
                ],[
                    InlineKeyboardButton(
                        "ᴅᴇᴠ sɪᴍᴏ", url=f"https://t.me/DaRrKNneSs_1"),
                ],[
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ sᴛᴀʀ", url=f"https://t.me/S0URCE_STAR"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )





@app.on_message(command(["غنيلي", "غني", "غغ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغنية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["‹ رمزيات شباب","‹ رمزيات شباب"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
