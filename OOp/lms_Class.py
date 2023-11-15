
"""
1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
"""
# class Class1:
#     def print_p1(self):
#         print('Привет!')
#     def print_p2(self):
#         print('Как твои дела?')

# class Class2(Class1):
#     def print_p1(self):
#         super().print_p1()
#         print('У меня все отлично')
#     def print_p2(self):
#         super().print_p2()
#         print('Я иду на учебу')

# ekzemplyar = Class2()
# ekzemplyar.print_p1()
# ekzemplyar.print_p2()



"""
2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
"""
# class A:
#     def method1(self):
#         print('Основной функционал')
    
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# c = B()
# c.method1()
"""
3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'
"""
# class MyString(str):
#     def __init__(self, str_1):
#         self.str_1 = str_1

#     def append(self, str_2):
#         self.str_1 = self.str_1 + str_2
#         return self.str_1
#     def pop(self):
#         last_al = self.str_1[-1:]
#         self.str_1 = self.str_1[:-1]
#         return last_al

#     def __str__(self):
#         return self.str_1
    


# example = MyString('String')
# example.append('hello')
# print(example)
# print(example.pop())
# print(example)


"""
4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.
"""
# class MyDict(dict):
#     def init_subclass(cls) -> None:
#         return super().init_subclass()

#     def get(self, k):
#         k = super().get(k)
#         if k is None:
#             return 'Are you kidding?'


# a = MyDict(one=1, two=2)
# print(a.get(''))



"""
5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         return f'Имя: {self.name}\nВозраст: {self.age}'

# class Student(Person):
#     def __init__(self, name, age, facult):
#         super().__init__(name, age)
#         self.facult = facult
#     def display_student(self):
#         return f'Имя: {self.name}\nВозраст: {self.age}\nФакультет: {self.facult}'
        
# anvar = Student('Anvar', 21, 'IT Tehnology')
# print(anvar.display_student())


        


"""
6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
"""

# class ContactList(list):
#     def search_by_name(self, name):
#         res = [i.lower() for i in self if i == name.lower()]
#         return res
# all_contacts = ContactList(['Анвар', 'Каныбек', 'Алтайбек', 'Марлен', 'Марлен'])
# print(all_contacts.search_by_name('Марлен'))


""" 
7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию
должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.
У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.
Создайте два дочерних класса от Smartphone - Iphone и Samsung.
У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.
А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.
Создайте объекты от данных классов и примените все методы.

 """

# from datetime import datetime


# class Smartphone:

#     def __init__(self, name, color, memory, battery=0) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery
#     def charge(self, vel):
#         self.battery = self.battery + vel

#     def __str__(self) -> str:
#         return f'Названия: {self.name} память: {self.memory} батарея: {self.battery}'



# class Iphone(Smartphone):
#     def __init__(self, name, color, memory, battery, ios) -> None:
#         super().__init__(name, color, memory, battery)
#         self.ios = ios
#     def send_imessage(self):
#         return 'Привет как твои дела?\nIphone 8+'



# class Samsung(Smartphone):
#     def __init__(self, name, color, memory, battery, android) -> None:
#         super().__init__(name, color, memory, battery)
#         self.android = android
#     def show_time(self):
#         return datetime.now()


# a51 = Samsung('a51', 'red', 128, 3500, 'SnapDragon 555')
# print(a51)
# print(a51.show_time())


""" 
8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.
У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.
Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:
Открытие замков: Alohomora
позволяет магу попасть в любую комнату
способно открыть любую закрытую замочную скважину.
Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы
"""

# class Spell:
    
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula
#     def get_description(self):
#         return f'{self.name} {self.formula}- это очень эффективное заклинание, для убийства гоблинов.Оно сжигает их изнутри'
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self):
#         return f'{self.name}: {self.formula}\nэто очень эффективное заклинание, для убийства гоблинов.Оно сжигает их изнутри'
    

# a = Spell('Убийство', 'Avada Kedavra')
# print(a)
# print(a.execute())
# print(""" 

#  """)
#-------------------##-------------------##-------------------##-------------------##-------------------##-------------------#

# class The_Lord_of_the_Rings(Spell):
#     def __init__(self, name, formula, power):
#         super().__init__(name, formula)
#         self.power = power
#     def get_description(self):
#         return f'Называется: {self.name} \nПроизносится: {self.formula} - заклинание Темного властелина - Саурона, которое подчиняет все кольца!\nЕе мощность {self.power} Сильнее него только заклинание Тулкаса'
    
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self):
#         return f'Называется: {self.name} \nПроизносится: {self.formula} ---> заклинание Темного властелина - Саурона, которое подчиняет все кольца!\nЕе мощность {self.power} Сильнее него только заклинание Тулкаса'

# spell_one = The_Lord_of_the_Rings('Подчинение', 'Гакх назги илид дуруб - ури лата нут.\nКрив Шара - ури матуруз матат думпугаю \nАш туг ШАкхбурз - ур Улима - таб - иши за, \nУзг - Мордор - иши амал фауфут буругли.\nАш назг дурбатулукб аш назг гимбатул, \nАш назг фракатулук, агх бурзум - иши кримпатулю\nУзг - Мордор - иши амал фауфут буруглию', 60)
# print(spell_one)
# print(""" 

#  """)
#-------------------##-------------------##-------------------##-------------------##-------------------##-------------------#


# class HarryPotter(Spell):
#     def __init__(self, name, formula, avtor):
#         super().__init__(name, formula)
#         self.avtor = avtor
#     def get_description(self):
#         return f'{self.name} {self.formula} ---> дает возможность прочитать мысли при прикосновении в человеку \nРазработал его: {self.avtor}'
    
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self):
#         return f'Название: {self.name} \nПроизношение: {self.formula} ---->  дает возможность прочитать мысли при прикосновении в человеку \nРазработал его: {self.avtor}'

# spell_two = HarryPotter('Мыслесос', 'Мысли мысли выходите ко мне в ушки приходите', 'Гвидо Ван Россум')
# print(spell_two)
# print(""" 

#  """)
#-------------------##-------------------##-------------------##-------------------##-------------------##-------------------#
# class AutoCode(Spell):
#     def __init__(self, name, formula, avtor):
#         super().__init__(name, formula)
#         self.avtor = avtor
#     def get_description(self):
#         return f'{self.name} {self.formula} ---> Пишет программный код за вас. Нужно только представить какой проект нужно сделать! \nРазработал его: {self.avtor}'
    
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self):
#         return f'Название: {self.name} \nПроизношение: {self.formula} ---> Пишет программный код за вас. Нужно только представить какой проект нужно сделать! \nРазработал его: {self.avtor}'
    
# spell_three = AutoCode('Магический Код', 'Сode borum vin lasa sopricum', 'Анвар Айтишник')
# print(spell_three)



""" 
9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом
чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.
Создайте исключение от этого класса с сообщением:
"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"
Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:
 Traceback (most recent call last):
  File "inheritance.py", line 121, in <module>
    check_letters(a)
  File "inheritance.py", line 117, in check_letters
    raise capitals_error
main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ
  """
# class CustomError(Exception):
#     def __init__(self, *args):
#         super().__init__(*args)

# error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# # ____________________________________________
# def stroka(a):
#     if a != a.upper():
#         raise error
# stroka('DKoAS')


""" 10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:
power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
Класс должен иметь методы:
give_weapon - выбирает случайное оружие из списка
give_role - выбирает случайную роль из списка, к примеру:
["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:
char1.give_powers('ловкость', 5)
увеличит ловкость вашего героя.
Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,
дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.
"""

# from random import choice
# class Character:
#     role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#     weapon_list = ['Пистолет', 'Автомат', 'Меч', 'Гранотамет', 'Граната', 'Бита', 'Танк', 'Копье', 'Снайпер', 'Лук', 'Базука - РПГ']
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
#     def __init__(self, name):
#         self.name = name
#     def give_weapon(self):
#         weapon = choice(self.weapon_list)
#         return weapon
#     def give_role(self):
#         role = choice(self.role_list)
#         return role
#     def give_powers(self, power, val):
#         self.power_list[power] = val

# ##--------------------------------#--------------------------------#--------------------------------#--------------------------------


# class Elf(Character):
#     magic_skill = ['Бессмертие', 'Читать мысли', 'Регенерация', 'Управление чужим разумом', 'Управление воздухом', 'Управление водой', 'Управление огнем', 'Целительство']
#     def __init__(self, name):
#         super().__init__(name)

#     def skill_(self):
#         skill = choice(self.magic_skill)
#         return skill
#     def __str__(self):
#         return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nУникальный скилл: {self.skill_()}'
    
    
# elf = Elf('Legolas')
# elf.give_powers('мудрость', 200)
# print(elf)
# print(""" 

#  """)
# ##--------------------------------#--------------------------------#--------------------------------#--------------------------------

# class Orc(Character):
#     location = ['Средиземье', 'Мордор', 'Шир', 'Драндуил', 'Темный лес', 'Гондор', 'Мериадок', 'Вонючий носок']
#     def __init__(self, name):
#         super().__init__(name)

#     def local(self):
#         local_ = choice(self.location)
#         return local_

#     def __str__(self):
#             return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nМесто жительства: {self.local()}'
    
# orc = Orc('АзокОсквернитель')
# orc.give_powers('мудрость', 40)
# orc.give_powers('харизма', 90)
# orc.give_powers('интеллект', 2)
# orc.give_powers('сила', 100)
# orc.give_powers('ловкость', 5)
# print(orc)
# print(""" 
#  """)
    
# ##------------------------------#------------------------------#------------------------------#------------------------------


# class DragonBorn(Character):
#     duty = ['Мыть посуду', 'Смотреть за детьми', 'Пылесосить', 'Жена на час', 'Боди массаж']
#     def __init__(self, name):
#         super().__init__(name)
#     def choice_duty(self):
#         duty_ = choice(self.duty)
#         return duty_
#     def __str__(self):
#         return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nОбязанность: {self.choice_duty()}'

# gohan = DragonBorn('Гохан')
# print(gohan)
# print(""" 

#  """)

