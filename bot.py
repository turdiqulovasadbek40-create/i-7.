import os
import threading
from aiohttp import web
import telebot
from telebot import types

# 1. Bot tokeni to'g'ridan-to'g'ri kiritildi
BOT_TOKEN = "8920455563:AAFiVQoxu_m7ZyZPunNsAAWJDfeZ5mtynuc"
PORT = int(os.environ.get("PORT", 10000))

bot = telebot.TeleBot(BOT_TOKEN)

# 2. Список из 31 темы
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

# 3. Хэндлеры бота
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎓 Discord Live", "ℹ️ Ma'lumot")
    keyboard.row("📚 Kurs haqida ma'lumot olish", "👤 Admin bilan bog'lanish")
    
    text = (
        "Assalomu alaykum! 👋\n\n"
        "🎓 <b>To'liq Bank Sistema</b> kursiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang."
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "🎓 Discord Live")
def discord_live(message):
    text = "🎓 <b>DISCORD LIVE</b>\n\n"
    text += "📚 <b>TO'LIQ BANK SISTEMA</b>\n\n"
    text += "Kursda quyidagi mavzular mavjud:\n\n"
    
    for i, topic in enumerate(topics, 1):
        text += f"{i}. {topic}\n"
        
    text += "\n\n📌 Kurs haqida batafsil ma'lumot olish uchun administrator bilan bog'laning."
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "ℹ️ Ma'lumot")
def information(message):
    text = (
        "ℹ️️ <b>MA'LUMOT</b>\n\n"
        "🎓 To'liq Bank Sistema — trading bo'yicha 31 ta mavzuni o'z ichiga olgan kurs.\n\n"
        "Kursga ulanish va batafsil ma'lumot uchun administrator bilan bog'laning."
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "📚 Kurs haqida ma'lumot olish")
def course_info(message):
    text = (
        "📚 <b>KURS HAQIDA</b>\n\n"
        "🎓 <b>To'liq Bank Sistema</b>\n\n"
        "📖 Kursda 31 ta mavzu mavjud.\n\n"
        "💵 <b>Narxi: $500</b>\n\n"
        "Kursga ulanish uchun administrator bilan bog'laning:\n\n"
        "👤 @laa_admin"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "👤 Admin bilan bog'lanish")
def admin(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("💬 @laa_admin", url="https://t.me/laa_admin"))
    
    text = (
        "👤 <b>ADMIN BILAN BOG'LANISH</b>\n\n"
        "Kurs bo'yicha batafsil ma'lumot, to'lov va ulanish masalalari uchun administratorga yozing."
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=keyboard)

# 4. Настройка веб-сервера aiohttp для UptimeRobot
async def handle_ping(request):
    return web.Response(text="Bot is running!")

def run_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    web.run_app(app, host="0.0.0.0", port=PORT)

# 5. Запуск сервера и бота
if __name__ == "__main__":
    # Запуск веб-сервера в отдельном потоке
    server_thread = threading.Thread(target=run_web_server, daemon=True)
    server_thread.start()

    print("✅ Web server и Bot успешно запущены...")
    bot.infinity_polling(skip_pending=True)
