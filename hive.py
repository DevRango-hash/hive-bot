import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found. Set it as an environment variable.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🐝 Hello! I'm Hive. Tag me in any group or DM me questions!")

@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.reply_to(message, f"📢 Your question: {message.text}\n\nI'm learning Web3. Full answers coming soon!")

print("✅ Hive is running...")
bot.infinity_polling()