""" 
Создайте класс Person
Создайте метод __init__ () и определите внутри него два динамических атрибута: name и birth_year (год рождения). Свои начальные значения они получают из параметров метода __init__ ()
Создайте класс Student (студент), который наследуется от класса Person
Добавьте ему 3 динамических поля (атрибут)
Первое поле course (курс на котором он обучается) должно быть public так как такая информация как должность сотрудника она открытая и не является тайной,
Второе поле notebook (его ноутбук) должно быть экземпляром класса Notebook
Третье поле private называется payments (сумма оплат студента за курсы) и по умолчанию при создании равен пустому списку.
Создать метод do_payment, которое принимает в качестве параметра сумму платежа и добавляет его в payments
Создать метод get_all_payments, которое возвращает сумму всех платежей, сделанных студентом.
Создать метод check_pc которая проверяет ноутбук на соответствие требованиям к программированию. Минимальные требования к ноутбуку должны быть:
Оперативная память 4ГБ и более
Память 120 ГБ и более
Процессор 2 ядра и более
Если ноутбук не подходит хотя бы по одному параметру, то метод должен выдать False, если все три параметра сходятся, то True """

characteristic = {

    'ram': 12,

    'memory': 500,

    'cpu': 4

}
class Notebook:
    def __init__(self, ram=0, memory=0, cpu=0):
        self.ram = int(ram)
        self.memory = int(memory)
        self.cpu = cpu
    def info(self):
        return f'Ноутбук с {self.ram} ГБ оперативной памяти, {self.memory} внутренней памяти и с {self.cpu} ядрами процессора'
    @classmethod
    def add_notebook(cls, dict_):
        return cls(dict_['ram'], dict_['memory'], dict_['cpu'])


acer = Notebook.add_notebook(characteristic)

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

class Student(Person):
    def __init__(self, name, birth_year, course, notebook):
        super().__init__(name, birth_year)
        self.course = course
        if isinstance(notebook, Notebook):
            self.notebook = notebook
        self.__payments = []

    def do_payment(self, sum):
        self.__payments.append(sum)
    def get_all_payments(self):
        return self.__payments
    def check_pc(self):
        ls = [4 <= self.notebook.ram, 120 <= self.notebook.memory, 2 <= self.notebook.cpu]
        return all(ls)

john = Student('John', 2002, 'Python', acer)
john.do_payment(34)
print(john.get_all_payments())
print(john.check_pc())



