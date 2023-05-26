import os
import sqlite3

import datetime
from datetime import date
import sys
import logging
import time
import json
import signal

import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda x: x.text == 'Домой')
@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 6
    item1=types.InlineKeyboardButton('Связаться с салоном')
    item2=types.InlineKeyboardButton('О нас')
    item3=types.InlineKeyboardButton('Записаться')
    item4=types.InlineKeyboardButton('Оставить отзыв')
    markup.add(item1, item2, item3, item4)
    bot.send_message(m.chat.id, '\nПривет путник', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Связаться с салоном':
        phone_number = 'Рады звонку в любое время \n8 800 555 35 35'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Домой")
        markup.add(item1)
        bot.send_message(message.chat.id, f'\n{phone_number}', reply_markup=markup)

    elif message.text == 'О нас':
        text = '[примеры работ](https://salonvb.ru/portfolio)'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Связаться с салоном')
        item2 = types.KeyboardButton("Домой")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, f'\nМы супер студия, ниже можно посмотреть {text}', parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Записаться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Маникюр')
        item2 = types.KeyboardButton('Мейкап')
        item3 = types.KeyboardButton('Покраска волос')
        item4 = types.KeyboardButton('Выбрать мастера')
        item5 = types.KeyboardButton("Назад")
        item6 = types.KeyboardButton("Домой")
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(message.chat.id, '\nПора определиться с услугой', reply_markup=markup)

    #elif message.text == 'Оставить отзыв': #!!!!!!!!!!!!

    elif message.text == 'Маникюр':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Выбрать дату')
        item2 = types.KeyboardButton("Назад")
        item3 = types.KeyboardButton("Домой")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '\nСтоимость маникюра - 5000', reply_markup=markup)

    elif message.text == 'Мейкап':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Выбрать дату')
        item2 = types.KeyboardButton("Назад")
        item3 = types.KeyboardButton("Домой")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '\nСтоимость макияжа - 4000', reply_markup=markup)

    elif message.text == 'Покраска волос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Выбрать дату')
        item2 = types.KeyboardButton("Назад")
        item3 = types.KeyboardButton("Домой")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '\nСтоимость покраски - 10000', reply_markup=markup)

    elif message.text == 'Выбрать дату':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('сегодня')
        item2 = types.KeyboardButton("Назад")
        item3 = types.KeyboardButton("Домой")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '\nСтоимость макияжа - 4000', reply_markup=markup)
    # как выбрать

def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
            time.sleep(5)


if __name__ == '__main__':
    main()
