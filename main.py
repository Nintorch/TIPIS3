from threading import Thread
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


def wait_for_input():
    while True:
        text = input("Введите текст уведомления: ")
        for user in users:
            bot.send_message(user, "Уведомление: " + text, parse_mode="html")


print("Bot is starting")
Thread(target=wait_for_input).start()
bot.polling(none_stop=True, interval=0)
