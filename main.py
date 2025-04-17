import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Вставь ссылку на Instagram Reels.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "instagram.com/reel/" in message.text:
        modified_link = message.text.split("?")[0] + "?__a=1"
        bot.send_message(message.chat.id, f"Вот твоя ссылка:\n{modified_link}")
    else:
        bot.send_message(message.chat.id, "Это не похоже на ссылку Reels.")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv("WEBHOOK_URL") + "/" + TOKEN)
    return "Webhook set!", 200
