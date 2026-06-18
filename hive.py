import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found. Set it as an environment variable.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🐝 Hello! I'm Hive. Tag me in any group or DM me questions!")

@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.reply_to(message, f"📢 Your question: {message.text}\n\nI'm learning Web3. Full answers coming soon!")

from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home()
    return "Hive is running"

def run_flask():
   app.run(host='0.0.0.0', port=8080)  

threading.Thread(target=run_flask, daemon=True).start()

print("✅ Hive is running...")
bot.infinity_polling()
