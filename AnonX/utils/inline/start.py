from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك ✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹  اوامر التشغيل  ›⁩",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ اضغط لاضافتي لمجموعتك ›⁩",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹  اوامر التشغيل  ›⁩", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قناة السورس ›⁩", url=f"https://t.me/S0URCE_STAR"
            ),
            InlineKeyboardButton(
                text="‹ مطور البوت ›⁩", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ مطور السورس ›⁩", url=f"https://t.me/RQ_X0"
            )
        ],
     ]
    return buttons
