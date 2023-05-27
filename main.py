import os
import sqlite3

import datetime
from datetime import date
import sys
import logging
import time
import json
import signal
from unittest.mock import call

import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(token)
name = ''
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower == 'записаться' or 'домой':
        markup=types.InlineKeyboardMarkup(row_width = 2)
        item1=types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
        item2=types.InlineKeyboardButton('О нас', callback_data='about_us')
        item3=types.InlineKeyboardButton('Записаться', callback_data='sing_up')
        item4=types.InlineKeyboardButton('Оставить отзыв', callback_data='leave_review')
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, '\nвыбери нужный пункт', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'call_us':
            phone_number = 'Рады звонку в любое время \n8 800 555 35 35'
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id, text=f'\n{phone_number} \n\n введи "домой" для возврата в меню',
                                  reply_markup=markup)

        elif call.data == 'about_us':
            text = '[примеры работ](https://salonvb.ru/portfolio)'
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            markup.add(item1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'\nМы супер студия, ниже можно посмотреть {text} \n\n введи "домой" для возврата в меню',
                                  parse_mode='Markdown', reply_markup=markup)

        elif call.data == 'sing_up':
            markup = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton('Маникюр', callback_data='manicure')
            item2 = types.InlineKeyboardButton('Мейкап', callback_data='makeup')
            item3 = types.InlineKeyboardButton('Покраска волос', callback_data='coloring')
            item4 = types.InlineKeyboardButton('Выбрать мастера', callback_data='choose_master')
            item5 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            markup.add(item1, item2, item3, item4, item5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='\nПора определиться с услугой \n\n введи "домой" для возврата в меню',
                                  reply_markup=markup)

        elif call.data == 'choose_service':
            markup = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton('Маникюр', callback_data='manicure')
            item2 = types.InlineKeyboardButton('Мейкап', callback_data='makeup')
            item3 = types.InlineKeyboardButton('Покраска волос', callback_data='coloring')
            item4 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item5 = types.InlineKeyboardButton('Назад', callback_data='choose_master')
            markup.add(item1, item2, item3, item4, item5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='\nПора определиться с услугой \n\n введи "домой" для возврата в меню',
                                  reply_markup=markup)
    #elif message.text == 'Оставить отзыв': #!!!!!!!!!!!!

        elif call.data == 'manicure':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Выбрать дату', callback_data='choose_date')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton('Назад', callback_data='sing_up')
            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nСтоимость маникюра - 5000 \n\n введи "домой" для возврата в меню',
                             reply_markup=markup)

        elif call.data == 'makeup':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Выбрать дату', callback_data='choose_date')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton('Назад', callback_data='sing_up')
            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nСтоимость мейкапа - 4000 \n\n введи "домой" для возврата в меню',
                             reply_markup=markup)

        elif call.data == 'coloring':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Выбрать дату', callback_data='choose_date')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton('Назад', callback_data='sing_up')
            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,
                             text='\nСтоимость покраски волос - 10000 \n\n введи "домой" для возврата в меню',
                             reply_markup=markup)

        elif call.data == 'choose_date':
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = types.InlineKeyboardButton('1', callback_data='choose_master')
            item2 = types.InlineKeyboardButton('2', callback_data='choose_master')
            item3 = types.InlineKeyboardButton('3', callback_data='choose_master')
            item4 = types.InlineKeyboardButton('4', callback_data='choose_master')
            item5 = types.InlineKeyboardButton('5', callback_data='choose_master')
            item6 = types.InlineKeyboardButton('6', callback_data='choose_master')
            item7 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item8 = types.InlineKeyboardButton("Назад", callback_data='sing_up')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери дату \n\n введи "домой" для возврата в меню', reply_markup=markup)

        elif call.data == 'choose_master':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Ольга', callback_data='Ольга')
            item2 = types.InlineKeyboardButton('Татьяна', callback_data='Татьяна')
            item3 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item4 = types.InlineKeyboardButton("Назад", callback_data='choose_date')
            markup.add(item1, item2, item3, item4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери мастера \n\n введи "домой" для возврата в меню', reply_markup=markup)

        elif call.data == 'Татьяна':
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = types.InlineKeyboardButton('09:00', callback_data='entry')
            item2 = types.InlineKeyboardButton('09:30', callback_data='entry')
            item3 = types.InlineKeyboardButton('10:00', callback_data='entry')
            item4 = types.InlineKeyboardButton('10:30', callback_data='entry')
            item5 = types.InlineKeyboardButton('11:00', callback_data='entry')
            item6 = types.InlineKeyboardButton('11:30', callback_data='entry')
            item7 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item8 = types.InlineKeyboardButton("Назад", callback_data='choose_master')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери время \n\n введи "домой" для возврата в меню', reply_markup=markup)

        elif call.data == 'Ольга':
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = types.InlineKeyboardButton('09:00', callback_data='entry')
            item2 = types.InlineKeyboardButton('09:30', callback_data='entry')
            item3 = types.InlineKeyboardButton('10:00', callback_data='entry')
            item4 = types.InlineKeyboardButton('10:30', callback_data='entry')
            item5 = types.InlineKeyboardButton('11:00', callback_data='entry')
            item6 = types.InlineKeyboardButton('11:30', callback_data='entry')
            item7 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item8 = types.InlineKeyboardButton("Назад", callback_data='choose_master')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери время \n\n введи "домой" для возврата в меню', reply_markup=markup)

    # проблема с возвратом от мастера

        elif call.data == 'entry':
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = types.InlineKeyboardButton('Продолжить', callback_data='save')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            markup.add(item1, item2)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='\nВведи имя и номер телефона \n\n введи "домой" для возврата в меню', reply_markup=markup)







def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
            time.sleep(5)


if __name__ == '__main__':
    main()
