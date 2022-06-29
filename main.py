import telebot
from telebot import types
from processor import *
bot = telebot.TeleBot('5300635034:AAGBwsRuOXCsC_kSpBTfl-zZW6RzV252JQw')


@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Hello, {message.from_user.first_name}! This is a simply dictionary with a small database.\nEnter a word below:'
    bot.send_message(message.chat.id, hello)


@bot.message_handler()
def get_user_text(message):
    m = wordSpelling(message.text)
    if m[0]:
        definition = getKey(m[1])
        bot.send_message(message.chat.id, definition)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(f'{m[1].capitalize()}')
        btn2 = types.KeyboardButton('/start')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, f'Maybe you mean "{m[1]}" instead?', reply_markup=markup)


bot.polling(none_stop=True)
