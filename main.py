import os
import telebot

# Вставь сюда свой токен
TOKEN = os.getenv("TOKEN") or "вставь_сюда_свой_токен_если_не_через_переменные"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Йоу, дропай свой рилс 🎥✨ — ща замутим красоту")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "instagram.com/reel/" in message.text:
        # Заменяем домен на ddinstagram и убираем лишнее
        modified_link = message.text.replace("instagram.com", "ddinstagram.com").split("?")[0]
        bot.send_message(message.chat.id, f"👉 Апгрейд подъехал 🚀👇\n{modified_link}")
    else:
        bot.send_message(message.chat.id, "👉 Давай по новой, миша! 🤨 🔄")

# Запуск бота
print("✅ Бот запущен!")
bot.infinity_polling()
