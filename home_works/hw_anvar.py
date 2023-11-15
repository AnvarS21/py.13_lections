# import random

# def run(f):
#     def wrapper():
#         res = f'Функция {f.__name__} была занущена успешно'
#         dict_ = {f(): id(f())}
#         print(dict_)
#         return res
        
#     return wrapper
# @run
# def dict():
#     return random.randint(1, 1000)
    
# print(dict())


# _____________________________________________________
# def fraza():
#     f = input('Введите фразу').split()
#     rez = ''.join([i[0].upper() for i in f])
#     return rez

# print(fraza())

# ____________________________________________________________
# def uch(steps):
#     count = 0
#     kolvo_0 = 0

#     for i in steps.upper():
#         if i == 'U':
#             count += 1
#         elif i == 'D':
#             count -= 1
#             if count == 0:
#                 continue

#         if count == 0:
#             kolvo_0 += 1

#     print(kolvo_0)


# uch('')
