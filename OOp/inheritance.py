# Принципы ООП

# 1) Наследование
# 2) Инкапсуляция
# 3) Полиморфизм

# 4) Абстракции
# 5) Ассоциация(композицияю агрегация)
# ----------------------------------------------------------------------
# Наследование
# Позволяет принимать родительские методы и атрибуты дочернему классу

# Родительский класс
# Дочерний класс

# ----------------------------------------------------------------
# ---------------------------------------------------------------
# --------------------------------------------------------------


# class Animal:
#     def print_info(self):
#         print('I\m an Animal!')
# class Lion(Animal):
#     pass
# class Dog(Animal):
#     pass

# simba = Lion()
# simba.print_info()
# # print(dir(simba))
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

# class Animal:
#     def say(self):
#         print(f'this animal name is: {self.name}: {self.golos}')
#     def eat(self):
#         print(f'{self.name} eats: {self.meal}')

# class Lion(Animal):
#     name = 'Lion'
#     golos = 'roar'
#     meal = 'meat'

# class Dog(Animal):
#     name = 'Dog'
#     golos = 'bark'
#     meal = 'home meat'

# class Koala(Animal):
#     name = 'Koala'
#     golos = 'roar'
#     meal = 'efkalit'

# rex = Dog()
# simba = Lion()
# maris = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# print()
# maris.say()
# maris.eat()




# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

class Person:
    def info(self):
        print('I\'m a person from Bishkek!')

class Student(Person):
    def info(self):
        super().info()
        print('I\'m study in Manas University!')

class Adult(Person):
    def info(self):
        super().info()
        print('I\'m older than 18 years! I work 5 days in the week!')

obj1 = Student()
obj2 = Adult()
obj1.info()
print()
obj2.info()


# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------

class Laptop:
    def __init__(self, brand, model, price) -> None:
        self.brand = brand
        self.model = model
        self.price = price
    def get_info(self):
        return {'brand': self.brand, 'model': self.model, 'price': self.price}

class Acer(Laptop):
    def __init__(self, model, price, year, videocard):
        super().__init__('Acer', model, price)
        self.year = year
        self.video = videocard

    def get_info(self):
        repr = super().get_info()
        repr['year'] = self.year
        repr['videcard'] = self.video
        return repr

class Aplle(Laptop):
    def __init__(self, model, price, cpu, display):
        super().__init__('Macbook', model, price)
        self.cpu = cpu
        self.display = display

    def get_info(self):
        repr = super().get_info()
        repr['cpu'] = self.cpu
        repr['display'] = self.display
        return repr

acer = Acer('swift', 700, 2022, 'nvidia')
print(acer.get_info())

mac = Aplle('Air', 1200, 'M2', 13.6)
print(mac.get_info())