import os
import telebot
import time

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Йоу, дропай свой рилс 🎥✨ — ща замутим красоту")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "instagram.com/reel/" in message.text:
        modified_link = message.text.split("?")[0] + "?__a=1"
        bot.send_message(message.chat.id, f"👉 Апгрейд подъехал 🚀👇\n{modified_link}")
    else:
        bot.send_message(message.chat.id, "👉 Давай по новой, миша! 🤨 🔄")

print("Bot started...")
while True:
    try:
        bot.polling(non_stop=True, timeout=30)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
