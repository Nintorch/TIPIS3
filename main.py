import telebot

with open("token.txt") as file:
    bot = telebot.TeleBot(file.read())
users = set()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Ожидайте уведомлений")
        users.add(message.from_user.id)
    elif message.text == "/stop":
        bot.send_message(message.from_user.id, "Больше не ожидайте уведомлений :)")
        users.remove(message.from_user.id)

print("Bot is starting")
bot.polling(none_stop=True, interval=0)
