import telebot

with open("token.txt") as file:
    bot = telebot.TeleBot(file.read())


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Ожидайте уведомлений")


print("Bot is starting")
bot.polling(none_stop=True, interval=0)
