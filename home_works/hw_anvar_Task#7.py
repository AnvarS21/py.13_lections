
                    # Задача 1  
# flag = True
# def summa_n(n):
#     if n.isdigit():
#         n = int(n)
#         summa = 0
#         for i in range(0, n + 1):
#             summa += i
#         print(f'я знаю, что сумма чисел от 1 до {n} равна {summa}')
#     elif n == 'выход':
#         global flag
#         flag = False
#     else:
#         print('Введите число!')  
    
# while flag:
#     a = input('Введите число: ')  
#     summa_n(a)

                          # Задача 2
# def test(a):
#     def pozitive():
#         print('Положительное')
#     def negative():
#         print('Отрицательное')
#     if a > 0:
#         pozitive()
#     else:
#         negative()

# test(int(input('Введите число: ')))


                         # Задача 3

# figura = input('Какой формат? ').strip().lower()

# if figura == 'треугольник':
#     def tri(stor, vysot):
#         print(f'Площадь треугольника {stor*vysot / 2} кв.')
#     tri(stor = int(input('Введите длину стороны: ')), vysot = int(input('Введите высоту: ')))

# elif figura == 'круг':
#     def krug(radius):
#         print(f'Площадь круга {(radius ** 2) * 3.14} кв.')
#     krug(radius = int(input('Введите радиус круга: ')))

# elif figura == 'прямоугольник':
#     def prya(st1, st2):
#         print(f'Площадь прямоугольника {st1 * st2} кв.')
#     prya(st1 = int(input('Введите 1ю сторону: ')), st2 = int(input('Введите 2ю сторону: ')))
# else:
#     print('Неизвестная фигура!')


                        # Задача 4
# flag = True
# def perev(num):
#     if num.isdigit():
#         num = list(num)
#         num = num[::-1]
#         num = ''.join(num)
#         print(f'Число наоборот: {num}')
#     elif num == 'Программа завершена!':
#         global flag
#         flag = False
#     else:
#         print('Вводите число!')
# while flag:
#     perev(input('Вint(input('Монет по 1 копейке: ')ведите число: '))
    



                    # Задача 5

# def kassa():
#     m1 = int(input('Монет по 1 копейке: '))
#     m5 = int(input('Монет по 5 копеек: '))
#     m10 = int(input('Монет по 10 копеек: '))
#     m50 = int(input('Монет по 50 копеек: '))
#     sum = (m1 * 0.01) + (m5 * 0.05) + (m10 * 0.10) + (m50 * 0.5)
#     print(f'Всего у нас {round(sum, 2)} рубля')
# kassa()













        