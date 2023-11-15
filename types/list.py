# list() - (списки, массив) - изменяемый тип данных, который представляет из себя коллекцию каких либо обьектов

# my_list = [1, 'string', False, None, [1, 2, 3, 4]]
# print(my_list, type(my_list))
# print(my_list[0])
# print(my_list[-1][2])

# print(my_list[2:4])

# range() - возвращает последовательность чисел
# ls = range(1, 10)
# spisok = list(ls)
# print(spisok, type(spisok))

# tuple_ = ('123', 1, 2, 3, 4, 5)
# print(tuple_, type(tuple_))
# a = (5, 7, 9)
# num1, num2, num3 = a
# print(num1, num2, num3)
# b = 1, 2, 3, 4, 5
# print(b, type(b))

#________________________________________________________
# ls = [1, 2, [123, 234, 234], True, 3, 4, 5, 6, 'string, False']
# i = 0
# while i < len(ls):
#     # print(i)
#     print(ls[i])
#     i += 1 #increment

# ls = [1, 2, [123, 234, 234], True, 3, 4, 5, 6, 'string, False']

# for x in ls:
#     print(x)

# ls = ['John', 'Sansa', 'Tirion', 'Eddart', 'Jamie', 'Serseya']
# print(ls, len(ls))

# black_list = ['Serseya', 'Jamie']

# for name in ls:
#     if name not in black_list:
#         print(f'We\'re calling to {name}!')
#     else:
#         print(f'{name} is black listed!')


# ls -> 1, 21 -> четные числа - квадрат числа
#             # -> нечентные числа - куб числа
# ls = list(range(1, 21))
# for i in ls:
#     if i % 2 == 0:
#         print(f'Число {i} четное  ------> квадрат: {i ** 2}')
#     else:
#         print(f'Число {i} нечетное  ------> куб: {i ** 3}')


#__________________________________________________
#методы списков
# print(dir([]))
# append(element) - добавляет элемент в конец списка
# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# print(ls)
# ls.append([True, False, True])
# print(ls)

# extend(object) - расширяет список элементами из object
# ls = [1, 2, 3]
# print(ls)
# ls.append('Hello')
# ls.append([4, 5, 6])
# print(ls)

# ls = [1, 2, 3]
# print(ls)
# ls.extend('Hello')
# ls.extend([4, 5, 6])
# print(ls)

# insert(index, element) - добавляет элемент по индексу
# ls = ['string', 2, 3, False]
# print(ls)
# ls.insert(2, None)
# print(ls)

# remove(element) - удаляет элемент из списка, если нет такого то будет ошибка
# pop([index]) - удаляети возвращает элемент по index, если нет index то ужалит последний элемент

# ls = [5, 1, 2, 3, 4, 5, 5, 5, 5, 5]
# print(ls)
# # ls.remove(5)
# # print(ls)
# print(5 in ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)

# ls = [5, 1, 2, 3, 4]
# ls.pop()
# print(ls)

# deleted = ls.pop(0)
# print(ls)
# print(delete)

# update
# ls = [1, 'h', 3, 4, 5, 6, 7, None, 9]
# i = ls.index(None)
# ls[i] = 8
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# ls = ls[::-1]
# print(ls)


# sort() - сортирует список, если передать revese = True, то список отсортируется в убывающем порядке

# from random import randint

# ls = []
# for x in range (0, 50):
#     num = randint(0, 1000)
#     ls.append(num)
# print(ls)
# ls.sort()
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'Osmon', 'Aibek', 'aizhan']
# ls.sort(key = len)
# print('\n', ls)