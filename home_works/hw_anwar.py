# # 1

print('Привет, студент!')
name, surname, birth_year, patronymic = input(' Enter name: '), input(' Enter surname: '), int(input(' Enter birth year: ')), input(' Enter patronymic: ')
name = name.capitalize()
surname = surname.upper()

print(f'{surname}, {name} {patronymic.lower()} \n{birth_year} - года рождения \n\t\t рад приветствовать в нашей академии')



# # 2
a, b = int(input('Vvedite chislo 1: ')), int(input('Vvedite chislo 2: '))
ost = a % b
print(a == b)
print(a > b)
print(a < b)




# # 3
num = 7
n = int(input('Введите цифру от 1 до 10 : '))
if num == n:
    print('Браво, Вольф Мессинг!')
else:
    print('Не угадал')


# # 4
while True:
    num1, num2, oper = int(input('Введите первое число :')), int(input('Введите первое число :')), input('Выберите операцию (+, -, /, *), а для закрытия напишите \'end\'')

    if oper == '+':   
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '/':    
        print(num1 / num2)
    elif oper == '*':
        print(num1 * num2)
    elif oper == 'End' or oper == 'end' or num1 == 'end' or num1 == 'End' or num2 == 'end' or num2 == 'End':
        break
    else:
        print('Операция неизвестна')