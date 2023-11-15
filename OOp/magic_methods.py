# magic methods (магические методы)
# dunder methods (double underscore) -> __init__
# служебные методы

# Магия(фишка) закллючается в том что эти методы запскаются без прямого обращения к ним, определенные методы могут отвечать за определенные операторы

# class A(int):
#     def __init__(self):
#         pass
#     def func(self):
#         pass

# obj = A()
# print(dir(obj))

##----------------##----------------##----------------##----------------##----------------

# dunder methodы сравнения

# __eq__(self, other) -> 5 == (8)
#                       #5.__eq__(8)
# __ne__ -> !=
# __lt__ -> <
# __gt__ -> >
# __le__ -> <=
# __ge__ -> >=



# __sub__(self, other) -> -
# __mul__ -> *    __div__ -> /
# __mod__ -> %    __floordiv__ -> //
# __add__ -> +    __pow__ -> **

##---------##---------##---------##---------##---------##---------##---------##---------

# class MyClass:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return self.string
    
#     def __add__(self, other):
#         print('add worked!')
#         print(self, '***')
#         print(other, '___')
#         res = self.string + ' ' + other.string
#         return MyClass(res)

# obj1 = MyClass('John')
# obj2 = MyClass('Jamie')
# obj3 = MyClass('Lanister')
# res = obj1 + obj2 + obj3
# print(res.string)

##---------##---------##---------##---------##---------##---------##---------##---------

# class Word(str):
#     def __init__(self, word):
#         self.word = word
    
#     def __gt__(self, __value):
#         print('gt сработал')
#         print(self, '!!!!')
#         print(__value, '****')
#         return len(self) > len(__value)

# obj1 = Word('John')
# obj2 = Word('hello world')

# print(obj1 > obj2)

#------------#------------#------------#------------#------------#------------#------------


# дандер методы строкового отображения объектов
# __str__ -> для отображения строки, которую будут видеть ползователи
# __repr__ -> строковую информацию о том как создать объект

# print(eval('6 + 6')) # -> 6 + 6 -> 12

# class Base:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return f'Объект: {self.string}'

#     def __repr__(self):
#         return 'Base("string")'

# user = Base('Hello John')

# print(user)
# a = eval(repr(user))
# print(a)

##---------##---------##---------##---------##---------##---------##---------##---------

# Конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# деструктор -> __del__(self) 

# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance

#     def __add__(self, other):
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')
#         return Cifra(res)

# value1 = Cifra(-117)
# value2 = Cifra(54)
# value3 = Cifra(-7778)
# a = value1 + value2
# value3 + a


##-----------##-----------##-----------##-----------##-----------##-----------##-----------
# from random import choice
# class Dog:
#     def sound(self):
#         print('Bark')

# class Cat:
#     def sound(self):
#         print('Meow!')

# class Parrot:
#     def sound(self):
#         print('say')

# class Pat:
#     def __new__(cls):
#         other = choice([Dog, Cat, Parrot])
#         instance = super().__new__(other)
#         print(f'I\'m {type(instance)}')
#         return instance

#     def __init__(self):
#         print('init was never closed!')

# pet = Pat()
# pet.sound()

##---------##---------##---------##---------##---------##---------##---------


# SINGLETON
# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self):
#         return str(id(self))


# class A:
#     def __del__(self):
#         choice = input('Are you sure to delete(yes/no): ')
#         if choice.lower().strip() == 'yes':
#             del self
#             print('Deleted')
#         else:
#             print('Operation denied!')
# obj = A()
# del obj
# print(obj)


##---------------##---------------##---------------##---------------##--------------
##---------------##---------------##---------------##---------------##--------------
##---------------##---------------##---------------##---------------##--------------
##---------------##---------------##---------------##---------------##--------------
"""
1. Создайте класс Account и переопределите в нем методы init, repr, str и del.
Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
Метод init должен возвращать сообщение о создании счета, repr только имя держателя счета
и баланс, а str сообщение с приветствием и также информацией о держателе счета, 
балансе и филиале банка в котором зарегистрирован клиент, del в свою очередь сообщение об удаление 
и слово "Пока!"
"""
# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Счет создан!')
#     def __repr__(self):
#         return f'Имя держателя: {self.name}\nБаланс: {self.balance}'
#     def __str__(self):
#         return f'Здраствуйте!\nФИО: {self.name}\nБаланс: {self.balance}\nГород проживания: {self.city}'
#     def __del__(self):
#         del self
#         print('Пока, епта!')
# a = Account('Анвар', 900, 'Бишкек')

"""
2. Определите класс MyNumber который наследуется от класса int. 
У экземпляра класса должен быть обязательный атрибут value. 
Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
"""
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         res = self.value + other

#         return f'Это сложение и ваш результат равен {res}'
#     def __sub__(self, other):
#         res = self.value - other

#         return f'Это вычитание и ваш результат равен {res}'
#     def __mul__(self, other):
#         res = self.value * other
#         return f'Это умножение и ваш результат равен {res}'
#     def __truediv__(self, other):
#         res = self.value / other
#         return f'Это деление и ваш результат равен {res}'
        
# num = MyNumber(5)
# print(num + 5)
# print(num - 5)
# print(num * 5)
# print(num / 5)



"""
3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""
# class MyList(list):
#     def __init__(self, values):
#         self.values = values
    
#     def __getitem__(self, key):
#         if key > 0:
#             return self.values[key-1]
#         elif key < 0:
#             return self.values[key]
#         else:
#             raise IndexError


# x = MyList(['sd', 'asd', 'ty'])
# print(x[1])
    

"""
4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""
# class Student:
#     def __init__(self, first_name, last_name, class_, grade):
#         self.name = first_name + ' ' + last_name
#         self.class_ = class_
#         self.grade = grade
#         self.average = 0
#     @property
#     def av(self):
#         ls_grade = [i for k, i in self.grade.items()]
#         self.average = sum(ls_grade) / len(ls_grade)
#         self.average = round(self.average, 1)


# a = Student('John', 'Snow', 8, {'math': 100, 'history': 89, 'literature': 88})
# a.av
# b = Student('Jamie', 'Lanister', 8, {'math': 10, 'history': 89, 'literature': 81})
# b.av
# v = Student('Joe', 'BArker', 8, {'math': 0, 'history': 0, 'literature': 0})
# v.av
        
# def rating(*args):
#     a = sorted(list(args), key=lambda x: x.average)
#     return a

# print(rating(v, b, a))

"""
5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""
# class Word(str):
#     def __new__(cls, *args, **kwargs):
#         stroka = args[0].replace(' ', '')
#         instance = super().__new__(cls)
#         instance.stroka = stroka

#         return instance

#     def __init__(self, word):
#         self.word = self.stroka

#     def __gt__(self, __value):
#         print(__value)
#         return len(self) > len(__value)

#     def __lt__(self, __value):
#         return len(self) < len(__value)
    
#     def __ge__(self, __value):
#         return len(self) >= len(__value)
        
#     def __le__(self, __value):
#         return len(self) <= len(__value)

# a = Word('qwtryvbubuyuynk')

# b = Word('wejhgksddu')
# print(a.word)
# print(b.word)
# print(a > b)

# class A:
#     def __init__(self, word):
#         print(self)
#         print('----------')

# a = A('sa')

""" # 1) Создайте класс Person и объявите в нем 3 атрибута класса: name (public), phone_number(protected) и сard_number(private), атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999". Создайте объект 'john' класса Person и выведите на экран все атрибуты класса.
 """
# class Person:
#     def __init__(self):
#         self.name = "John"
#         self._phone_number = +996557551757
#         self.__card_number = 9999999999999999

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)
    



""" 
# 2) Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). Создайте экземпляр "john" класса Person со значениями ("John", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты.
 """
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
    
# john = Person('John', +996557551757, 9999999999999999)

# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)



""" # 3) Снова создайте класс Person и объявите в нем 3 атрибута: name (public), phone_number(protected) и сard_number(private), атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999".. Создайте объект "john" класса Person и измените все атрибуты класса на значение None после выведите все атрибуты класса.
 """
# class Person:
#     def __init__(self):
#         self.name = "John"
#         self._phone_number = +996557551757
#         self.__card_number = 9999999999999999

# john = Person()
# john.name = None
# john._phone_number = None
# john._Person__card_number = None

# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)



""" # 4) Продолжая изменять логику предыдущего задания создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации обьекта проверяйте введенные имя. Для этого напишите приватный метод validate_name для валидации имени: данный метод будет проверять длину имени, если длина имени меньше двух то возвращайте имя по дефолту John, если же введенное пользователем имя больше двух, то необходимо возвращать имя с заглавной буквы (JOHN -> John, john -> John и тд). Создайте экземпляр sam класса Person со значениями ("SAM", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты
 """

# class Person:
#     def validate_name(self):
#         if len(self.name) < 2:
#             self.name = "John"
#             return self.name
#         else:
#             self.name = self.name.lower().capitalize()
#             return self.name
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
#         self.validate_name()

# john = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)

    


""" 
# 5) На этот раз заказчик передумал и попросил вас переписать предыдущий класс, теперь его интересует только валидация номера телефона и номера карты. Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации обьекта проверяйте введенный номер телефона и номер карты. Для этого напишите приватный метод validate_phone_number и защищенный метод validate_cart_number.
# Метод validate_phone_number сначала проверяет на то чтобы номер телефона являлся типом int иначе возвращаем None далее нужно также проверять, чтобы номер начинался на 999 иначе возвращается None
# Метод validate_cart_number в первую очередь также проверяет то что бы номер карты являлся типом int иначе возвращаем None далее нужно также проверять что чтобы количество цифр в номере карт была ровно 16 иначе также возвращаем None. Создайте экземпляр 'tolik' класса Person c правильными данными и выведите на экран все его атрибуты
 """

# class Person:
#     def __validate_phone_number(self):
#         if type(self._phone_number) != int or str(self._phone_number)[:3] != '999':
#             self._phone_number = None
        

#     def __validate_cart_number(self):
#         if type(self.__card_number) != int or len(str(self.__card_number)) != 16:
#             self.__card_number = None

#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
#         self.__validate_phone_number()
#         self.__validate_cart_number()

# john = Person("SAM", 999557551757, 9999999299999999)
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)



""" # 6) Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
# Класс Game должен иметь методы для увеличения уровня игры (play) и получения текущего уровня (get_level).
# Метод play принимает в себя переменную hours и проверяет если значение этой переменной больше двух то уровень игры увеличивается на единицу иначе ничего не происходит. Так как атрибут класса "level" приватный и поэтому недоступен извне, необходимо реализовать метод "get_level" который возвращает значение атрибута "level".
# Создайте экземпляр "game" класса Game. Выведите на экран значение атрибута "level" затем два раза используйте метод play чтобы уровень игры поднялся на два, после снова выведите на экран значение атрибута "level".
"""
# class Game:
#     def __init__(self, name):
#         self.__level = 0
#         self.name = name
#     def play(self, hours):
#         if hours > 2:
#             self.__level += 1
    
#     def get_level(self):
#         return f'Твой уровень ---> {self.__level}'

# game = Game('John')
# print(game.get_level())
# game.play(4)
# print(game.get_level())
""" 
# 7) Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
# Класс Game должен иметь два метода: "set_level" и приватный метод "validate_name". 
# При инициализации экземпляра класса вызывается приватный метод validate_name который возвращает имя в котором первая буква в верхнем регистре, а остальные в нижнем (JOHN -> John).
# Также в классе необходимо реализовать метод "set_level" который принимает в себя переменную "level" и увеличивает  значение приватного атрибута класса "level" на значение этой переменной которую передали только в том случае если имя обьекта (который сейчас играет в эту игру) "Tolik", иначе выведите на экран '"имя_обьекта" ты не Tolik!'.
# Создайте сначала экземпляр класса "game" и передайте ему имя Raychel в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом). Теперь создайте экземпляр класса game2 и передайте ему имя "TOLIK" в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом).
# Ожидаемый вывод: 
# Raychel ты не Tolik!
# 0
#
# 5
  """

# class Game:
#     def __validate_name(self):
#         self.name = self.name.lower().capitalize()

#     def set_level(self, level):
#         if self.name == 'Tolik':
#             self.__level = level
#         else:
#             print(f'{self.name} ты не Tolik!')
#     def __init__(self, name):
#         self.name = name
#         self.__level = 0
#         self.__validate_name()
    

# a = Game('Raychel')
# a.set_level(5)
# print(a._Game__level)

# b = Game('TOLIK')
# b.set_level(5)
# print(b._Game__level)




    





""" # 😍 Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю и атрибут экземпляра класса name (ваше имя).
# Так как атрибут класса level приватный и поэтому недоступен извне, необходимо реализовать два метода для работы с ним: get_level и set_level. Где get_level возвращает значение атрибута level и set_level принимает значение и присваивает его атрибуту level. Создайте экземпляр game класса Game. Выведите на экран значение атрибута level затем присвойте ему значение 10 и выведите его на экран.
 """

# class Game:
#     def __init__(self, name):
#         self.name = name
#         self.__level = 0
#     def get_level(self):
#         return self.__level
#     def set_level(self, a):
#         self.__level = a

# game = Game('John')
# print(game.get_level())
# game.set_level(3)
# print(game.get_level())





""" # 9) Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю. Напишите метод level с использование декоратора @property для предоставления доступа к атрибуту level. Создайте экземпляр game класса Game. Выведите на экран значение атрибута level.
 """
# class Game :
#     def __init__(self, name):
#         self.name = name
#         self.__level = 0
#     @property
#     def level(self):
#         return self.__level

# game = Game('John')
# print(game.level)

""" 
# 10) Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю. Напишите метод level с использованием декоратора @setter для того чтобы вы имели право на изменение приватного атрибута класса level вне класса Game. Но обратите внимание что вы не сможете написать этот метод без метода level у которого используется декоратор @property, поэтому также создайте этот метод.
# Создайте экземпляр game класса Game. Выведите на экран значение атрибута level, после 'легально' измените значение level на 10 и снова выведите это значение на экран.
 """

# class Game:
#     __level = 0
#     @property
#     def level(self):
#         print(self.__level)
#     @level.setter
#     def level(self, a):
#         self.__level = a

# game = Game()
# game.level
# game.level = 4
# game.level

    


""" 
# 11) Напишите класса Person, который будет хранить информацию о пользователе. У обьекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email). При инициализации обьекта, передовать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными. Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран. Пример:
# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com
 """
 

# class Person:
#     __name = None
#     __last_name = None
#     __age = None
#     __email = None

#     def get_name(self):
#         print(self.__name)
#     def set_name(self, name):
#         self.__name = name
#     def get_last_name(self):
#         print(self.__last_name)
#     def set_last_name(self, last_name):
#         self.__last_name = last_name
#     def get_age(self):
#         print(self.__age)
#     def set_age(self, age):
#         self.__age = age
#     def get_email(self):
#         print(self.__email)
#     def set_email(self, email):
#         self.__email = email


# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com


# print(john.get_email())



""" # 12) Перепишите предыдущий класс используя декораторы property и setter. Условие: Реализуйте класс Person, который будет хранить информацию о пользователе. У обьекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email). При инициализации обьекта, передовать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными. Поэтому реализуйте для каждого атрибута методы доступа get и set с помощью декораторов которые вы прошли.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран. Пример:
# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

# Согласитесь что этот способ использования декораторы позваоляет писать более понятный и элегантный код
"""

# class Person:
#     __name = None
#     __last_name = None
#     __age = None
#     __email = None
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def last_name(self):
#         return self.__last_name

#     @last_name.setter
#     def last_name(self, last_name):
#         self.__last_name = last_name

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         self.__age = age

#     @property
#     def email(self):
#         return self.__email

#     @email.setter
#     def email(self, email):
#         self.__email = email

# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com
""" 
# 13) Реализуйте класс Dad у которого будут следующие атрибуты класса: name который равен 'John', защищенный атрибут last_name который равен 'Snow' и приватный атрибут age равный 40. Затем реализуйте класс Me: который будет наследоваться от класса Dad и будет содержать атрибуты name равный 'Sam', защищенный атрибут last_name равный фамилии отца и приватный атрибут age равный 10. Также реализуйте 2 метода: about_me который выводит информацию об этом обьекте в виде: 'My name is Sam Snow and I am 10 years old' и about_dad который выводит информацию об этом обьекте в виде: 'My father is John Snow'. (Обратите внимание что в методе about_father мы не выводим атрибут age обьекта отца, как этот атрибут приватный а это значит что он не будет доступен в дочерних классах).
# Создайте экземпляр me класса Me и вызовите методы обьекта (их два).
# Ожидаемый результат: 
# My name is Sam Snow and I am 10 years old
# My father is John Snow """

# class Dad:
#     name = 'John'
#     _last_name = 'Snow'
#     __age = 40

# class Me(Dad):
#     name = 'Sam'
#     _last_name = 'Snow'
#     __age = 10

#     def about_me(self):
#         return f'My name is {self.name} {self._last_name} I am {self.__age} years old'

#     def about_dad(self):
#         return f'My father is {super().name} {self._last_name}'

# me = Me()
# print(me.about_me())
# print(me.about_dad())