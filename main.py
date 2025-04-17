import os
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Йоу, дропай свой рилс 🎥✨ — ща замутим красоту"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()
    if "instagram.com/reel/" in text:
        modified_link = text.replace("www.instagram.com", "ddinstagram.com").replace("instagram.com", "ddinstagram.com").split("?")[0]
        bot.send_message(
            message.chat.id,
            f"👉 Апгрейд подъехал 🚀👇"
        )
    else:
        bot.send_message(
            message.chat.id,
            "👉 Давай по новой, миша! 🤨 🔄"
        )

print("🤖 Погнали!!!")
bot.infinity_polling()
