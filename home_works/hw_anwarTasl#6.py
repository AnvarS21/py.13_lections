# Задача 1. 

# У вас есть словарь игроковint(num1)
#     int(num2), которые участвовали в трёх видах спорта. В словаре хранятся пары «Ф. И. — очки»:
# b = []
# players = {
#     ("Will", "Smith"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }
# for k, v in players.items():
#     b.append(k+v)
# print(b)

# Задача 2

# Есть список из 10 случайных чисел. Напишите программу, которая делит эти числа на пары кортежей внутри списка, и выведите результат на экран.

# метод 1
a = [0, 1, 9, 3, 4, 5, 6, 7, 8, 9]
b = []
for i in range(0, len(a) - 1, 2):
    c = (a[i], a[i + 1])
    b.append(c)
print(b)








# Задача 3

#  Посчитайте, сколько раз символ "O"и "А" встречается в строке.   
# a = "ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"
# a = list(a)

# print(f'Символ "А" встречается {a.count("А")} раз')
# print(f'Символ "О" встречается {a.count("О")} раз')



# Задача 4 

# Переделайте прошлый калькулятор
# Сделайте так, чтобы калькулятор спрашивал постоянно данные для совершения операций в калькулятор
# Если пользователь вводит букву q то калькулятор должен завершаться (для хардкора, если пользователь введет пустую строку, вывести строку "Нет ничего приятнее, чем знание о твоих знаниях!

# while True:
#     num1, num2, oper = int(input('Введите первое число :')), int(input('Введите первое число :')), input('Выберите операцию (+, -, /, *), а для закрытия напишите \'q\'')

#     if oper == '+':   
#         print(num1 + num2)
#     elif oper == '-':
#         print(num1 - num2)
#     elif oper == '/':    
#         if num1 == 0 or num2 == 0:
#             raise Exception('На ноль делить нельзя!')
#             break
#         else:
#             print(num1 / num2)
#     elif oper == '*':
#         print(num1 * num2)
#     elif oper == 'q' or oper == 'Q':
#         break
#     elif oper == '':
#         print('Нет ничего приятнее, чем знание о твоих знаниях!')
#         break
#     else:
#         print('Операция неизвестна')



# Задача 5

# violator_songs = {
#     'World in My Eyes': 4.86,

#     'Sweetest Perfection': 4.43,

#     'Personal Jesus': 4.56,

#     'Halo': 4.9,

#     'Waiting for the Night': 6.07,

#     'Enjoy the Silence': 4.20,

#     'Policy of Truth': 4.76,

#     'Blue Dress': 4.29,

#     'Clean': 5.83

# }
# a = int(input('Сколько песен выбрать? '))
# count = 0
# for i in range(a):
#     b = input(f'Введите название {i + 1} песни:')
#     if b in violator_songs:
#         count += violator_songs[b]
#     else:
#         print('Этой песни нет в плеере!')
# print(f'Общее время звучания песен: {count} минут')



# #Задача 6
# n = int(input('Введите количество стран: '))
# a = {}
# b = []
# for i in range(n):
#     stran = input(f'{i + 1} страна: ').split()
#     b = stran[1:]
#     a[stran[0]] = b
    
#     print(a)
    
# city = input('город: ')
# s = 0
# for k, v in a.items():
#     if city in v:
#         print(f'город {city} расположен в стране {k}')
#         s += 1
# if s == 0:
#     print(f'по городу {city} данных нет!')
    


    