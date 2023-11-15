                #Задача 1
# умножение похожих цифр в двух списках   
# from functools import reduce
# a = [3, 4, 6, 8, 2]
# b = [1, 3, 9, 5, 8, 6, 10, 38, 30]
# c = [i for i in a if i in b]
# res = reduce(lambda y, u: y * u, c)
# print(res)

# умножение соответствующих элементов в двух списках
# a = [3, 4, 6, 8, 2]
# b = [1, 3, 9, 5, 8, 6, 10, 38, 30]
# print(list(map(lambda x, y: x*y, a,b)))

                # Задача 2

# glas = 'eyuioa'
# str_ = 'pppppppppppq'
# res = any(map(lambda x: x in glas, str_))
# print(res)

                # Задача 3

# ls = ['Оливейра', 'Роберт', 'Бенджамин', 'Киесаки', 'Волкановски']
# print(list(filter(lambda x: len(x) > 7, ls)))

                # Задача 4

# ls = [3, 6, 324, 1, 3, 4]
# print(all(map(lambda x: x > 0, ls)))

                # Задача 5

# from functools import reduce
# list_ = [3, 4, 2, 67, 45, 3, 11]
# print(reduce(lambda x, y: (y ** 2) + (x ** 2), [i for i in list_ if i % 2 == 0]))

