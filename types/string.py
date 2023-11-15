# 'String - Строки'
# "Hello world! my name is John Snow"
# print("""I'm John Snow.
# I'm king of North!""")

# Строки набор последовательных символов, которые мы используем для хранения и представления текстовой информации

#                     Индексация в строке
# name = 'John'
#         # J = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1
# print(name)
# print(name[-1])
# str1 = 'world'
# print(str1[0], str1[-2])
#                     Срезы по индексам
# [start:end: <step>]
# str2 = 'birthday'
# print(str2[0:4])
# print(str2[5:])
# print(str2[:5])
# print(str2[:16])

# text = 'Hello world! My name is John Snow!, I\'m King of North!'
# print(text[::2]) 
# print(text[:13:-1])

# Конкатенация строк - Это соединение строк -> +
# a = 'Hello'
# b = 'World'
# c = ' '
# res = a + c + b

# \n -> перенос строки
# \t -> горизонтальная табуляция
# str1 = 'Hello World!\n\tHello John!'
# print(str1)

                    # Форматирование строк
# 1. с помощью %
# 2. с использованием .format()
# 3. интерполяция (преобразование строк) f-строки

                    # %
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# str1 = 'Hello mr/ms %s %s!' %(name, last_name)
# print(str1)

                    # .format
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# club = 'kipish'
# print('welcome to the club {}, mr/mrs {} {}!'.format(club, name, last_name))


                    # f-строки
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# print(f'Hello mr/mrs {name} {last_name}! Welcome to the party!')


#____________________________________________________________________________________

                    # методы строк - dir()
# print(dir(str))
# replace(old, new, [count]) - меняет в строке old на new, заменит count раз если передадите
# txt = 'ha ha ha ha'
# res = txt.replace('a', 'e', 2)
# print(res)
# print(f'result after replace: {res}')

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '    Hello     '
# print(len(a))
# print(a.strip())

# isdigit1  - Проверяют
# isnumeric - -> состоит ли наша строка
# isdecimal - полностью из чисел

# a = '56'
# print(a.isdigit())

# num = input('Vvedite chislo: ')
# print(f'Vvedeno li chislo? {num.isdigit()}')

# isalpha - состоит ли наша строка из символов алфавита
# txt = 'Hello world'
# print(txt)
# print(txt.isalpha())
# res = txt.replace(' ', '')
# print(res)
# print(res.isalpha())

# index(value, [start], [end]) - выводит индекс значение value внутри строки
# find(value, [start], [end]) - делает тоже самое что и index, но если не нащел то вернется -1

# text = 'Hello Anvar'
# print(text.index('a'))
# print(text.find('a'))

                # count(value, [start]) - он считает количество символов value внутри строки

# text = 'hello oooo oo o hello'
# print(text.count('a'))
# print(text.count('o'))
# print(text.count('hello'))
# print(text.count('hills'))
                # split(separator) - дробит(разделяет) строку на несколько частей по разделителю, все части сохранятся в типе list
# text = 'Let me speak by my heart!'
# res = text.split('e')
# print(text)
# print(res)
# print(text.split())

# a = '#hello#hello#hello#hello'
# print(a[1:].split('#'))

# 'connector'.join(list) - соединяет по connector строки которые были в list
# a = '#hello#hello#hello#hello#hiking'
# ls = a[1:].split('#')
# print(a)
# print(ls) #['hello', 'hello', 'hello', 'hello', 'hiking']
# res = '-'.join(ls)
# print(res)

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

          # john.capitalize() -> John
# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'jOHN edart snow'
# print(fio.title())
# print(fio.capitalize())
