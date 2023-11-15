# num = int(input('Vvedite chislo: '))
# if num % 2 == 0:
#     print('even!')
# else:
#     print('odd!')

# res = 'even!' if num % 2 == 0 else 'odd!'  #Тернарные операторы - можно написать в 1 строку
# print(res)

# __________________________________________________________
# Ternary operators(тернарный оператор) - это конструкция, которая по своему действию аналогична конструкции if/else, но при этом записывается в одну строчку
# <выражение если True> if <условие> else<выражение если False>

# sentence = input('vvedite predlozhenie: ')
# if sentence[-1] == '?':
#     res = 'voproaitelnoe'
# else:
#     res = 'Normal one!'
# print(res)
# res = 'voprositelnoe' if sentence[-1] == '?' else 'Normal one!'
# print(res)


#__________________________________________________________________________

# ls = [55, 12, 75, 89, 99, 15, 11]
# print(ls)
# choice = input('vvedite min/max: ').lower().strip()
# res = max(ls) if choice == 'max' else min(ls) if choice == 'min' else 'incorect choice'
# print(res)
# ____________________________________________________________________

flag = True
symbols = '1234567890' + '-' + '.'
while flag:
    print()
    num1 = input('vvedite 1 chislo: ')
    #-54, 63e4, 100.54, 51
    is_correct = True
    for x in num1:
        if x not in symbols:
            print('Вы ввели неправильное число!')
            is_correct = False
            break
    if not is_correct:
        continue
    
    num2 = input('vvedite 2 chislo: ')
    #-54, 63e4, 100.54, 51
    is_correct = True
    for x in num2:
        if x not in symbols:
            print('Вы ввели неправильное число!')
            is_correct = False
            break
    if not is_correct:
        continue

    num1 = float(num1) if '.' in num1 else int(num1)

    num2 = float(num2) if '.' in num2 else int(num2)
    # print(type(num1), num1)
    # print(type(num2), num2)
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
    


    