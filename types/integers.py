                    # Типы данных - Числа -> int, float

# = -> оператор присваивания
# variable(Переменная)
# num = 5
# print(num) # 5
# num = 79 # переопределение
# print(num) # 79

# abc = Нижний регистр
# ABC = Верхний регистр
 
# PEP8 - правила написания кода на питоне
# tomorrow_day = '27.09.2023' # Snake case
# tomorrowDay = '27.09.2023' # Camel case

                    # +
# num1 = 5
# num2 = 15
# print('result: ', num1, '+', num2, '=', num1 + num2) # <---- Кастомная строка
    # Result 5 + 15 = 20
 

                    # -
# print(55 -45) 
# print(45- 5.5)

                    # *
# num1 = input('Enter the num1: ') # -> int('5') -> 5
# num2 = input('Enter the num2: ')

# num1 = int(num1)
# num2 = int(num2)

# result = num1 * num2
# print(num1, '*', num2, '=', result)


                    # / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление(получение остатка от деления)

# num1 = 10
# num2 = 4
# print('/', num1 / num2) # 2.3333
# print('//', num1 // num2) # 2
# print('%', num1 % num2) # 1

                    # **
# print(5 ** 2) # 5 * 5 -> возведение в степень
# print(9 ** 0.5) # 3 вытаскиваем квадратный корень


# pow - возведение в степень
# pow(num1, num2, <mod>)
# print(pow(5, 3, 3)) # 1) первое число возводится в степень второго и делится на 3 число

# round() - округление числа с плавающей точкой
# num1 = 5.367
# print(round(num1))

# abs() - асболютное значение числа -> |-67| -> 67
# a = abs(-657616)
# b = abs(16)
# print(a, b)
    #result(657616, 16)

# divmod(a, b) -> Она выводит два числа, первое число это a // b, а второе число a % b
# print(divmod(10, 4)) # 2, 1
# print(5 // 2, 5 % 2) # 2, 1
 

                    # Множественное присваивание
# = - это Оператор присваивания
# a = 5 # одно присваивание
# num1, num2, num3 = 4, 10, 7 # множественное присваивание

# num1, num2 = divmod(27, 8)
# print(num1, num2)

import math
# res = math.sqrt(144)
# print(res) # 12

# res = math.factorial(235) # 2 * 3 * 4 * 5
# print(res)

# r = int(input('Vvedite radius:'))
# pi = math.pi
# result_P = 2 * r * pi
# result_S = pi *(r ** 2)
# print('Площадь окружности : ', math.ceil(result_S))
# print('Периметр окружности : ', round(result_P))




