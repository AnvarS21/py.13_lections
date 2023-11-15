# """
# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
# # """
# # class Circle:
# #     color = 'blue'
# #     pi = 3.14

# #     def __init__(self, rad, color=color):
# #         self.rad = rad
# #         self.color = color

# #     def ploshad(self):
# #         print(f'Площадь круга: {self.rad ** 2 * self.pi}, \nЦвет: {self.color}')

# # c = Circle(5)
# # c.ploshad()



# """
# 2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
# """

# # class Song:
# #     def __init__(self, name_song, avtor, year):
# #         self.name = name_song
# #         self.avtor = avtor
# #         self.year = year

# #     def show_author(self):
# #         print(f'Автор этой песни {self.avtor}')
# #     def show_title(self):
# #         print(f'Название этой песни {self.name}')
# #     def show_year(self):
# #         print(f'Эта песня вышла в {self.year} году')

# # song = Song('Привет', 'Bakr', '2023')
# # song.show_author()
# # song.show_title()
# # song.show_year()
    


# """
# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
# """

# # class Taxi:
# #     def __init__(self, company_name, price: int, price_km: int):
# #         self.company_name = company_name
# #         self.price = price
# #         self.price_km = price_km

# #     def price_drive(self, km):
# #         return f'Стоимость поездки: {km * self.price_km + self.price}'

# # namba = Taxi('Namba', 100, 10)
# # print(namba.price_drive(5))

# # yandex = Taxi('Yandex', 150, 12)
# # print(yandex.price_drive(5))

# # jorgo = Taxi('Jorgo', 90, 8)
# # print(jorgo.price_drive(5))


# """
# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# """

# # class Tel_book:
# #     def __init__(self, name, last_name, tel_number):
# #         self.name = name + ' ' + last_name
# #         self.tel_number = tel_number

# #     def get_info(self):
# #         return f'Контакт: {self.name}, телефон: {self.tel_number}'

# # contact = Tel_book('Анвар', 'Шамсутдинов', +996707646192)
# # print(contact.get_info())


# """
# 5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
# """
# # class Salary:
# #     tax_per = 0.08
# #     def __init__(self, sum_salary: int, experience: int):
# #         self.sum_salary = sum_salary
# #         self.experience = experience

# #     def sum_tax(self):
# #         return f'Общая сумма налогов: {int(self.experience * 12 * self.sum_salary * self.tax_per)} сом!'

# # tax = Salary(10000, 2)
# # print(tax.sum_tax())
 


    
# """ 
# Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# # В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
#  """

# # class Soda:
# #     dobav = 'Обычная газировка'
# #     def __init__(self, dobav=dobav):
# #         self.dobav = dobav
# #     def show_my_drink(self):
# #         if self.dobav != 'Обычная газировка':
# #             return f'Газировка и {self.dobav}'
# #         else:
# #             return self.dobav

# # napitok = Soda('sdfgnfrew')
# # print(napitok.show_my_drink())


# """ 
# Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = [ ]
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.

#   """

# # class Student:
# #     books = []
# #     knowledge = 0
# #     def __init__(self, name, last_name):
# #         self.name = name + last_name

# #     def read_book(self, book_name):
# #         self.books.append(book_name)
# #         self.knowledge += 100
# #     def do_homework(self):
# #         self.knowledge += 10

# # a = Student('Анвар', 'Шамсутдинов')
# # a.read_book('Властелин колец: Братство колец')
# # a.read_book('Властелин колец: Две башни')
# # a.read_book('Гарри Поттер')
# # a.do_homework()

# # print(a.books)
# # print(a.knowledge)


# """
# 1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
# """
# # class Class1:
# #     def print_p1(self):
# #         print('Привет!')
# #     def print_p2(self):
# #         print('Как твои дела?')

# # class Class2(Class1):
# #     def print_p1(self):
# #         super().print_p1()
# #         print('У меня все отлично')
# #     def print_p2(self):
# #         super().print_p2()
# #         print('Я иду на учебу')

# # ekzemplyar = Class2()
# # ekzemplyar.print_p1()
# # ekzemplyar.print_p2()



# """
# 2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
# """
# # class A:
# #     def method1(self):
# #         print('Основной функционал')
    
# # class B(A):
# #     def method1(self):
# #         super().method1()
# #         print('Дополнительный функционал')

# # c = B()
# # c.method1()
# """
# 3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# # example = MyString('String')
# # example.append('hello')
# # print(example) -> 'Stringhello'
# # print(example.pop()) -> 'o'
# # print(example) -> 'Stringhell'
# """
# # class MyString(str):
# #     def __init__(self, str_1):
# #         self.str_1 = str_1

# #     def append(self, str_2):
# #         self.str_1 = self.str_1 + str_2
# #         return self.str_1
# #     def pop(self):
# #         last_al = self.str_1[-1:]
# #         self.str_1 = self.str_1[:-1]
# #         return last_al

# #     def __str__(self):
# #         return self.str_1
    


# # example = MyString('String')
# # example.append('hello')
# # print(example)
# # print(example.pop())
# # print(example)


# """
# 4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.
# """
# # class MyDict(dict):
# #     def init_subclass(cls) -> None:
# #         return super().init_subclass()

# #     def get(self, k):
# #         k = super().get(k)
# #         if k is None:
# #             return 'Are you kidding?'


# # a = MyDict(one=1, two=2)
# # print(a.get(''))



# """
# 5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
# Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
# Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
# """
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def display(self):
# #         return f'Имя: {self.name}\nВозраст: {self.age}'

# # class Student(Person):
# #     def __init__(self, name, age, facult):
# #         super().__init__(name, age)
# #         self.facult = facult
# #     def display_student(self):
# #         return f'Имя: {self.name}\nВозраст: {self.age}\nФакультет: {self.facult}'
        
# # anvar = Student('Anvar', 21, 'IT Tehnology')
# # print(anvar.display_student())


        


# """
# 6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
# """

# # class ContactList(list):
# #     def search_by_name(self, name):
# #         res = [i.lower() for i in self if i == name.lower()]
# #         return res
# # all_contacts = ContactList(['Анвар', 'Каныбек', 'Алтайбек', 'Марлен', 'Марлен'])
# # print(all_contacts.search_by_name('Марлен'))
# """
# 3. Создайте класс BankAccount, в конструкторе которого определена переменная
# экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
# который будет отнимать сумму от баланса и возвращать текущий баланс. Также
# добавьте метод deposit, который также имеет параметр amount и соответсвенно
# добавляет сумму к балансу, возвращает баланс.
# """

# # class BankAccount:
# #     balance = 0
# #     def __init__(self, balance=balance):
# #         self.balance = balance
# #     def withdraw(self, amount):
# #         self.balance = self.balance - amount
# #         return f'Ваш текущий баланс: {self.balance}'
# #     def deposit(self, amount):
# #         self.balance = self.balance + amount
# #         return f'Вы пополнили свой баланс!\nВаш текущий баланс: {self.balance}'

# # anvar = BankAccount(40)
# # anvar.withdraw(20)
# # anvar.deposit(60)
# # print(anvar.balance)


"""
7. Вам дан такой код:
winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())
который выводит в терминал такие значения:
Литература 1971 Пабло Неруда
выиграл 50 лет назад
Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад
Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
"""

# class Nobel:
#   def __init__(self, category, year, winner):
#     self.category = category
#     self.year = year
#     self.winner = winner
#   def get_year(self):
#     return f'Выиграл {2023 - self.year} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

"""
8. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'
если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.
Также переопределите метод str, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - ******
"""
# class Password:
#     chek_sym = False
#     chek_alpha = False
#     chek_num = False
#     chek_len = False
#     sym = '!@#$%&*'
#     alpha = 'qwertyuiopasdfghjklzxcvbnm'
#     num = '1234567890'
#     def __init__(self, passwords):
#         self.passwords = passwords
#     def validate(self):
#         if len(self.passwords) > 7:
#             self.chek_len = True
#         for i in self.passwords:
#             if i in self.sym:
#                 self.chek_sym = True
#             elif i.lower() in self.alpha:
#                 self.chek_alpha = True
#             elif i in self.num:
#                 self.chek_num = True
#         if self.chek_alpha == True and self.chek_len == True and self.chek_num == True and self.chek_sym == True:
#             return 'Ваш пароль сохранен!'
#         else:
#             return 'Пароль не годен!'
#     def __str__(self):
#         return f'{self.validate()}\n{"*" * len(self.passwords)}'
    
# a = Password('Privet12332456@')
# print(a)



"""
9. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 
"""

# import math
# class Math:
#     def __init__(self, num):
#         self.num = num
#     def get_factorial(self):
#         return math.factorial(self.num)
#     def get_sum(self):
#         self.num = str(self.num)
#         self.num = list(self.num)
#         p = 0
#         for i in self.num:
#             p += int(i)
#         return p
#     def get_mul_table(self):
#         for i in range(1, 11):
#             print(self.num, '*', i, '=', self.num * i)
# b = Math(5234)
# print(b.get_mul_table())

"""
10. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

"""


"""
11. оздайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""
# class Auto:
#     def ride(self):
#         print('Riding on a ground')
# class Boat:
#     def swim(self):
#         print('floating om water')
# class Amphibian(Auto, Boat):
#     pass
# a = Amphibian()
# a.ride()
# a.swim()

"""
12.
Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""
# class RadioMixin:
#     def play_music(self, name):
#         print(f'Музыка {name} играет!')
# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')
# class Boat(RadioMixin):
#     def swim(self):
#         print('floating om water')
# class Amphibian(Auto, Boat, RadioMixin):
#     pass
"""
13.Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""
# from datetime import datetime
# class Alarm:
#     def on(self):

# class Clock(Alarm):
#     def time_now(self):
#         return time.now()


"""
14.
Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

# class Coder:
#     experience = 'Pascal'
#     count_code_time = 0
#     def get_info(self):
#         return f'Язык {self.experience}\nВремя кодинга {self.count_code_time}'
#     def coding(self):
#         pass
# class Backend(Coder):
#     def __init__(self, languages_backend):
#         self.languages_backend = languages_backend
#         self.experience = self.languages_backend
#     def coding(self, hours):
#         self.count_code_time += hours
    
# class Frontend(Coder):
#     def __init__(self, languages_frontend):
#         self.languages_front = languages_frontend
#     def coding(self, hours):
#         self.count_code_time += hours


from random import randrange
import random
""" 

Создайте класс BankAccount, у которого должны быть:
        переменные объекта
            balance (со значением 0 по умолчанию)
            account_id (со значением random.randrange(100000,199999))
            transactions_history (c пустым словарем)
        методы
            withdraw (снять) принимает сумму, которую нужно снять с баланса и возвращает остаток баланса после снятия
            deposit (положить) принимает сумму, которую нужно положить на баланс и возвращает остаток баланса после пополнения
        После создания методов и переменных, попробуйте создать счет, пополнить баланс и снять деньги с баланса.
    В созданный класс BankAccount добавьте методы:
        receive (принять) который принимает сумму, увеличивает свой баланс, записывает счет отправителя в словарь transactions_history в качестве ключа, и сумму добавляет в список, который является значением. Почему список? Потому что переводов от данного банковского счета может быть много (пока дату перевода не будем записывать).
        transfer (перевести), который принимает сумму и другой экземпляр класса BankAccount (параметр назовём receiving_account), на который нужно перевести деньги. В результате работы этого метода нужно уменьшить сумму на балансе, вызвать метод receive у receiving_account. Метод должен возвращать остаток денег на балансе после перевода.
        После реализации этих методов, попробуйте создать несколько счетов, попробуйте совершить несколько денежных переводов. """

# class BankAccount:
    
#     def __init__(self):
#         self.balance = 0
#         self.transactions_history = {}
#         self.account_id = randrange(100000, 199999)

#     def withdraw(self, sum):
        
#         self.balance -= sum
#         return self.balance
#     def deposit(self, sum):

#         self.balance += sum
#         return self.balance
#     def receive(self, i, sum):
#         self.balance += sum 
#         if i.account_id in self.transactions_history:
#             self.transactions_history[i.account_id].append(sum)
#         else:
#             self.transactions_history[i.account_id] = [sum]
#         return self.balance

#     def transfer(self, receiving_account, sum):
#         self.balance -= sum
#         receiving_account.receive(self, sum)
#         return self.balance

# anvar = BankAccount()
# altai = BankAccount()
# kanybek = BankAccount()

# anvar.deposit(1000)
# print(anvar.balance)
# print(altai.balance)
# anvar.transfer(altai, 300)
# print(anvar.balance)
# print(altai.balance)
# anvar.receive(altai, 100)
# print(anvar.balance)
# print(altai.balance)



        
"""
1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, и пройдитесь по нему циклом чтобы распечатать длину сразу каждого из объектов.
"""
# a = 'stroka'
# ls = ['spisok']
# d = {1: 'Словарь'}
# list_ = [a, ls, d]
# for i in list_:
#     print(len(i))
"""
2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""
# class Dog:
#     def voice(self):
#         print('Гав!')

# class Cat:
#     def voice(self):
#         print('Мяу!')

# sobaka = Dog()
# koshka = Cat()

# def to_pet(a):
#     a.voice()
# to_pet(koshka)
"""
3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
классов переопределите метод, который отвечает за работу с оператором “+”.
Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
потом идти логика сложения 2 чисел, и выдача результата.
При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
конкатенация”, а затем логика конкатенации из базового класса и выдача результата.
"""
# class MyInt(int):
#     def __init__(self, my_int):
#         self.my_int = my_int

#     def __add__(self, other):
#         print('Это сложение!')
#         return self.my_int + other

# class MyString(str):
#     def __init__(self, my_str):
#         self.my_str = my_str
#     def __add__(self, other):
#         print('Это конкатенация!')
#         return self.my_str + other
# a = MyString
# print(a.__add__('we'))
# def add_objects(o):


"""
4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
-для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
-для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
-для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def get_info(self):
#         print(f'Привет меня зовут {self.name}')
    
# class Employee(Person):
#     def get_info(self):
#         super().get_info()
#         print('я работаю в компании "Рога и копыта" на должности "директор"')

# class Student(Person):
#     def get_info(self):
#         super().get_info()
#         print('я учусь в КГТУ на 3 курсе')

# def get_human_info(obj):
#     obj.get_info()


# a = Student('Anvar')
# get_human_info(a)

"""
5) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем наследуйте от Shape три класса: Triangle, Square и Circle.
-треугольник создаётся с заданными основанием и высотой
-квадрат создаётся с заданной длиной стороны
-круг создаётся с заданным радиусом
Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
"""
# class Shape:
#     pass
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, osn, vysota):
#         self.osn = osn
#         self.vysota = vysota
#     def get_area(self):
#         return self.osn * self.vysota / 2

# class Square(Shape):
#     def __init__(self, stor):
#         self.stor = stor
#     def get_area(self):
#         return self.stor * 2

# class Circle(Shape):
#     def __init__(self, rad):
#         self.rad = rad
#     def get_area(self):
#         return self.rad ** 2 / 3.14






"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""
# class M:

#     @property
#     def pu(self):
#         print('Это публичный метод!')

#     @property
#     def _zash(self):
#         print('Это защищенный метод!')
#     @property
#     def __priv(self):
#         print('Это приватный метод!')
# a = M()
# a.pu
# a._zash
# a._M__priv
"""
2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
"""
# class A:
#     def method1(self):
#         print('Hello World')
# class B(A):
#     pass
# b = B()
# b.method1()

"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""
# class Car:
#     def __init__(self):
#         self.__speed = 0
#     def set_speed(self, speed):
#         self.__speed = speed
#     @property
#     def show_speed(self):
#         return self.__speed

# a = Car()
# print(a.show_speed)
# a.set_speed(100)
# print(a.show_speed)

"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
# """
# class Car:
#     def __init__(self):
#         self.__speed = 0

#     @property
#     def show_speed(self):
#         return self.__speed

#     @show_speed.setter
#     def set_speed(self, speed):
#         self.__speed += speed


# a = Car()
# print(a.show_speed)
# a.set_speed = 100
# print(a.show_speed)

"""
5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью приватного
метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
"""
# class Car:
#     def __init__(self, make, model, year, fuel=70, odometer=0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel
#     def drive(self, km):
#         if km / 10 > self.fuel:
#             print('Need more fuel, please, fill more!')
#         else:
#             self.__add_distance(km)
#             self.__subtract_fuel(km)
#     def __add_distance(self, km):
#         self.odometer += km

#     def __subtract_fuel(self, km):
#         self.fuel -= km / 10
#         print('Lets drive!')

# Lexus = Car('V8', 'RX350', 2013, 10)
# Lexus.drive(100)
# print(Lexus.odometer)

"""
6)# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
"""

class MobilePhone:
    def __init__(self, imei, os, battary=100):
        self._imei = imei
        self._battery = battary
        self._os = os

    def __discharge(self, a):
        if a == 0:
            print('Батарея разряжена!')
        else: 
            pass

    @property
    def get_info(self):
        print(f'Уровень заряда: {self._battery}')
        if self._battery > 0.5: 
            self._battery -= 0.5
        else:
            self._battery -= 0.5
            self._battery = 0
        self.__discharge(self._battery)

    @property
    def listen_mus(self):
        if self._battery > 5.5: 
            self._battery -= 5
            print('Вы прослушиваете музыку!')
        else:
            self._battery -= 5
            self._battery = 0
        self.__discharge(self._battery)
    @property
    def watch_video(self):
        if self._battery >= 10:
            self._battery -= 7.5
            print('Вы просматриваете видео!')
        else:
            print('Уровень заряда батареи не позволяет смотреть видео!')
    @watch_video.setter
    def charge(self, time):
        self._battery += time * 2 
        if self._battery >= 100:
            self._battery = 100
            print('Батарея заряжена!')
    
pro = MobilePhone(2432, 'Android', 15)
pro.get_info
pro.watch_video
pro.get_info
pro.listen_mus
pro.get_info
pro.charge = 20

print(pro._battery)
##--------------------------##--------------------------##--------------------------##--------------------------

# class MobilePhone:
#     def __init__(self, imei, os):
#         self._imei = imei
#         self._battery = 100
#         self._os = os
#     def power(method):
#         def wrapper(self):
#             self._battery -= 0.5
#             if self._battery <= 0:
#                 self._battery = 0
#                 print('Батарея разряжена!')
#             method(self)
#         return wrapper
#     @property
#     @power
#     def music(self):
#         print('Playing music...')
#         self._battery -= 5
#     @property
#     @power
#     def video(self):
#         print('Playing video...')
#         self._battery -= 7


# pro = MobilePhone(123, 'Android')
# print(pro._battery)
# pro.music
# pro.video
# print(pro._battery)

##---------------------------------##---------------------------------##---------------------------------
