""" Создайте класс, сохраняющий каждый экземпляр в переменную класса all_contacts = [ ]. В инициализаторе класса должны быть параметры name, lastname, phone_number. Подсказка: подумайте о self.

Создайте субкласс Friend, у которого должен быть метод play_football_with_me()

Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя, и возвращать список всех совпадений. Замените all_contacts = [ ] на all_contacts = ContactList(). Создайте несколько контактов, используйте метод search_by_name. """

# class A:
#     all_contacts = []
#     def __init__(self, name, lastname, phone_number):
#         self.name = name
#         self.lastname = lastname
#         self.phone_number = phone_number
#         self.all_contacts.append(self)

# a = A('John', 'Snow', 999)
# b = A('Jamie', 'Lanister', 998)

# # print(b.all_contacts[1].name)

# class Friend(A):
#     def play_football_with_me(self):
#         return 'Я играю в футбол'

# class ContactList(list):
#     sovpadenia = []
#     def __init__(self, *a):
#         self.all_contacts = [*a]

#     def search_by_name(self, name):
#         for i in self.all_contacts:
#             if i == name:
#                 self.sovpadenia.append(i)
#         print('Список совпадений: ')
#         return list(set(self.sovpadenia))

# a = ContactList('Адилет', 'dfs', 'Адилет')
# # print(a.all_contacts)
# print(a.search_by_name('ыаыв'))

    
    
            



""" Реализуйте родительский класс Publication, конструктор которого принимает name, date, pages, library, type
Создайте субкласс Book. В конструктор родительского класса должен передавать type=’book’
Создайте субкласс Magazine. В конструктор родительского класса должен передавать type=’magazine’
Создайте субкласс Newspaper. В конструктор родительского класса должен передавать type=’newspaper’
В классе Publication создайте метод get_code_in_library() который будет возвращать первые_2_буквы_библиотеки_тип_первые_2_буквы_названия_количество_страниц_дата_без_точек """


# class Publication:
#     def __init__(self, name, date, pages, library, type):
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.type = type
#     def get_code_in_library(self):
#         return f'{self.library[:2]},{self.type}, {self.name[:2]}, {self.pages}, {self.date}'

# class Book(Publication):
#     def __init__(self, name, date, pages, library):
#         self.type = 'book'
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library

# class Magazine(Publication):
#     def __init__(self, name, date, pages, library):
#         self.type = 'magazine'

# class Newspaper(Publication):
#     def __init__(self, name, date, pages, library):
#         self.type = 'newspaper'
# book = Book('Властелин колец', 2002, 604, 'Национальная')
# print(book.type)
# print(book.get_code_in_library())

""" Создайте класс Weight (Вес).
        Создайте метод init() и определите внутри него три динамических атрибута: gram (граммы, целочисленное значение), kilogram (килограммы, целочисленное значение) и centner (центнер, целочисленное значение) . Свои начальные значения они получают из параметров метода init (). Если не указывать значения gram и kilogram, то по умолчанию их значение равна 0.
        Напишите магический метод str () в котором будет возвращаться информация: «Вес .. центнеров, .. кг, .. гр».
        Напишите методы прибавления add и убавления sub для данного класса
        Напишите методы сравнения двух экземпляров класса (eq, gt, le и т.д.)
    Создайте отдельный файл для проверки класса Weight. В данном файле проверьте:
        Результат прибавления одного экземпляра класса на другой
        Результат убавления одного экземпляра класса от другой
        И все сравнения двух экземпляров класса (eq, gt, le и т.д.) """

# class Weight:
#     def __init__(self,  centner,  kilogram=0, gram=0):
#         self.gram = gram
#         self.kilogram = kilogram
#         self.centner = centner

#     def __sub__(self, other):
#         return f'{self.gram - other.gram} грамм, {self.kilogram - other.kilogram} килограмм, {self.centner - other.centner} центнеров'
#     def __add__(self, other):
#         return f'{self.gram + other.gram} грамм, {self.kilogram + other.kilogram} килограмм, {self.centner + other.centner} центнеров'
#     def __eq__(self, other):
#         a = f'{self.centner}{self.kilogram}{self.gram}'
#         b = f'{other.centner}{other.kilogram}{other.gram}'
#         if int(a) == int(b):
#             return True
#         else:
#             return False
#     def __gt__(self, other):
#         a = f'{self.centner}{self.kilogram}{self.gram}'
#         b = f'{other.centner}{other.kilogram}{other.gram}'
#         if int(a) > int(b):
#             return True
#         else:
#             return False
       
#     def __le__(self, other):
#         a = f'{self.centner}{self.kilogram}{self.gram}'
#         b = f'{other.centner}{other.kilogram}{other.gram}'
#         if int(a) <= int(b):
#             return True
#         else:
#             return False
#     def __lt__(self, other):
#         a = f'{self.centner}{self.kilogram}{self.gram}'
#         b = f'{other.centner}{other.kilogram}{other.gram}'
#         if int(a) < int(b):
#             return True
#         else:
#             return False
#     def __ne__(self, other):
#         a = f'{self.centner}{self.kilogram}{self.gram}'
#         b = f'{other.centner}{other.kilogram}{other.gram}'
#         if int(a) != int(b):
#             return True
#         else:
#             return False
#     def __ge__(self, other):
#         a = f'{self.centner}{self.kilogram}{self.gram}'
#         b = f'{other.centner}{other.kilogram}{other.gram}'
#         if int(a) >= int(b):
#             return True
#         else:
#             return False

#     def __str__(self):
#         return f'Вес: {self.centner} центнеров, {self.kilogram} кг, {self.gram} гр'
    
# a = Weight(2, 2, 2)
# b = Weight(2, 2, 2)
# print(a != b)