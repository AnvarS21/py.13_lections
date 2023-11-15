# Генераторы

# print(x for x in range(1, 10))
# x, a, b = (x for x in range(1, 4))
# print(x, a, b)

# list comprehensions - генераторы списков 
# list comprehensions - упрощенный подход к созданию списков, который задействует в себе цикл for, а так же конструкцию if для определения того, что в итоге попадает в нащ список
# __________________________________________________________________
# list -> 0 - 200 -> chetnye
# ls = []
# for x in range(0, 200):
#     if x % 2 == 0:
#         ls.append(x)
# print(ls)


# ls = [x for x in range(0, 200) if x % 2 == 0]
# print(ls)

# list -> 0, 300 -> num % 2, 4
# ls = {x for x in range(0, 300) if x % 2 == 0 and x % 4 == 0}; print(ls)


# list - 0, 100 -> x 2 -> ** 2, x 3 -> x ** 3

# ls = [x ** 2 if x % 2 == 0 else x ** 3
#         for x in range(101)
#         if x % 2 == 0 or x % 3 == 0]
# print(ls)




# ___________________________________________________________
# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = [item for x in ls for item in x]
# print(res)
# __________________________________________________________
from datetime import datetime

# start = datetime.now()# 12:22:56
# ls = [x for x in range(0, 100_000_000)]
# finish = datetime.now() #12:23:01
# print(finish - start)

# start = datetime.now()# 12:22:56
# ls = []
# for x in range(0, 100_000_000):
#     ls.append(x)
# finish = datetime.now() #12:23:01
# print(finish - start)

# ______________________________________________________
# dict_ = {x: x ** 2 for x in range(11)}
# print(dict_)

# ______________________________________________________
# names = ['John', 'Tirion', 'Sansa', 'Eygan', 'Ramsi']
# res = {name: len(name) for name in names}
# print(names)
# print(res)

