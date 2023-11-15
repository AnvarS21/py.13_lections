""" # 1.
# Вам дан список со словарями, сериализуйте этот список в json-строку
 """
# import json


# ls = [
#     {'name': 'John', 'rating': 1,},
#     {'name': 'Jamie', 'rating': 5},
#     {'name': 'Lesha', 'rating': 2,},
#     {'name': 'Alesha', 'rating': 9}
# ]


# with open('data-test.json', 'w') as file:
#     json.dump(ls, file, indent=4)



""" # 2.
# Вам дана json-строка, десериализуйте ее. 
# Выведите названия тех продуктов, рейтинг которых больше 4
 """
# import json 

# with open('data-test.json', 'r') as f:
#     data = json.load(f)

# print(data)
# print()
# ls_rating = [i for i in data if i['rating'] > 4] # list comprehension
# print(ls_rating)

# for i in data: # loop
#     if i['rating'] > 4:
#         print(i['name'])

""" # 3.
# Вам дан файл db.json. Десериализуйте данные с него. 
# Добавьте в каждый продукт новую пару ("description":"..."). 
# Запишите измененные данные в файл new_db.json
 """
# import json

# with open('db.json', 'r') as file:
#     data = json.load(file)

# for i in data:
#     i['description'] = '...'
# print(data)

# with open('new_db.json', 'w') as file:
#     json.dump(data, file, indent=4)

""" # 4.
# Удалите из файла new-db.json продукт с id 3.
 """
# import json

# with open('new_db.json', 'r') as file:
#     data = json.load(file)
#     for i in data:
#         if i['id'] == 3:
#             data.remove(i)

# with open('new_db.json', 'w') as file:
#     json.dump(data, file, indent=4)

""" # 5.
# Напишите функцию, которая будет запрашивать id, title, description, price, rating и добавлять этот продукт в new_db.json
 """
# import json
# from bs4 import BeautifulSoup
# import requests
# url = 'https://auto312.kg/'
# def parsing_data():
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     container = soup.find('div', class_ = 'dj-items-rows')
#     cars = container.find_all('div', class_ = 'item_row')
#     result = []
#     c_id = 0
#     for i in cars:
#         c_id += 1
#         title = i.find('a', class_ = 'title').text
#         price = i.find('div', class_ = 'item_price').text
#         rating = i.find('div', class_ = 'item_display').text
#         desc = i.find('div', class_ = 'item_content_in').text.strip().replace('\n', '')
#         data = {'id': int(c_id), 'title': title, 'price': int(price[3:]), 'rating':int(rating), 'desc':(desc)}
#         result.append(data)
#     return result

# with open('car_db.json', 'w') as file:
#     json.dump(parsing_data(), file, indent=4)

# with open('car_db.json', 'r') as f:
#     data = json.load(f)

# def add_car(id, title, description, price, rating):
#     car = {'id': id, 'title': title, 'description': description, 'price': price, 'rating': rating}
#     data.append(car)
#     with open('new_car_db.json', 'w') as file:
#         json.dump(data, file, indent=4)
    
# add_car(11111, 'OSMON', 'TOP1MIRA', 'MNOGO', 10)









""" # 6.
# Напишите функцию, которая будет принимать id продукта
# если такого продукта нет в new_db.json, функция выводит ошибку
# если такой продукт есть, то запрашивается id, title, description, price, rating и продукт должен обновиться в new_db.json """
# with open('new_car_db.json', 'r') as f:
#     data = json.load(f)
    
# def id_(id):
#     for i in data:
#         if i['id'] == id:
#             return



""" # 7.
# Напишите функцию, которая будет вытаскивать все продукты из new_db.json и выводить отсортированный список с продуктами по рейтингу (в порядке убывания)
 """
# import json
# def sort_json():
#     with open('new_car_db.json', 'r') as file:
#         data = json.load(file)
#     data1 = sorted(data, key=(lambda x: x['rating']), reverse=True)
#     for i in data1:
#         print(i['rating'])

# sort_json()


# print(sort_json())


"""  8.
# Напишите функцию, которая принимает часть названия и выводит список из всех продуктов из new_db.json в названиях которых будет находится эта часть названия
 """
# import json
# def name(name):
#     with open('new_car_db.json', 'r') as file:
#         data = json.load(file)
#     for i in data:
#         if name in i['title']:
#             print(i)

# name('Mer')


""" # 9.
# Напишите функцию, которая принимает цену и выводит список из всех продуктов из new_db.json цена которых больше или равна заданной
 """
# import json
# def price(price):
#     with open('new_car_db.json', 'r') as file:
#         data = json.load(file)
#     for i in data:
#         if price <= i['price']:
#             print(i['title'])

# price(7000)


""" # 10.
# Напишите функцию, которая принимает список из продуктов
# эти продукты должны будут добавиться в new_db.json
# если продукт с таким же id уже есть в new_db.json, то он не добавляется """
# import json
# def ls_title(*args, **kwargs):
#     id_ = []
#     lats = []
#     for i in args:
#         if i['id'] not in id_:
#             id_.append(i['id'])
#             lats.append(i)
#         else:
#             continue
#     with open('test.json', 'w') as file:
#         json.dump(lats, file, indent=4)

# ls_title({'id': 2, 'name': 'Ascelator'}, {'id': 3, 'name': 'Bulbulyator'}, {'id': 2, 'name': 'Sindikator'})


"""Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}

удалите один из элементов, не используя методы словаря
"""



"""
#3
Объявите словарь

a = {'a': 1, 'b': 2, 'c': 1}

выведите всего его элементы специальным методом и распечатайте результат. 
Результат в терминале, должен быть такой:

dict_items([('a', 1), ('b', 2), ('c', 3)])
"""

# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.items())



#4
"""
Дан словарь. Распечатайте максимальное значение в словаре

a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

Вывод:
56
"""
# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(a.values()))


#5
"""
Дан словарь. Распечатайте минимальное значение в словаре

a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

Вывод:
21
"""
# a = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(min(a.values()))



#6
"""Создайте словарь a с числовыми значениями. 
Создайте новый словарь b, такой же как словарь а, 
но все нечетные значения замените на 1.

Пример: Ввод -> 
a = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
Вывод -> 
b = {'a': 1, 'b': 4, 'c': 1, 'd': 1,  'e': 6}
"""
# a = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# b = {k: v if v % 2 == 0 else 1 for k, v in a.items()}
# print(b)



#7
"""Дан словарь, оставьте все элементы с пустыми значениями, остальные удалите

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

Вывод:

{'a': None, 'd': None}
"""

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for k, v in a.items():
#     if v == None:
#         b[k] = v

# print(b)



#8
"""Дан словарь a, где ключами будут цены товаров, а значениями их названия, 
затем пройдитесь циклом по нему и поменяйте все ключи элементов, 
возведя их в квадрат, новые элементы запишите в словарь b

Ввод:
a = {25: 'apple', 26: 'orange', 27: 'banana'} 
b = {}


Вывод:
{625: 'apple', 676: 'orange', 729: 'banana'}
"""

# a = {25: 'apple', 26: 'orange', 27: 'banana'} 
# b = {k**2:v for k, v in a.items()}
# print(b)



#9
"""Дан список. Создайте словарь а, ключами которого будут строки из списка,
а значениями их длины

list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
a = {}

Вывод:
{'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
"""

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# a = {i: len(i) for i in list_}



#10
"""Из предыдущего словаря а, достаньте ключ, значение которого является 
максимальным

a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

Вывод:
'Bootcamp'
"""

# a = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# print(max(a, key=len))




'===============MEDIUM================'
#1
"""Дан словарь a, где ключи - числа от 1 до 5 и значения те же самые числа.
Создайте словарь b, у которого ключи такие же как в первом словаре, 
а значения эти же числа, возведенные в куб


a = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
b = {}

Вывод:
{'1': 1, '2': 8, '3': 27, '4': 64, '5': 125}
"""
# a = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
# b = {k: v**3 for k, v in a.items()}
# print(b)


#2
"""Дан словарь а, значениями, которого являются словари,
измените словарь 'а' таким образом, чтобы значения внутреннего словаря стали 
внешними значениями

a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

Вывод:
{'a': 32, 'b': 36, 'c': 37, 'd': 21}
"""
# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = {}
# for k, v in a.items():
#     for i in v.values():
#         b[k] = i
# print(b)

#3
"""Дан словарь dict1. Создайте словарь dict2, с ключами как в 
словаре dict1, а значениями пусть будут произведение чисел внутренних словарей 

dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}

Вывод:
{'a': 4, 'b': 8, 'c': 27}
"""
# import math
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k, v in dict1.items():
#     dict2[k] = math.prod(v.values()) 
# print(dict2) 


#4
"""Дан список, состоящий из строк и чисел. Создайте словарь, ключами которого
будут строки из списка, а значениями числа


list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
a = {}


Вывод:
{'hello': 23, 'world': 56, 'Makers': 928, 'word': 456, 'bootcamp': 223, 'coding': 89}
"""
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# word = [i for i in list_ if type(i) == str]
# num = [i for i in list_ if type(i) == int]
# a = {k: v for k, v in zip(word, num)}
# print(a)


#5
"""Дан словарь dict_. Отсортируйте словарь по значениям в порядке увеличения.
Новые элементы занесите в словарь sorted_dict

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
"""


# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = sorted(dict_.items())
# print(dict(sorted_dict))

#6
"""Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
Новые элементы занесите в словарь sorted_dict

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
"""
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(dict_.items(), reverse=True))
# print(sorted_dict)

#7
"""Дан словарь. С помощью переменной x проверьте есть ли такой ключ в словаре.
Если есть, напечатайте строку 'Key is present in the dictionary', если нет -
'Key is not present in the dictionary'

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# x = input()
# """
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# x = int(input())
# if  x in dict_:
#     print('Key is present in the dictionary')
# else:
#     print('Key is not present in the dictionary')



'==================HARD===================='
#1
"""Даны 3 словаря. Объедините эти словари в 4

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4 = {}

Вывод:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# dic4 = {**dic1, **dic2, **dic3}
# print(dic4)

#2
"""Даны два списка одинаковой длины. 
Необходимо создать из них словарь таким образом, 
чтобы элементы первого списка были ключами, 
а элементы второго — соответственно значениями нашего словаря


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
a = {}

Вывод:
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
"""

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# a = {k: v for k, v in zip(list1, list2)}
# print(a)

#3
"""Дан словарь. Найдите сумму значений словаря, который хранится под ключом 'vars',
используя значение словаря, под ключом 'math'

dict_ = {
    'math': {
        'sum': sum
    },
    'vars': {
        'a': 5,
        'b': 20,
        'c': 50
    }
}

Вывод: 
75
"""

# dict_ = {'math': {'sum': sum}, 'vars': {'a': 5, 'b': 20, 'c': 50}}
# print(dict_['math']['sum'](dict_['vars'].values()))