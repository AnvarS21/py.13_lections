# OOP - object oriented programming
# Целью создания было связать с функциями которые управляют этими данными

# класс - это описание того, как должен выглядеть объект, то есть в классах мы записываем какими данными и функциями будет обладать объект


# Объект - сущность которую мы создаем от класса, у каждого объекта есть собственные данные

# аттрибуты - обычные переменные внутри класса

# методы - функции внутри класса


# __________________________________________________________________________________________________________________________

# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Cirizenship: {self.citizen}'

# john = Human('John', 'Snow', 'King of North', 'Northener')
# james = Human('James', 'Kirk', 'programmer', 'USA')

# print(john.show_info())
# print(james.show_info())
# john.age = 24
# james.age = 19
# john.job = 'King of Westeros'
# print(""" 

#  """)
# print(john.show_info())
# print(james.show_info())


# ===================================================================================================================================================================================


# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name, color) -> None:
#         """ Инициализатор, именно здесь создаются атрибуты объекта """
#         # self - ссылка на объект который только что создался
#         # аттрибы объекта
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')


# rex = Dog('Rex', 'Black')
# pluto = Dog(color='brown', name='Pluto')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()



# rex.age = 2
# pluto.age = 7
# aktosh.age = 1
# aktosh.ushi = False

# rex.bark()
# pluto.bark()
# aktosh.bark()



# rex.show_info()
# pluto.show_info()
# aktosh.show_info()





# ===========================================================================================================================================================================================================================================================================

# class Human:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.golod = 100

#     def walk(self):
#         print(f'{self.name} walking around!')
#         self.golod += 30

#     def work(self):
#         print(f'{self.name} rabotu rabotaet!')
#         self.golod += 50

#     def eat(self, meal, finish=True):
#         print(f'{self.name} покушала')
#         self.golod -= 60 if finish else 30

#     def info(self):
#         print(f'{self.name} --> {self.golod}')


# obj = Human('Raychel')
# obj.info()
# obj.eat('kruassan')
# obj.eat('Sandwich', finish=False)
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat('Burger')
# obj.eat('Fried Potatoe', finish=False)
# obj.info()
# ===============================================================================================================================================


# class Car:
#     def __init__(self, brand, model, color) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color

#     def show_info(self):
#         return f'{self.brand} {self.model} --> {self.color}'
#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} --> {self.color}'
        

# obj = Car('Chevrolet', 'Impala', 'Black')
# obj2 = Car('Kia', 'K8', 'White')
# obj3 = Car('Toyota', 'Avalon', 'Gray')

# # print(obj.show_info())
# # print(obj2.show_info())
# # print(obj3.show_info())

# print(obj)
# print(obj2)

# print(obj3)




# +=========================================
# +=========================================
# +=========================================
# +=========================================







# import random
# class Sniper:
#     health = 100
#     def __init__(self, name) -> None:
#         self.name = name
#     def shoot(self, other: 'Sniper'):
#         other.health -= 20
#         print(f'Атаковал{self}, у {other} осталось {other.health}!')
#     def __str__(self) -> str:
#         return f'{self.name}'

# sniper1 = Sniper('John Wick')
# sniper2 = Sniper('James Bond')

# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper1.shoot(sniper2) if choice == 1 else sniper2.shoot(sniper1)

# print(f'{sniper1 if sniper1.health else sniper2} won the game!')
