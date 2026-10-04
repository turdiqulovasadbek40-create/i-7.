from flask import Flask
from threading import Thread
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# Bot tokeni
TOKEN = "8920455563:AAFiVQoxu_m7ZyZPunNsAAWJDfeZ5mtynuc"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Flask server (Render uxlab qolmasligi uchun) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()
# -----------------------------------------------------------------

# 31 ta mavzu ro'yxati
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
app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎓 Discord Live"), KeyboardButton(text="ℹ️️ Ma'lumot")],
            [KeyboardButton(text="📚 Kurs haqida ma'lumot olish"), KeyboardButton(text="👤 Admin bilan bog'lanish")]
        ],
        resize_keyboard=True
    )
    text = (
        "Assalomu alaykum! 👋\n\n"
        "🎓 <b>To'liq Bank Sistema</b> kursiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang."
    )
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)

@dp.message(F.text == "🎓 Discord Live")
async def discord_live_handler(message: types.Message):
    text = "🎓 <b>DISCORD LIVE</b>\n\n📚 <b>TO'LIQ BANK SISTEMA</b>\n\nKursda quyidagi mavzular mavjud:\n\n"
    for i, topic in enumerate(topics, 1):
        text += f"{i}. {topic}\n"
    text += "\n\n📌 Kurs haqida batafsil ma'lumot olish uchun administrator bilan bog'laning."
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "ℹ️ Ma'lumot")
async def info_handler(message: types.Message):
    text = (
        "ℹ️ <b>MA'LUMOT</b>\n\n"
        "🎓 To'liq Bank Sistema — trading bo'yicha 31 ta mavzuni o'z ichiga olgan kurs.\n\n"
        "Kursga ulanish va batafsil ma'lumot uchun administrator bilan bog'laning."
    )
    await message.answer(text, parse_mode="HTML")

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
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "👤 Admin bilan bog'lanish")
async def admin_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 @laa_admin", url="https://t.me/laa_admin")]
        ]
    )
    text = (
        "👤 <b>ADMIN BILAN BOG'LANISH</b>\n\n"
        "Kurs bo'yicha batafsil ma'lumot, to'lov va ulanish masalalari uchun administratorga yozing."
    )
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    keep_alive()
    await dp.start_polling(bot)
if __name__ == '__main__':
    keep_alive()  # <-- Mana shu qatorni eng boshiga qo'shasiz
    
    # Bu yerda sizning oldingi botingizni yoqadigan kodingiz turadi 
    # (masalan: asyncio.run(main()) yoki executor.start_polling(...) va hokazo)

if __name__ == "__main__":
    asyncio.run(main())
