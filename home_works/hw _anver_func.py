                # Задача 1
# def str_():
#     a = input('Введи строку: ')
#     count_A = 0
#     count_a = 0
#     for i in a:
#         if i.isalpha() and i.isupper():
#             count_A += 1
#         elif i.isalpha() and i.islower():
#             count_a += 1
#     print(f'количество букв верхнего регистра: {count_A} n\количество букв нижнего регистра: {count_a}')
# str_()

                # Задача 2

# def dict_():
#     n = int(input('Введите число: '))
#     dict__ = {i: i ** 3 for i in range(1, n+1)}
#     return dict__
# print(dict_())

#                     # Задача 3
                    
# def sum_range(start, end):
#     a = end
#     if start > end:
#         end = start
#         start = a
#     summa = 0
#     for i in range(start, end + 1):
#         summa += i
#     print(summa)
# while True:
#     try:
#         sum_range(int(input('Введите старт ')), int(input('Введите конец: ')))
#         break
#     except ValueError:
#         print('Вводите только целые числа')



                # Задача 4

# def izo():
#     a = input('Введите: ')
#     a = a.lower()
#     return True if a == a[::-1] else False
# print(izo())


                # Задача 5
# def op():
#     a = input('Введите текст: ')
#     b = []
#     v = []
#     a = a.split()
#     print(a)
#     for i in a:
#         if i[-1] == ',':
#             i = i[0:-1]
#         i = i.lower()
#         v.append(i) 
#         if i in b:
#             continue
#         else:
#             b.append(i) 

#     for sl in b:
#         print(f'{sl}: {v.count(sl)}')
# op()