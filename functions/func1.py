# Найти квадрат, куб, результат деления на 100 любого числа

# num1 = 5
# -> {'num': 5, '2': 25, '3': 125, '100': 0.05}
# num1 = 5
# res = {'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100}
# print(res)

# num2 = 75
# res = {'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100}
# print(res)

# num3 = 1154
# res = {'num': num3, '2': num3** 2, '3': num3 ** 3, '100': num3 / 100}
# print(res)


# DRY - Don't repeat yourself

# def do_operations(num: int):
#     res = {'num': num, '2': num** 2, '3': num ** 3, '100': num / 100}
#     print(res)

# do_operations(int(input('sd ')))
# do_operations(4356)
# do_operations(31)
# do_operations(1298)
# do_operations(567)


# __________________________________
# Функция - это именнованая часть программы, которая содержит в себе определенный блок кода, и может вызываться в других частях программы столько раз сколько угодно



# def name_of_func(<a, b> # параметры функции):
#     <body> # код, какая то логика которая будет давать конечный результат
#     <return> # оператор который помогает сохранить результат

# name_of_func(5, 6 # Аргументы)

# параметры функции - переменные в которые мы временно сохранаяем данные которые передаем при вызове в функцию, доступны только внутри функции

# аргументы функции - это данные которые мы передаем при вызове функции , они попадают в параметры по очередно

# from typing import Iterable

# def our_len(obj: Iterable) -> str:
#     '''Возвращает длину итерируемого обьектa'''
#     print(obj)
#     i = 0
#     for o in obj:
#         i += 1
#     return f"result: {i}"


# # print(len('string'))
# ls = [1, 2, 3, 4, 5]
# str1 = 'Hello world s vami John Snow!'

# print(our_len(ls))
# print(our_len(str1))


# def isEven(num):
#     return True if num % 2 == 0 else False

# res = isEven(15)
# print(res)


# def isEven(num: int) -> bool:
#     '''Return True or False while after cheking number for even!'''
#     return True if num % 2 == 0 else False

# res = isEven(456)
# print(res)


# ________________________________
# def sum_of_args(a: int, b: int, c: int = 0) -> int:
#     '''Возвращает сумму аргументов'''
#     return a + b + c

# print(sum_of_args(5, 6, 7))
# print(sum_of_args(9, 123))

# ________________________________________________________
# позиционные и именнованные аргументы

# def printParams(a, b, c):
#     print(a, 'in stored in param a')
#     print(b, 'in stored in param b')
#     print(c, 'in stored in param c')

# printParams(10, 5, 15) # Позиционные аргументы (Arguments)
# print()
# printParams(b = 5, a = 10, c = 15) # Именованные аргументы (keyword arguments)
# print()
# printParams(5, c=10, b=15)

# _____________________________________
# оператор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)
# ___________________________________________
# # *args, **kwargs
# def get_some_data(a, b, *args, **kwargs):
#     print('parametry a и b:', a, b)
#     print('Аргументы: ', args)
#     print('именованные аргументы: ', kwargs)
# get_some_data(1, 2, 3, 4, 5, x=5, b='BMW')


# def printScores(student: str, *scores):
#     """prints info about student to terminal!"""
#     print(f'name of student: {student}!')
#     print(f'AVG: {round(sum(scores) / len(scores), 1)}')
#     print(scores, type(scores), '!!!')
#     for x in scores:
#         print('Score:', x)


# printScores('John Snow', 5, 5, 5, 5, 4, 4, 2)



# def printPetNames(owner: str, **pets):
#     print(f'Owner name {owner}!')
#     print(pets, type(pets), '!!!')
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')
# printPetNames('John Snow', dog='Pluto', cat='Garfild', fish=['nemo', 'Dori', 'Golden'], turtle = 'Leonardo')



# #--------------------------------------------------------
# from random import choice, shuffle
# from string import ascii_letters, digits, punctuation

# symbols = digits + ascii_letters

# def generate_password(len_: int = 8) -> str:
#     '''Function generates random string for password, parameter len needs to give lenghts of password. If blank len_ = 8'''
#     res = [choice(symbols) for _ in range(len_ - 2)] + [choice(punctuation) for _ in range(2)]
#     shuffle(res)
#     return ''.join(res)

# print(generate_password())
# print(generate_password(12))


# -------------------------------------------------------
