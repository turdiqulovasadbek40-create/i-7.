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
    InlineKeyboardButton,
)

TOKEN = "8920455563:AAFiVQoxu_m7ZyZPunNsAAWJDfeZ5mtynuc"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ---------- Render / UptimeRobot uchun veb-server ----------
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot ishlayapti!"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)


def keep_alive():
    Thread(target=run_web, daemon=True).start()


# ---------- 31 ta mavzu ----------
topics = [
    "Cendlar", "AFU, SFU, FU, SELF FU, Inside FU", "Negationlar",
    "X2 va X3 Negation", "First, Third", "Likvidlik", "Major Minor Doji",
    "Doji", "LAL", "Imbalans", "Inside FU", "Self FU", "HCS modeli",
    "HCS X1, X2, X3", "HCS Negation", "HCS + Negation modeli",
    "True Stop Loss", "True Stop Loss bilan ishlash", "Time Frame Stretch",
    "TFS Established, Fresh, Closed", "Self Negation", "Entry modellari",
    "Special Candle", "0.1 Apart", "LAOL Negation", "X3 Negation",
    "X2 Manipulation", "X3 Manipulation", "X2 Negation", "True HCS",
    "Yo'nalish topish",
]


def topics_text():
    return "".join(f"{i}. {t}\n" for i, t in enumerate(topics, 1))


# ---------- /start ----------
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎓 Discord Live"),
             KeyboardButton(text="ℹ️ Ma'lumot")],
            [KeyboardButton(text="📚 Kurs haqida ma'lumot olish"),
             KeyboardButton(text="👤 Admin bilan bog'lanish")],
        ],
        resize_keyboard=True,
    )
    await message.answer(
        "Assalomu alaykum! 👋\n\n"
        "🎓 <b>To'liq Bank Sistema</b> kursiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang.",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


# ---------- Discord Live ----------
@dp.message(F.text == "🎓 Discord Live")
async def discord_live_handler(message: types.Message):
    text = (
        "🎓 <b>DISCORD LIVE</b>\n\n"
        "📚 <b>TO'LIQ BANK SISTEMA</b>\n\n"
        "Kursda quyidagi mavzular mavjud:\n\n"
        + topics_text()
        + "\n📌 Batafsil ma'lumot uchun administrator bilan bog'laning."
    )
    await message.answer(text, parse_mode="HTML")


# ---------- Ma'lumot ----------
@dp.message(F.text == "ℹ️ Ma'lumot")
async def info_handler(message: types.Message):
    await message.answer(
        "ℹ️ <b>MA'LUMOT</b>\n\n"
        "🎓 To'liq Bank Sistema — trading bo'yicha 31 ta mavzuni "
        "o'z ichiga olgan kurs.\n\n"
        "Kursga ulanish va batafsil ma'lumot uchun "
        "administrator bilan bog'laning.",
        parse_mode="HTML",
    )


# ---------- Kurs haqida ----------
@dp.message(F.text == "📚 Kurs haqida ma'lumot olish")
async def course_info_handler(message: types.Message):
    text = (
        "📚 <b>KURS HAQIDA</b>\n\n"
        "🎓 <b>To'liq Bank Sistema</b>\n\n"
        "📖 Kursda 31 ta mavzu mavjud:\n\n"
        + topics_text()
        + "\n💵 <b>Narxi: $500
