# print('     Задание 1')
# print('Ответ 1го задания:')
# num = 27
# print(num)

# print('     Задание 2')
# print('Ответ 2го задания:')
# stroka = 'Hello, world!'
# print(stroka)

# print('     Задание 3')
# print('Ответ 3го задания:')
# a = 4
# b = 'Salam'
# print(b * a)

# print('     Задание 4')
# print('Ответ 4го задания:')
# a1 = 79
# a2 = 81
# print(a2 + a1)

# print('     Задание 5')
# print('Ответ 5го задания:')
# f = 81
# d = 9
# print(f / d)

# print('     Задание 6')
# print('Ответ 6го задания:')
# pol = 7
# otr = -34
# print(abs(pol), abs(otr))

# print('     Задание 7')
# print('Ответ 7го задания:')
# o = 4
# p = pow(o, 3)
# print(p)

# print('     Задание 8')
# print('Ответ 8го задания:')
# num1 = 32
# num2 = 4
# print(num1 % num2)

# print('     Задание 9')
# print('Ответ 9го задания:')
# import math
# number = 7
# number2 = pow(number, 2, 5)
# print(number2)

# print('     Задание 10')
# c1 = int(input('Введите первое число: '))
# c2 = int(input('Введите второе число: '))
# c3 = int(input('Введите третье число: '))
# print('Ответ 10го задания:')
# umn = c1 * c2 % c3
# print('Остаток от деления: ', umn)

# print('     Задание 11')
# d1 = int(input('Enter the first number'))
# d2 = int(input('Enter the second number'))
# print('Ответ 11го задания:')
# d3 = 5.6
# d4 = d1 % d2 * d3
# print(d4)

# print('     Задание 12')
# print('Ответ 12го задания:')
# des = 11
# print(pow(des, 2))
# print(pow(des, 3))
# print(pow(des, 0.5))

# print('     Задание 13')
# print('Ответ 13го задания:')
# k1 = 4
# k2 = 3
# sum_k = pow(k1, 2) + pow(k2, 2)
# dlina_G = pow(sum_k, 0.5)
# print('Длина гипотенузы :', dlina_G)

# print('     Задание 14')
# print('Ответ 14го задания:')
# radius = 7
# pi = math.pi
# print(pi * (radius ** 2))

# print('     Задание 15')
# print('Ответ 15го задания:')
# x1 = 4
# y1 = 5
# z1 = 6
# x1 = y1
# z1 = x1
# y1 = z1
# print(x1, y1, z1)



# num1, num2, operation = int(input('Введите число 1: ')), int(input('Введите число 2: ')), input('Введите операцию: ')
# if operation == '+':
#     print(num1 + num2)
# elif operation == '-':
#     print(num1 - num2)
# elif operation == '*':
#     print(num1 * num2)
# elif operation == '/':
#     print(num1 / num2)
# else:
#     print('Неизвестная операция')


# is_your_leap = int(input('Введите год:'))
# if is_your_leap % 4 == 0:
#     print('Год високосный')
# else:
#     print('Год не високосный')


# square = int(input('Введите сторону квадрата: '))
# perimetr = square * 4
# plosh = pow(square, 2)
# d = 2 * (square ** 2)
# diagonal = d ** 0.5
# print(diagonal)

# season = int(input('Введите номер месяца'))
# z = [12, 1, 2]
# v = [3, 4, 5]
# l = [6, 7, 8]
# o = [9, 10, 11]
# if season in z:
#     print('Зима')
# elif season in v:
#     print('Весна')
# elif season in l:
#     print('Лето')
# elif season in o:
#     print('Осень')
# else:
#     print('Ошибка')

# a = int(input('Размер вклада: '))
# years = int(input('На сколько лет?'))
# bank = 0
# p = 0
# for i in range(years):
#     p = a / 10
#     a = p + a
#     bank += a
# print(a)


# is_prime = int(input('Введите число от 0 до 1000: '))
# if is_prime % 2 != 0 and is_prime % 3 != 0:
#     print('Число простое')
# else:
#     print('число не простое')

#2
# day, hour, sec = int(input('Введите дни: ')), int(input('Введите часы: ')), int(input('Введите секунды: '))
# print((day * 86400) + (hour * 3600) + sec, 'Секунд в общем')
# #1
# import time
# print(time.asctime())
# #3
# fut = int(input('Введите расстояние в футах: '))
# d = fut * 12
# ya = fut / 3
# m = fut / 5280
# print('В одном футе', d, 'дюймов,', ya, 'ярдов,', m, 'миль.')

# day, month, year = int(input('введите день: ')), int(input('введите месяц: ')), int(input('введите год: '))
# if 0 < day < 32 and 0 < month < 13 and 0 < year < 2024:
#     print(True)
# else:
#     print(False) 


# s = 'python'
# s = s[:3] + 't' + s[4:]
# print(s)

# s = 'My name is Anvar'
# s = s.replace(' ', 'p')
# print(s)

# subst = 'Привет меня зовут питон'
# st = 'х'
# if st in subst:
#     print('Есть контакт!')
# else:
#     print('Мимо!')

# letter = 's'
# st = 'Hello my name is Anvar'

# a = [2, 168]
# b = [[10, 15], [50, 78], [20, 32], [17, 29],]


# a = [2, 168]
# b = [[10, 15], [50, 78], [20, 32], [17, 29]]
# for i in range(a[0], a[1] + 1):
#     a.append(i)
# for u in range(b[0][0], b[0][1] + 1):
#     if u in a:
#         a.remove(u)
# for e in range(b[1][0], b[1][1] + 1):
#     if e in a:
#         a.remove(e)
# for s in range(b[2][0], b[2][1] + 1):
#     if s in a:
#         a.remove(s)
# for d in range(b[3][0], b[3][1] + 1):
#     if d in a:
#         a.remove(d)
# a = set(a)
# print(len(a))


# a = [2, 168]
# b = [[10, 15], [50, 78], [20, 32], [17, 29]]
# c = 0
# for i in range(a[0], a[1] + 1):
#     a.append(i)
# del a[b[0][0]:b[0][1] + 1]
# del a[b[1][0]:b[1][1] + 1]
# del a[b[2][0]:b[2][1] + 1]
# del a[b[3][0]:b[3][1] + 1]
# print(a)

# a = [2, 168]
# b = [[10, 15], [50, 78], [20, 32], [17, 29]]
# for i in range(a[0], a[1] + 1):
#     a.append(i)
# a1 = a[:b[0][0]], a[b[0][1] + 1:b[-1][0]], a[b[2][1] + 1:b[1][0]], a[b[1][1] + 1:a[1]]
# a1 = list(a1)

# print(a1)


# print("\t\tДобро пожаловать в игру 'Виселица'!")
# print( """ Сейчас я загадаю слово, а вы должны будете 
# по буквам его угадать. Вы будете предлагать по одной букве, если
#  эта буква есть в моем слове, то я открою вам ее положение в слове. 
# Если же нет, то я буду дорисовывать человечка на виселица. 
# Игра будет длиться до тех пор, пока вы не отгадаете слово, либо пока человечек не полностью повешен. 
# Итак, осталось, только пожелать вам удачи, ведь от вас зависит судьба, несчастного рисованного человечка! """ )

# 1) Получить слово от пользователя
# 2) Запустить цикл с равную длине слова
# word = input('Enter word: ')
# word = list(word)
# b = len(word) * '*'
# b = list(b)
# s = 0
# f = None
# while s < 1:
#     a = input('Enter letter: ')
#     if a in word:
#         b[word.index(a)] = a
        
        

    
#  word = input('Введите слово')
# word = []
# w = []
# e = []
# s = len(word) * '*'
# p = 0
# while p <= 1:
#     a = inwordword[word.index(a):]
#         e = word[:word.index(a)]
#         if a in w:
#             s[word.index(a)] = a
#         elif a in e:
#             s[word.index(a)] = a
#     print(s)








