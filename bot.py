import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
from threading import Thread

# Bot tokeni
TOKEN = "8920455563:AAFiVQoxu_m7ZyZPunNsAAWJDfeZ5mtynuc"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Flask server (Render yoki boshqalar uxlab qolmasligi uchun) ---
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

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    welcome_text = (
        "🤖 **Market Manipulation Bot** 24/7 rejimida ishlayapti!\n\n"
        "Buyruqlar:\n"
        "/manipulation - 7 ta asosiy manipulyatsiya turlari"
    )
    await message.answer(welcome_text, parse_mode="Markdown")

@dp.message(Command("manipulation"))
async def manipulation_handler(message: types.Message):
    text = (
        "📊 **Bozor Manipulyatsiyasining 7 ta Asosiy Turi:**\n\n"
        "1. **AFU (Accumulation Fake-out):** Narxni yig'ish zonasidagi soxta chiqishlar.\n"
        "2. **SFU (Stop-Loss Hunting / Sweep):** Treiderlarning stop-loss'larini yig'ib ketish zonalari.\n"
        "3. **FU (Fake-out Zone):** Soxta buzilishlar sodir bo'ladigan darajalar.\n"
        "4. **Stop Hunting:** Katta o'yinchilar tomonidan likvidlikni tozalash.\n"
        "5. **Spoofing & Layering:** Orderbook'ga soxta yirik orderlar tashlab narxni chalg'itish.\n"
        "6. **Wash Trading:** Sun'iy savdo hajmini hosil qilish.\n"
        "7. **Pump & Dump:** Sun'iy ravishda narxni osmonga ko'tarib, keyin keskin sotib yuborish."
    )
    await message.answer(text, parse_mode="Markdown")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    # Veb serverni alohida oqimda (thread) ishga tushiramiz
    keep_alive()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
