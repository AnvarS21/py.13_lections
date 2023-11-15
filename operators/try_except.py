# обработка исключений
# операторы try....except

# Ошибки Errors -> связаны с кодом
    # SyntaxError
    # TabError
    # IndentationError
# a = 5
# b = 6
# var = int('55b') Не работает потому что неправильные данные, код свыше сработает

# Исключения Exceptions -> связаны с неправильным вводом данных, которые передаются в код 
# ValueError 
# TypeError
# NameError
# ZeroDivisionError
# IndexError
# KeyError
# ImportError
# BaseException # Прородитель всех ошибок
# try:
#     num1 = int(input('Enter the num1: '))
#     num2 = int(input('Enter the num2: '))
#     print(num1 / num2)
# except (ValueError):
#     print('Invalid values for num!')
# except ZeroDivisionError:
#     print('Cant divide by zero!')

# try:
#     <body> # код с вероятным исключением
# except:
#     <body except> сработает только если ошибка в try
# <else>:
#     <body> сработает только если нет ошибки в try
# <finally>:
#     <body> сработает в любом случае

# dict_ = {1: 'one', 2: 'two', 3:'three'}
# print(dict_)
# try:
#     key = int(input('Vvedite key: '))
#     print(dict_[key])
# except ValueError:
#     print('Invalid value for key!')
# except KeyError:
#     print('Key does not exists!')
# else:
#     print('No errors!')
# finally:
#     print('The end!')


# ______________________________________________________________________
# отображение ошибки
# 1. import sys

# ls = [1, 2, 3, 4, 5]
# try:
#     index = int(input('Vvedite index: '))
#     print(ls[index])
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error')

# 2. Exception as e
ls = [1, 2, 3, 4, 5]
while True:
    try:
        index = int(input('Vvedite index: '))
        print(ls[index])
    except Exception as e:
        print(f'Oops, we catced {e.__class__} error!')





        # _______________________________________________


flag = True
symbols = '1234567890' + '-' + '.'
while flag:
    print()
    
    num1 = input('vvedite 1 chislo: ')
    num2 = input('vvedite 2 chislo: ')
    try:
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)
    except ValueError:
        print('Vy vveli nekorektnoe chislo!')
        continue


    operator = input('Введите операцию(, +, -, /, *): ').strip()
    if operator == '+':
        print(f'Результат {num1 + num2}')
    elif operator == '-':
        print(f'Результат {num1 - num2}')
    elif operator == '*':
        print(f'Результат {num1 * num2}')
    elif operator == '/':
        print(f'Результат {num1 / num2}' if num2 != 0 else 'На ноль делить нельзя!')
    else:
        print('Неправильный оператор!')

    choice = input('Хотите продолжить?(yes/no): ')
    if choice.lower().strip() != 'yes':
        flag = False
        print('Пока пока!') 

