def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.InlineKeyboardButton("Связаться с салоном")
    item2=types.InlineKeyboardButton("О нас")
    item3=types.InlineKeyboardButton("Записаться")
    item4=types.InlineKeyboardButton("Оставить отзыв")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(m.chat.id, '\nПривет путник', reply_markup=markup)

def call_us(message):
    phone_number = 'Рады звонку в любое время \n8 800 555 35 35'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("Домой")
    markup.add(item1)
    bot.send_message(message.chat.id, f'\n{phone_number}', reply_markup=markup)
