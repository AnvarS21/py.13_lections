# Области видимости и пространство имен (scopes)
# Технология которая опеределяет контекст имени в рамках которого мы можем ее использовать

# built-ins(Встроенная область видимости) -> print( len)
# global(Глобальная) -> область одного файла
# enclosed(не локальная(замкнутая), nonlocal)
# local(локальная) -> область внутри одной функции


# x = 200

# def myFanc():
#     print(x)
#     a = 300
#     print(a)
#     return a
# myFanc()

# a = 10 #global
# print # built_in

# def hello(): # global
#     print(a)
#     a = 'Hello'
#     print(a, 'local inside in func')

# hello()
# print(a, 'global')

# LEGB - local enclosed global built-ins



# ------------------------------------------------------------------
# enclosed
# замкнутое пространство имен - локальное пространство, у которого есть внутреннее(вложение) локальное пространство

# x = 'global'
# print(x, '1') #global 

# def enclosed(): # global
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3') # local
#     print(x, '2') # enclosed
#     local()
#     print(x, '4') # enclosed

# enclosed()
# print(x, '5') # global

# --------------------------------------------
# global -> позволяет изменять значение глобальной переменной

# nonlocal -> позволяет изменять значение не локальной (замкнутой переменной находясь внутри локальной области)

# var = 0
# def increment(): #LEGB
#     global var
#     # print(var)
#     var += 1
#     print(var)
# increment()
# increment()
# increment()
# increment()
# increment()

# def func():
#     print('John Snow')

# a = func
# print(a())

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_steps = counter()
# c_squads = counter()
# # print(c_steps)
# print(c_steps()) #1
# print(c_steps()) #2
# print(c_steps())#3
# print(c_steps())#4
# print(c_steps())#5
# print(c_squads())#1
# print(c_squads())#2
# print(c_steps())#6
# print(c_steps())#7
# print(c_steps())#8


def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

def showStats(heroes, walkers):
    print()
    print(f'John Snow ты убил: \n\tгероев {heroes} \n\tбелых ходоков: {walkers}')
    print()
counter_heroes = counter()
counter_walkers = counter()
heroes = 0
walkers = 0
print("Приветствую вас, король севера  John Snow, в игре Престолов!")
print('Тебе доступны следующие действия: ')

while True:
    print()
    print('1 - убить героя, 2 - убить ходока, 3 - статистика, 4 - выйти из игры')
    choice = input('Введите что хотите сделать:').strip()
    if choice == '1':
        heroes = counter_heroes()
        print('Вы обезглавили Ланистера!')
    elif choice == '2':
        walkers = counter_walkers()
        print('Вы убили белого ходока!')
    elif choice == '3':
        showStats(heroes, walkers)
    elif choice == '4':
        print('Bye Bye!')
        break







