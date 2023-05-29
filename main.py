import os
import sqlite3

import datetime
from datetime import date
import time

import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(token)
conn = sqlite3.connect('beauty_salon/db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

params = []

def review(message):
    global name
    global phone
    name = message.text.split(' ')[0]
    phone = message.text.split(' ')[1]
    params.append(name)
    params.append(phone)

    return name, phone

def master1(message):
    global master
    master = 'Татьяне'
    return master

def master2(message):
    global master
    master = 'Ольге'
    return master
def choose_time(message):
    global time_in
    time_in = message.text.split('#')[-1]
    return time_in

def client_review(message):
    global comment
    comment = message.text
    return comment

def bd_table_val(id: int, name: str, master: str, service: str, price: int, visit_time: str):
    cursor.execute('INSERT INTO salon_salon(name, master, service, price, visit_time) VALUES (?,?,?,?,?)',
                   (params[-2], params[3], params[0], params[1], params[2]))
    conn.commit()

@bot.message_handler(content_types=['text'])
def start(message):

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
                                  message_id=call.message.id, text=f'\n{phone_number} \n\nдля возврата в меню отправь сообщение',
                                  reply_markup=markup)

        elif call.data == 'about_us':
            text = '[примеры работ](https://salonvb.ru/portfolio)'
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            markup.add(item1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'\nМы супер студия, ниже можно посмотреть {text} \n\nдля возврата в меню отправь сообщение',
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
                                  text='\nПора определиться с услугой \n\nдля возврата в меню отправь сообщение',
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
                                  text='\nПора определиться с услугой \n\nдля возврата в меню отправь сообщение',
                                  reply_markup=markup)


        elif call.data == 'manicure':
            params.append('маникюр')
            params.append(4000)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Выбрать дату', callback_data='choose_date')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton('Назад', callback_data='sing_up')
            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nСтоимость маникюра - 5000 \n\nдля возврата в меню отправь сообщение',
                             reply_markup=markup)


        elif call.data == 'makeup':
            params.append('мейкап')
            params.append(5000)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Выбрать дату', callback_data='choose_date')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton('Назад', callback_data='sing_up')
            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nСтоимость мейкапа - 4000 \n\nдля возврата в меню отправь сообщение',
                             reply_markup=markup)

        elif call.data == 'coloring':
            params.append('покраска')
            params.append(10000)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Выбрать дату', callback_data='choose_date')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton('Назад', callback_data='sing_up')
            markup.add(item1, item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,
                             text='\nСтоимость покраски волос - 10000 \n\nдля возврата в меню отправь сообщение',
                             reply_markup=markup)

        elif call.data == 'choose_date':
            all_dates = []
            current_date = date.today()
            new_day = current_date
            all_dates.append(current_date.strftime("%d.%m"))
            for i in range(1, 30):
                next_day = new_day + datetime.timedelta(days=1)
                new_day = next_day
                all_dates.append(next_day.strftime("%d.%m"))

            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = [types.InlineKeyboardButton(f'{date_sing}', callback_data=f'choose_master#{date_sing}') for date_sing in all_dates]
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item3 = types.InlineKeyboardButton("Назад", callback_data='sing_up')
            markup.add(*item1)
            markup.add(item2, item3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери дату \n\nдля возврата в меню отправь сообщение', reply_markup=markup)


        elif 'choose_master' in call.data:
            params.append(call.data.split('#')[-1])
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Ольга', callback_data='Ольга')
            item2 = types.InlineKeyboardButton('Татьяна', callback_data='Татьяна')
            item3 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item4 = types.InlineKeyboardButton("Назад", callback_data='choose_date')
            markup.add(item1, item2, item3, item4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери мастера \n\nдля возврата в меню отправь сообщение', reply_markup=markup)



        elif 'Татьяна' in call.data:
            params.append('Татьяна')
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = [types.InlineKeyboardButton(f'{hour+1}:00', callback_data=f'entry#{hour+1}:00') for hour in range(7, 11)]
            item2 = [types.InlineKeyboardButton(f'{hour+1}:30', callback_data=f'entry#{hour+1}:30') for hour in range(7, 11)]
            item3 = [types.InlineKeyboardButton(f'{hour+1}:00', callback_data=f'entry#{hour+1}:00') for hour in range(11, 15)]
            item4 = [types.InlineKeyboardButton(f'{hour+1}:30', callback_data=f'entry#{hour+1}:30') for hour in range(11, 15)]
            item5 = [types.InlineKeyboardButton(f'{hour+1}:00', callback_data=f'entry#{hour+1}:00') for hour in range(15, 18)]
            item6 = [types.InlineKeyboardButton(f'{hour+1}:30', callback_data=f'entry#{hour+1}:30') for hour in range(15, 18)]
            item7 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item8 = types.InlineKeyboardButton("Назад", callback_data='choose_master')
            markup.add(*item1)
            markup.add(*item2)
            markup.add(*item3)
            markup.add(*item4)
            markup.add(*item5)
            markup.add(*item6)
            markup.add(item7, item8)

            sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери время \n\nдля возврата в меню отправь сообщение', reply_markup=markup)
            bot.register_next_step_handler(sent, master1)


        elif 'Ольга' in call.data:
            params.append('Ольга')
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = [types.InlineKeyboardButton(f'{hour+1}:00', callback_data=f'entry#{hour+1}:00') for hour in range(7, 11)]
            item2 = [types.InlineKeyboardButton(f'{hour+1}:30', callback_data=f'entry#{hour+1}:30') for hour in range(7, 11)]
            item3 = [types.InlineKeyboardButton(f'{hour+1}:00', callback_data=f'entry#{hour+1}:00') for hour in range(11, 15)]
            item4 = [types.InlineKeyboardButton(f'{hour+1}:30', callback_data=f'entry#{hour+1}:30') for hour in range(11, 15)]
            item5 = [types.InlineKeyboardButton(f'{hour+1}:00', callback_data=f'entry#{hour+1}:00') for hour in range(15, 18)]
            item6 = [types.InlineKeyboardButton(f'{hour+1}:30', callback_data=f'entry#{hour+1}:30') for hour in range(15, 18)]
            item7 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            item8 = types.InlineKeyboardButton("Назад", callback_data='choose_master')
            markup.add(*item1)
            markup.add(*item2)
            markup.add(*item3)
            markup.add(*item4)
            markup.add(*item5)
            markup.add(*item6)
            markup.add(item7, item8)
            sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                             text='\nвыбери время \n\n для возврата в меню отправь сообщение', reply_markup=markup)
            bot.register_next_step_handler(sent, master2)



        elif 'entry' in call.data:
            params.append(call.data.split('#')[-1])
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = types.InlineKeyboardButton('Продолжить', callback_data='your_sing')
            item2 = types.InlineKeyboardButton('Связаться с салоном', callback_data='call_us')
            markup.add(item1, item2)

            sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='\nВведи имя и номер телефона \n\n нажимая продолжить, вы даете согласие на обработку персональных данных',
                                         reply_markup=markup)
            bot.register_next_step_handler(sent, review)

        elif 'your_sing' in call.data:
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Оплатить', callback_data='оплата')
            markup.add(item1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'\n{params[-2]}, вы записаны к {master}. '
                                                                                                 f'Ждем вас {params[2]} в {params[-3]} по адресу: улица красивых 23'
                                                                                                 f'\nВы записаны на услугу: "{params[0]}", стоимость: {params[1]}'
                                                                                                 f'\n\n если хотите оплатить сразу, нажмите "Оплатить"',
                                  reply_markup=markup)

            bd_table_val(id= 1, name= params[-2], master= params[3], service= params[0], price= params[1], visit_time= params[2])
            print(params)


        elif 'leave_review' in call.data:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Ольга', callback_data='мастер#1')
            item2 = types.InlineKeyboardButton('Татьяна', callback_data='мастер#2')
            markup.add(item1, item2)

            sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                         text='\nОтправьте имя и телефон \n\n затем выбирете мастера', reply_markup=markup)

            bot.register_next_step_handler(sent, review)


        elif 'мастер' in call.data:
            if call.data.split('#')[-1] == '1':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Оставить отзыв', callback_data='отзыв#1')
                markup.add(item1)
                sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                             text='\nнапишите отзыв', reply_markup=markup)
                bot.register_next_step_handler(sent, client_review)

            elif call.data.split('#')[-1] == '2':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Оставить отзыв', callback_data='отзыв#2')
                markup.add(item1)
                sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                             text='\nнапишите отзыв', reply_markup=markup)
                bot.register_next_step_handler(sent, client_review)

        elif 'отзыв' in call.data:
            markup = types.InlineKeyboardMarkup(row_width=1)
            bot.sendmessage(call.message.chat.id, '\nспасибо за ваш отзыв\n\n если хотите оплатить сразу, нажмите "Оплатить"',
                                  reply_markup=markup)
            if call.data.split('#')[-1] == '1':
                master_name = 'Ольга'
            elif call.data.split('#')[-1] == '2':
                master_name = 'Татьяна'

            print(f'имя {name}, мастер {master_name}, отзыв: {comment}')

        elif 'оплата' in call.data:
            bot.send_message(f'Хоть твой кошелек и похудел, зато ты будешь красивее!') #Добавить стоимость услуги








def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
            time.sleep(5)


if __name__ == '__main__':
    main()
