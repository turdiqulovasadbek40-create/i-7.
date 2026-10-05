import os
import asyncio
import logging
from threading import Thread

from flask import Flask

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# =========================================================
# BOT TOKEN
# =========================================================

TOKEN = 8920455563:AAFiVQoxu_m7ZyZPunNsAAWJDfeZ5mtynucos.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN Render Environment Variables'da topilmadi!")


bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================================================
# FLASK SERVER - RENDER UCHUN
# =========================================================

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot ishlayapti!"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )


def keep_alive():
    thread = Thread(target=run_web, daemon=True)
    thread.start()


# =========================================================
# 31 TA MAVZU
# =========================================================

topics = [
    "Cendlar",
    "AFU, SFU, FU, SELF FU, Inside FU",
    "Negationlar",
    "X2 va X3 Negation",
    "First, Third",
    "Likvidlik",
    "Major Minor Doji",
    "Doji",
    "LAL",
    "Imbalans",
    "Inside FU",
    "Self FU",
    "HCS modeli",
    "HCS X1, X2, X3",
    "HCS Negation",
    "HCS + Negation modeli",
    "True Stop Loss",
    "True Stop Loss bilan ishlash",
    "Time Frame Stretch",
    "TFS Established, Fresh, Closed",
    "Self Negation",
    "Entry modellari",
    "Special Candle",
    "0.1 Apart",
    "LAOL Negation",
    "X3 Negation",
    "X2 Manipulation",
    "X3 Manipulation",
    "X2 Negation",
    "True HCS",
    "Yo'nalish topish"
]


# =========================================================
# /START
# =========================================================

@dp.message(Command("start"))
async def start_handler(message: types.Message):

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎓 Discord Live"),
                KeyboardButton(text="ℹ️ Ma'lumot")
            ],
            [
                KeyboardButton(text="📚 Kurs haqida ma'lumot olish"),
                KeyboardButton(text="👤 Admin bilan bog'lanish")
            ]
        ],
        resize_keyboard=True
    )

    text = (
        "Assalomu alaykum! 👋\n\n"
        "🎓 <b>To'liq Bank Sistema</b> kursiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang."
    )

    await message.answer(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================================================
# DISCORD LIVE
# =========================================================

@dp.message(F.text == "🎓 Discord Live")
async def discord_live_handler(message: types.Message):

    text = (
        "🎓 <b>DISCORD LIVE</b>\n\n"
        "📚 <b>TO'LIQ BANK SISTEMA</b>\n\n"
        "Kursda quyidagi mavzular mavjud:\n\n"
    )

    for i, topic in enumerate(topics, 1):
        text += f"{i}. {topic}\n"

    text += (
        "\n\n"
        "📌 Kurs haqida batafsil ma'lumot olish uchun "
        "administrator bilan bog'laning."
    )

    await message.answer(
        text,
        parse_mode="HTML"
    )


# =========================================================
# MA'LUMOT
# =========================================================

@dp.message(F.text == "ℹ️ Ma'lumot")
async def info_handler(message: types.Message):

    text = (
        "ℹ️ <b>MA'LUMOT</b>\n\n"
        "🎓 To'liq Bank Sistema — trading bo'yicha "
        "31 ta mavzuni o'z ichiga olgan kurs.\n\n"
        "Kursga ulanish va batafsil ma'lumot uchun "
        "administrator bilan bog'laning."
    )

    await message.answer(
        text,
        parse_mode="HTML"
    )


# =========================================================
# KURS HAQIDA
# =========================================================

@dp.message(F.text == "📚 Kurs haqida ma'lumot olish")
async def course_info_handler(message: types.Message):

    text = (
        "📚 <b>KURS HAQIDA</b>\n\n"
        "🎓 <b>To'liq Bank Sistema</b>\n\n"
        "📖 Kursda 31 ta mavzu mavjud.\n\n"
        "💵 <b>Narxi: $500</b>\n\n"
        "Kursga ulanish uchun administrator bilan bog'laning:\n\n"
        "👤 @laa_admin"
    )

    await message.answer(
        text,
        parse_mode="HTML"
    )


# =========================================================
# ADMIN BILAN BOG'LANISH
# =========================================================

@dp.message(F.text == "👤 Admin bilan bog'lanish")
async def admin_handler(message: types.Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💬 @laa_admin",
                    url="https://t.me/laa_admin"
                )
            ]
        ]
    )

    text = (
        "👤 <b>ADMIN BILAN BOG'LANISH</b>\n\n"
        "Kurs bo'yicha batafsil ma'lumot, to'lov va "
        "ulanish masalalari uchun administratorga yozing."
    )

    await message.answer(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================================================
# BOTNI ISHGA TUSHIRISH
# =========================================================

async def main():

    logging.basicConfig(level=logging.INFO)

    print("Bot ishga tushdi...")

    # Flask serverni faqat BIR MARTA ishga tushiramiz
    keep_alive()

    # Telegram polling faqat BIR MARTA
    await dp.start_polling(bot)


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    asyncio.run(main())
