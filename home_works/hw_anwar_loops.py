# 1

# a  = ['Анвар', 'Алтай', 'Марлен', 'Адилет', 'Осмон']
# name = input('Введите имя: ')
# if name in a:
#     print(f'Приветствую, любезный {name}!')
# else:
#     print('Тут ничего нет. Еще есть вопросы?')


# 2

# a = {'Кто ты?': 'Я программа', 'Что делашь?': 'Работаю', 'Как дела?': 'Хорошо', 'Как это работает?': 'Как-то так', 'Где ты?': 'У тебя на компе'}
# while True:
#     b = input('Вопрос: ')
#     if b == 'q':
#         break
#     elif b in a.keys():
#         print(a[b])
#     else:
#         print('ай нот андестенд!')
    


# 3

# a = input('Введите белеберду: ')
# b = []
# s = ''
# import re

# n = re.findall(r'\d*\.\d+|\d+', a)

# n = [float(i) for i in n]

# print(sum(n))

a = input('Введите беледерду: ')
if a == '':
    raise Exception('Вы ввели пустую строку!') # Если пользователь ввел пустую строку выводим ошибку
a = list(a)
b = []
count = 0
if a[0] == '.' or a[-1] == '.': #Убираем точки в начале списка и в конце если они есть
        a.remove('.')
for i in a:
    if i.isalpha() or i == '/' or i == '=' or i == '+' or i == '?' or i == '%' or i == '@' or i == '$' or i == ':' or i == '!' or i == '~' or i == '"' or i == "'" or i == '*' or i == ',' or i == ';':
        a[a.index(i)] = ' ' 
                                #Заменяем НЕ цифры пробелом для легкой работы
for u in a:
    if u == ' ':             #Перебираем каждый элемент, если это НЕ пробел то добавляем в список Б
                             #если далее нам попадается пробел и список Б не пуст(там уже добавлены цифры)
                             #то мы преобразовываем во флоат и добавляем в count и обнуляем список
        if len(b) != 0:
            if b[0] == '.':
                b.remove('.')
            b = ''.join(b)
            b = float(b)
            count += b
            b = []
            
    elif len(b) != 0 and u == '-':
            b = ''.join(b)
            b = float(b)
            count += b
            b = ['-']
    elif len(b) != 0 and '.' in b and u == '.':
        b = ''.join(b)
        b = float(b)
        count += b
        b = []

        
    


    
        
    else:
        b.append(u)
#Строчки кода ниже потому что цикл сверху не обрабатывает последний список Б
if len(b) != 0:
    if b[0] == '.':
        b.remove('.')
    b = ''.join(b)
    b = float(b)
    count += b


print(f'Сумма цифр в строке: {count}')