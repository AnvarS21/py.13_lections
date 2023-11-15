from bs4 import BeautifulSoup
import requests
import lxml
import csv


    








news_desc = []
news_photos = []


import telebot
from telebot import types
bot = telebot.TeleBot('6719285168:AAGh4M3RC2UaMg1Pnv-4xuAlohn-ii5HYvg')


@bot.message_handler(commands=['start'])
def start_message(message):
    global news_desc, news_photos
    news_desc = []
    news_photos = []

    bot.send_message(message.chat.id, "Салам алейкум")
    bot.send_message(message.chat.id, "Подожди чутька, я обрабатываю сайт!)") 

    url = 'https://kaktus.media/?lable=8&date=2023-10-24&order=time'
    news_url = []

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    container = soup.find('div', class_='Tag--articles')
    news = container.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
    for new in news:
        news_url.append(new.find('a').get('href'))
        
        if len(news_url) == 20:
            break

    
    news_title = []

    count = 1
    p = []
    d = []
    for url in news_url:
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        desc = soup.find('div', class_='BbCode').find_all('p')
        title = soup.find('h1', class_='Article--title').text.strip()
        news_title.append(f'{count} ---> ' + title)
        count += 1

        for i in desc:
            i = i.text
            d.append(i)
        news_desc.append(''.join(d))
        d = [] 
        photos = soup.find_all('div', class_='Gallery--multi-image')
        if photos:
            for u in photos:
                u = u.find('a').get('href')
                p.append(u)
            news_photos.append(p)
            p = []
                
        else:
            
            news_photos.append('Photo absent!')
    news_title = '\n'.join(news_title)

    

    bot.send_message(message.chat.id, f"{news_title}")
    bot.send_message(message.chat.id, "Какую новость хочешь почитать?")


        
# @bot.message_handler(content_types='text')
# def button_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("Description")
#     item2 = types.KeyboardButton("Photo")
#     markup.add(item1)
#     markup.add(item2)
#     bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

c = ' '

     


@bot.message_handler()
def info(message):
    global c
    a = ['1', '2', '3', "4", '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    
    if message.text.strip() in a:
        c = int(message.text.strip()) 
        bot.send_message(message.chat.id, "sometitle news you can see Description of this news and Photo")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Description")
    item2 = types.KeyboardButton("Photo")
    item3 = types.KeyboardButton("Quit")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)

    bot.send_message(message.chat.id, '', reply_markup=markup)
    if message.text == 'Description':
        bot.send_message(message.chat.id, f"{news_desc[c-1]}")
    elif message.text == 'Photo':
        bot.send_message(message.chat.id, f"{news_photos[c-1]}")
    elif message.text == 'Quit':
        
        return 'Пока!'




bot.polling()
