import telebot
from telebot import types
bot = telebot.TeleBot('6719285168:AAGh4M3RC2UaMg1Pnv-4xuAlohn-ii5HYvg')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Description")
    item2 = types.KeyboardButton("Photo")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

    if message.text == 'Description':
        bot.send_message(message.chat.id, 'ccsk')

        

bot.polling()


