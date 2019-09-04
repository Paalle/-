# -*- coding: utf-8 -*-
import telebot
token ="948807888:AAGo4zpbk6KIqudEgYHKt5C-CPngyP0wCOk"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=first_name))

if __name__ == '__main__':
     bot.polling(none_stop=True)


 
