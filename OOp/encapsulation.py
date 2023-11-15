                        # Инкапусялиция
# 1) Языковая конструкция которая помогает связать данные с методами для их обработки и управления (свзязь между данными и методами которые пользубтся ими) (класс - капсула)
# 2) Механизм сокрытия, при помощи которого можно ограничить доступ одного компонента программы к другому компоненту

# Инкапусялиция как Механизм сокрытия
# 3 уровня сокрытия данных: 
        # 1. Публичный(public) - number, print_number
        # 2. Защищенный(_protected) - _number
        # 3. Приватный(__private) - __number 
        

# class Car:
#     _country = 'Germany'
#     __motor = 'Turbo diesel'
    
#     def __init__(self):
#         self.marka = 'Mercedec-Benz' # Public
#         self._model = 'w140' # protected
#         self.__color = 'gray' # private

# obj = Car()
# print(dir(obj))
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)


# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         choice = input('Взять трубку (yes/no): ').lower().strip()
#         self._turn_on() if choice == 'yes' else print('Сбросили трубку!')
    
#     def __increment_calls(self):
#         self.__count_of_calls += 1

#     def _turn_on(self):
#         self.__increment_calls()
#         print('Alo!')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

# phone = Phone()
# print(phone.username)
# phone.call()
# phone.call()
# phone.call()
# phone.call()
##------------------------##------------------------##------------------------##------------------------


# class Person:
#     def __init__(self, name, age):
#         self.set_name(name)
#         self.set_age(age)

#     def display_info(self):
#         print(f'My name is {self._name} and I\'m {self._age} years old!')
    
#     def set_name(self, name):
#         if isinstance(name, str):
#             self._name = name 
#         else:
#             try:
#                 self._name
#             except AttributeError:
#                 self._name = None
#             print('Name must be str object')
#     def set_age(self, age):
#         if isinstance(age, int) and 0 < age < 200:
#             self._age = age 
#         else:
#             try:
#                 self._age
#             except AttributeError:
#                 self._age = None
#             print('Age must be int object')
    

# obj = Person(55, 24)
# obj.display_info()
# obj.set_name('Jamie')
# obj.set_age(28)
# obj.display_info()
# obj.set_name(55)
# obj.set_age(-14)
# obj.set_age(None)
# obj.display_info()
##------------------------##------------------------##------------------------##------------------------

# getter & setter
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить логику валидация(проверки) данных которые будут установлены в атрибут и тд

# Аннотация свойтсв (@property(getter setter))

# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__age = None
#     @property # getter
#     def name(self):
#         return self.__name
#     @property # getter
#     def age(self):
#         return self.__age
#     @name.setter
#     def name(self, other):
#         if not isinstance(other, str): print('Name must be str object!')
#         else: self.__name = other
#     @age.setter
#     def age(self, other):
#         if isinstance(other, int) and 0 < other < 200: self.__age = other
#         else: print('Age must be int object!')

            

# obj = Person()
# print(obj.name, obj.age)
# obj.name = 'John'
# obj.age = 24
# print(obj.name, obj.age)
