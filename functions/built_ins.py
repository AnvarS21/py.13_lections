# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возварщает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls1, ls2))
# print(res)


# _________________-----------------------------------------

# all(), any()

# all(iterable) - Возвращает True, если все элементы итерируемого объекта истина, иначе False

# ls = [[1, 2], 5, 'stroka', True, 1, None]
# print(all(ls))


# _____________________________________________________

# ip = '10.255.12.155' # True
# ip2 = '10.255.1y.155' # False

# result = all(x.isdigit() for x in ip2.split('.'))
# print(result)

# ______________________________________________________

# any - Возварщает True, если хотябы один элемент истина

# ls = [0, 0, 1, 0]
# print(any(ls))
# ________________________________________

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']

# command = input('Введите команду: ') # sudo get system
# if any(x in command for x in ignore):
#     raise Exception('You do not have permission!')
# print('OK!')

# _-------------------------------------------------------------,
# Анонимные функции - lamda(Такие же функции только без названия)

# lambda функции могут принимать сколько угодно аргументов, но всегда возвращают одно выражение

# def sum_of_args(a, b):
#     res = a + b
#     return res
# print(sum_of_args(3, 4))

# func = lambda *args: sum(args)
# print(func(5, 15, 34))


# def myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# print(myDoubler(50))
# print(myDoubler(123))
# print(myDoubler(7))
# print(myTripler(55))

# ______________________________________________________

# dict_ = {'Jonh': 50_000, 'Jamie': 100_000, 'Aibek': 1_000_000, 'Aigerim': 15}
# res = dict(sorted(dict_.items(), key=lambda x: x[1]))
# print(res)


# -________________________________________________________
# map(function, iterable) -> применяет ко всем элементам iterable функцию котору мы передаем

# ls = ['one', 'two', 'three', 'four', 'five']
# res = list(map(str.upper, ls))
# print(res)

# for i in range(len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)

# -______________________________________________________
# names = ['John', 'Sultan', 'Jamie', 'Raychel', 'Aibek']
    
# res = list(map(lambda name: f'Hello mr/mrs {name}!', names))
# print(res)



# def func(name):
#     return f'Hello mr/mrs {name}!'


# res = []
# for name in names:
#     res.append(func(name))
# print(names)


# print(res)


# dict_ = {1: 2, 3: 4, 5: 6}
#     #{1: '2', 3: '4', 5: '6'}

# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print((res))

# ___________________________________________________

# filter(function, iterable) -> применяет ко всем элементам iterable функцию которую мы передали и возвращает итератор с теми элементами для которых функция вернула True



ls = ['one', 'two', '', 'list', '100', '1', 'john']

            # Старый код
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)

            # Усовершенствованный код 

# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ['John', 'codify', '
# aibek', 'ono', 'bootcamp', 'Kyrgyzstan', 'mountains']

# res = list(filter(lambda a: len(a) > 5, ls))
# print(res)




# ls = [
#     {'name': 'python', 'point': 10}, 
#     {'name': 'C++', 'point': 6},
#     {'name': 'JC', 'point': 8},
#     {'name': 'JAVA', 'point': 3}, 
#     {'name': 'C#', 'point': 0}
    
# ]

# res = list(filter(lambda x: x['point'] > 7, ls))
# print(res)



# users = [
# {"username": 'John', "comments": [
# "I love this content", "Realy Good"]},
# {
# "username": 'Raychel', "comments": []},
# {
# "username": 'Steven', "comments": ["Bishkek", "Python"]},
# {
# "username": 'Hello', "comments": []},
# {
# "username": 'Kira', "comments": [
# "The best"]},
# ]
# inactive_users = list(map(lambda x: x["username"], filter(lambda a: not a['comments'], users)))
# print(inactive_users)
# print()

# active_users = list(filter(lambda x: len(x['comments'])>0, users))
# print(active_users)

# ______________________________________
# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', "Bob"]
# new_names = list(map(lambda x: f'Hello mr/mrs {x}', filter(lambda x: len(x) > 5, names)))

# print(new_names)



# _______________________________________________________

# enumerate - Она пронумеровывает каждый элемент внутри iterable, ее собственным индексом

# ls = ['one', 'two', 'three', 'four', 'five']
# # res = list(enumerate(ls))
# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}!')




# ________________________________________________________

# Функция Reduce() принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не появятся элементы.

# from functools import reduce
# ls  = [1, 2, 3, 4, 5]
# sum_ = reduce(lambda a, b: a + b, ls)
# res = reduce(lambda a, b: a * b, ls)
# print(res)
# print()
# print(sum_)

# ________________________________________________________
# repeat
from itertools import repeat
from random import choices, shuffle
from string import ascii_letters, digits
from statistics import mean

symbols = '_()$!%+-@#'
q_pass = int(input('Введите количесвто паролей: '))
result = {f(choices(ascii_letters, k=10), choices(digits, k=5), choices(symbols, k=2)) for f in repeat(lambda a,d,s: ''.join(set(a+d+s)), q_pass)}
# a = [f for f in range(10)]
# {x for x in repeat(lambda, ''.join())}

print(result)
print(f'Quality of passwords: {len(result)}')
dlina = [len(x) for x in result]
print(f'Avarage len: {mean(dlina)}')












# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = (map(int, old_list))

# range(10) -> 0,1,2,3,4,5,6,7,8,9 
# 1,2,3,4,5,6,7

# print(new_list)

