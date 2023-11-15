                    # Операторы сравнения
                    # Условные операторы и логические операторы

# Операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=
                # В питоне можно сравнивать строки между собой по таблице Аски сравнивают по первым буквам
# res = 5 > 3
# print(res)
# print(5 == 10, 10 == 10, 5 != 5, 5 != 6)
# print(5 >= 5)
# str1 = ' Codify'
# str2 = ' Bootcamp'
# print(str1 > str2)
# print(str1 < str2)
# print('ABC' == 'abc')

# print(ord('a'))
# print(ord('A'))

# str1 = 'Codify'
# str2 = 'Bootcamp'

# print(len(str1) > len(str2))
# print(len(str1) != len(str2))

                    # Условные операторы
# if elif else

# weather = 'rain'

# if weather == 'rain':
#     print('I gonna take an umbrella!')
# else:
#     print('I gonna take an sunglasses!')
    
# print('end!')
# name = input('Enter your name: ')

# if name == 'John':
#     print('My name is John Snow!')
#     print('John is a king of North!')

# age = int(input('Enter your age: '))

# if age > 18:
#     print(f'I\'m {age} years old!')

# string = input('Enter smt: ')

# if string.lower() == 'hello':
#     print('Hello, it\'s me. \nI was wondering if after all this years you\'d like to meet!')
# elif string.lower() == 'john':
#     print('Welcome back John Snow! The King of North!')
# elif string.lower() == 'abra-kadabra':
#     print('Sim salamon kadabra!')
# else:
#     print('Not found any match!')


# print('Registration form: ')
# email = input('Enter your email: ')
# password = input(('Enter your password: '))

# if len(password) < 8:
#     raise ValueError('Password is too short')
# elif password.isdigit():
#     raise ValueError('Password is invalid! \nAt least need one symbol!')
# elif password.isalpha():
#     raise ValueError('PAssword is invalid! \nAt least need one number!')

# password2 = input('Enter your password confirmation:')

# if password != password2:
#     raise Exception('Password didn\'t march!')

# print(f'Successfully registered! Hello Mr/Mrs {email}!')


# money = 1_000_000
# status = 'premium'

# if money >= 1_000_000 and status =='premium':
#     print('President of our Club')
# elif money >= 1_000_000 or status =='premium':
#     print('minister of our Club')
# else:
#     print('Honorable member of our club!')


# text = 'Hello world! S vami Aibek!'
# symbol = input('Enter the symbol: ')
# if symbol in text.lower():
#     print(f'The symbol: {symbol} exists in {text.lower().index(symbol)} index!')
# else:
#     print(f'The symbol: {symbol} not exists')
