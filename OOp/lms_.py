""" 
Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .

Добавьте атрибут horsepower, который равен 85.

Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.
#  """

class Car:
    horsepower = 85
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
    def add_horsepower(self, horsepower=horsepower):
        if self.brand.lower() == 'mers' or self.brand.lower() == 'bmw' or self.brand.lower() == 'porshe':
            self.horsepower += 40
        else:
            self.horsepower += 20
        return f'Horspower: {self.horsepower}'
        

    def get_auto(self):
        return f'Car: {self.brand}, year: {self.year}, color: {self.color}'
    def get_year(self):
        return f'This car is {2023 - self.year} years old'
    



bmw = Car('mers', 2002, 'red')
print(bmw.get_auto())
print(bmw.add_horsepower())


tractor = Car('tractor', 2002, 'black')
print(tractor.get_auto())
print(tractor.add_horsepower())

""" 
Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto
"""

# mers = Car('mers', 2016, 'purple')
# print(copy1.get_auto())

# wolks = Car('Wolkswagen', 2023, 'white')
# print(copy2.get_auto())



""" 
Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента. """

# class Student:
#     def __init__(self, name: str, age: int, course: str):
#         self.name = name
#         self.age = age
#         self.course = course
#     def get_student(self):
#         return f'Студент {self.name} учится в {self.course}. Ему {self.age} от роду'
#     def get_birth_year(self):
#         return f'Он родился в {2023 - self.age} году!'

# aidar = Student('Айдар', 21, 'Кодифай')
# print(aidar.get_student())
# print(aidar.get_birth_year())

# print(""" 

#  """)

# Saule = Student('Сауле', 21, 'Мейкерс')
# print(Saule.get_student())
# print(Saule.get_birth_year())


