"""
1) В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов и слов.
"""

# f = open('zadanie1.txt')
# count = 0
# count_i = 0
# a = []
# b = []
# for line in f:
#     count += 1
#     for i in line:
#         count_i += 1
#     a.append(count_i)
#     count_i = 0
#     line = line.split()
#     b.append(len(line))
# f.close()
# print(f'Количесвто строк: {count}')
# print(f'Количество символов в строке{a}')
# print(f'Количесвто слов в строке: {b}')


"""
2) Создайте файл nums.txt, содержащий несколько чисел, записанных через
пробел. Напишите программу, которая подсчитывает и выводит на экран
общую сумму чисел, хранящихся в этом файле.
"""
# f = open('nums.txt')
# summa = 0
# for line in f:
#     line = list(map(int, line.split()))
#     summa = sum(line)
# f.close()
# print(f'Сумма цифр: {summa}')

"""
3) Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
записать их произведение в файл output.txt.
"""
# summa = 1
# f1 = open('input.txt')
# for line in f1:
#     line = line.split()
#     for i in line:
#         summa *= int(i)
# f = open('output.txt', 'w')
# f.write(str(summa))
        
# f.close()
"""
5) В файле записаны в целые числа. Найти максимальное и минимальное
число и записать в другой файл.
"""
# f = open('max_min.txt')
# for line in f:
#     line = line.split()
#     res = [int(i) for i in line]

# f.close()
# f1 = open('max_min_res', 'w')
# f1.write(f'Максимальное число: {max(res)}\n')
# f1.write(f'Минимальное число: {min(res)}')
# f1.close()

"""
6) В файле записаны в столбик целые числа. Отсортировать их по
возрастанию суммы цифр и записать в другой файл.
"""


# with open('stolbik _num.txt', 'r') as f:
#     r = f.read()
#     r = r.split()
#     r = [int(i) for i in r]
#     r.sort()
#     r = [str(i) for i in r]
#     r = '\n'.join(r)
#     print(r)
#     with open('stolbik_sort', 'w') as fi:
#         fi.write(r)


'''1) Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым: Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела'''

# def read_last(lines, file):
#     try:
#         try:
#             with open(file, 'r') as p:
#                 p.seek(0)
#                 ls_lines = p.readlines()
#                 p.seek(0)
#                 ls_old = p.read()


#         except FileNotFoundError:
#             with open(file, 'w') as p:
#                 p.seek(0)

#                 ls_lines = p.readlines()
#                 p.seek(0)
#                 ls_old = p.read()


#         with open(file, 'w+') as f:
#             ls_lines = ls_lines[-2::]
#             ls_lines = ''.join(ls_lines)
#             ls_lines = ls_lines.split()
#             last_line = []
#             for i in range(lines):
#                 for x in ls_lines:
#                     last_line.append(x + '\n')
#             f.writelines(''.join(last_line))
#             f.seek(0)
#             print(f.read())
#             f.seek(0)
#             f.write(ls_old)
#     except ValueError:
#         print('Пустай файл!')


# read_last(2, 'moriarty.txt')


'''2) Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.'''
# import os

# print("lections", os.listdir())
'''
3) Документ «article.txt» содержит следующий текст: Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).'''
# with open('article.txt', 'r') as file:
#     max = 0
#     f = file.read()
#     for i in f.split():
#         if len(i) > max:
#             max = len(i)
#     for line in f.split():
#         if max == len(line):

#             print(line)
        

'''
4) Требуется создать csv-файл «rows_300.csv» со следующими столбцами: – № - номер по порядку (от 1 до 300); – Секунда – текущая секунда на вашем ПК; – Микросекунда – текущая миллисекунда на часах. На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.'''
# from datetime import datetime
# import time
# with open('rows_300.csv', 'w+') as file:
#     numeration = []
#     for i in range(1, 301):
#         time.sleep(0.01)
#         numeration.append(str(i) + ') ' + str(datetime.now().second) + ' ' + str(datetime.now().microsecond) + '\n')
#     file.writelines(numeration)

'''
5) При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне (каждый круг - отдельный файл). Для этого напишите функцию circles_generator(num_of_circles=100).
В первую очередь требуется установка модуля Pillow: pip install Pillow 
Осталось только случайным образом генерировать цвета в палитре RGB и воспользоваться классами Image, ImageDraw из установленной библиотеки. Чтобы нарисовать круг, нужно применить метод ellipse() и задать координаты точек, соответствующие квадрату.'''
import Pillow


'''
6) Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
наименование товара;
количество товара (целое число);
цена (в рублях) товара за 1 шт. (целое число).
Напишите программу, подсчитывающую общую стоимость заказа.'''

'''
7) Словарь из csv. Имеется файл data.csv, содержащий информацию в csv-формате. Напишите функцию read_csv() для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей. Функция read_csv() не должна принимать аргументов.'''
'''

😍 Запрещенные слова
Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
Формат ввода
Строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.
Формат вывода
Текст, отредактированный в соответствии с условием задачи.
Пример ввода вывода
Предположим, что forbidden_words.txt содержит следующие запрещенные слова:
hello email python the exam wor is
А текст файла, подлежащего цензуре, выглядит так:
Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
Тогда программа должна вывести отредактированный текст в таком виде:
*, *ld!   * programming language of * future. My * ....   awesome!!!!'''

'''
9) В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов'''