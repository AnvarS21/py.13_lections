# print('dsfkmsdfd')
# var = 5 + 5
# print(var * 10)




#                                  Типы данных в питоне
#   1. NoneType - ничего, пустота - None
# void = None
# stakan = 'water'
# stakan = None
# print(stakan)
#   2. Boolen - истина или ложь -> True/False
#   3. String - строки - str -> 'Hello world'
#   4. Числовые типы данных
#       а) integer - целое число - 1, 2, 555
#       b) float - число с плавающей точкой - 1.5, 45.12
#       c) complex - 0j: 1, 5-9j
#   5. Списковые типы данных (Коллекция)
#       а) list (массив/список) -> [5, 7, 10, True, 'HELLO']
#       b) tuple (кортеж) -> (1, 2, 3, None)
#       с) range (последовательность) -> 
#   6. set() - множества -> {1, 2, 3, 4, 5}
#   7. dict() - словари: данные хранятся в виде пар ключа и значения -> {1: 'one', 2: 'two'}


#                  Mutable(изменяемые типы данных)
# 1. list
# 2. set
# 3. dict


#                   Immutable(неизменяемые типы данных)
# 1. None
# 2. bool
# 3. int, float, complex
# 4. str
# 5. tuple, range
# 6. frozenset
# ----------------------------------------------------------------------
# Переменная - это именованная область(ячейка) памяти, предназначенная для хранения данных с ее помощью мы можем 
# проводить различные операции с данными:

# num = 5
# str1 = 'Hello world'
# print(num, type(num)) # 5 int
# print(str1, type(str1)) # hello world str

# '''
# Стандартный вывод данных в терминал'''
# # в питоне для вывода данных в терминал используется функция print()
# stroka = 'Hello world! my name is John Snow'
#  print(stroka)
# '''
# стандартный ввод данных
# используется функция input()
# '''
# name = input('Введите имя:')
# print(name, type(name))
# num1 = input('Vvedite num1: ')
# num2 = input('Vvedite num2: ')
# print('Result: ', int(num2) - int(num1))