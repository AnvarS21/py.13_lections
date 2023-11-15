# list_a = [1, 2, 39, 5, -6, 7, 8.1, 9, 10, -43, -134, 3.14, 2.55, 'Lenovo', 'Acer', 'Asus']

# list_b  = [123, -1.85, 43, -4.4, 8.16, - 5, 3.26, 21, 22, -43.97, 'Dell', 'HP', 'Lenovo', 'Acer' ]

# for u in list_b:        #Объединяем списки
#     list_a.append(u)

# list_cel = []      # Создаем списки с различными типами
# list_necel = []
# list_nout = []

# for i in list_a:                #Цикл для сортировки по спискам
#     if type(i) == int:
#         if i > 4:
#             list_cel.append(i)
#     elif type(i) == float:
#         list_necel.append(i)
#     elif type(i) == str:
#         list_nout.append(i)

# print(f'''Список целых, которые больше 4х: {list_cel}

# Список чисел с плавающей точкой: {list_necel}

# Список с наименованием ноутбуков: {list_nout}''')

# # Вставляем в середину списка любое значение.  
# list_cel.insert(len(list_cel) // 2, 'Hello, my name id John Snow')
# list_necel.insert(len(list_necel) // 2, 'Hello, my name id John Snow')


# print(f'''Резултат вставки в середину списка: {list_cel} \n и второй список: {list_necel}''')

# # Находим сумму элементов в списках
# sum_cel = 0
# for x in list_cel:
#     if type(x) == int:
#         sum_cel += x
# sum_necel = 0
# for o in list_necel:
#     if type(o) == float:
#         sum_necel += o

# print(f'Сумма элементов в 1 списке: {sum_cel} \nСумма элементов вo 2 списке: {sum_necel} \n\nКоличество элементов в списке 1: {len(list_cel)} \nА количество элементов во втором списке: {len(list_necel)}')        

# # удаляем одинаковые элементы в списке ноутбуков
# for y in list_nout:
#     if list_nout.count(y) > 1:
#         list_nout.remove(y)

# print(list_nout)

# list_nout.insert(0, 'Apple')
# list_nout.append('MSI')

# print(f'сначала удалили повторяющиеся названия потом добавили новые {list_nout}')



# 2_______________________________________________________
# print('Имя должно содержать цифры, пароль состоять из цифр и я email оканчиваться на ".kg"')
# name, email, password = input('Enter name: '), input('Enter email: '), input('Enter password: ')

# if name.isalpha() == False and password.isdigit() and email[-3:] == '.kg':
#     print('При вводе соблюдены все правила!')
#     print(f'{name}, вы успешно зарегистрировались \nинформация отправлена на {email}')
# else:
#     print('Ошибка при вводе')

# 1)Форматирование с помощью %
# name = 'Anvar'
# surname = 'Shamsutdinov'
# print('Добро пожаловать, %s %s!' %(name, surname))

# # 2) с помощью format()
# name = 'Anvar'
# surname = 'Shamsutdinov'
# print('Добро пожаловать, {} {}'.format(name, surname))

# # 3) c помощью f- строки
# name = 'Anvar'
# surname = 'Shamsutdinov'
# print(f'Добро пожаловать, {name} {surname}!')

# 4) 
# list_ = ['Телеграмм', 'Ватсап', 'Ютуб', 'Инстаграмм']
# list_ = '! '.join(list_)
# print(list_)

# from string import Template

# # 5
# info = "Hello, {name}. Welcome to our family!".format(name = input('введите свое имя :'))
# print(info)

# Мне понравилось форматировать с помощью f-строк, это удобно и очень быстро!. Так же очень удобно пользоваться join() для преоьразования списка в строку



# 3________________________________________________________________________

# a = input('Введите слово: ')
# a = a.lower()
# unic = 0
# for i in a:
#     if a.count(i) == 1:
#         unic += 1
# print('Количество уникальных букв:', unic)

# 4___________________________________________________________________________________

# import math

# radius = int(input('Введите радиус: '))
# okruzh = math.pi * 2 * radius
# if radius >= 10:
#     print('Длина окружности ', math.ceil(okruzh))

