""""
Tasks: 
1) Dollar. 
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в долларизованный формат: 
dollarize(123456.78901) -> "$123,456.80" 
dollarize(-123456.7801) -> "-$123,456.78" 
dollarize(1000000) -> "$1,000,000" 
Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода: init - инициализирует значение атрибута amount 
update - задаёт объекту новое значение amount 
repr - возвращает значение float 
str - метод, который реализует логику функции dollarize() 
//Вывод должен выглядеть следующим образом: 
cash = MoneyFmt(12345678.021) 
print(cash) -- выводит "$12,345,678.02" 
cash.update(100000.4567) 
print(cash) -- выводит "$100,000.46" 
cash.update(-0.3) 
print(cash) -- выводит "-$0.30" 
repr(cash) -- выводит -0.3 
"""
print("ZADACHA --- 1")
def dollarize(number):
    if number > 0:
        number = round(number, 1)

        number = str(number)[::-1]
        
    else:
        number = round(number, 3)
        number = str(number)[::-1]
    last = number[:number.index('.')+1]
    osnova = list(number[number.index('.')+1:])
    
    for i in range(3, len(osnova), 3):
        osnova.insert(i, ',')
    print(osnova)

dollarize(1000000.0)


    

"""
2) Велосипед. 
Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost (стоимость) 
self.make (производитель) 
self.model (модель) 
self.year (год выпуска) 
self.condition (состояние) 
self._sale_price = None (цена для продажи, по умолчанию None) 
self.sold = False (продан или нет, по умолчания False) 
Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод для указания цены для продажи, который принимает цену и если она меньше стоимости, то ставит дефолтную цену для продажи (стоимость + мин. прибыль). 
Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи. При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на
True и возвращает прибыль с продажи. 
Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его атрибутов. 
"""
# class Bike:
#     def __init__(self, cost, make, model, year, condition, _sale_price, sold):

#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = _sale_price
#         self.sold = sold
#         self.min_p = 100
#     def price(self, price):
#         if price < self.cost:
#             self._sale_price = self.cost + self.min_p

    
#     def service(self, repeir_price, op):
#         self._sale_price += repeir_price
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         return self._sale_price - self.cost
#     @classmethod
#     def get_default_bike(cls):
#         return cls(cost = 0, make='Kama', model='Turbo', year=2023, condition='Best', _sale_price=None, sold=False) 

#     def __str__(self):
#         return f'{self.cost}, {self.make}, {self.model}, {self.year}, {self.condition}, {self._sale_price}, {self.sold}, {self.min_p}'

# a = Bike.get_default_bike()
# print(a)
    
"""
3) Герой. 
Разработайте программу по следующему описанию. 
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня. 
В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки. 
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, поднимается уровень. Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
"""
# from random import choice
# class Human:
#     def __init__(self, unic_number, team):
#         self.unic_number = unic_number
#         self.team = team

# class Heroes(Human):
#     level = 0
#     def level_up(self):
#         self.level += 1

# class Sold(Human):
#     def go_heroe(self, a):
#         return f'Следую за героем {a}'

# john = Heroes(999, 'Real')
# jamie = Heroes(888, 'Barca')

# team = ['Real', 'Barca']
# real_sold = []
# barca_sold = []
# ls_soldiers = [Sold(f"{i}", f'{choice(team)}') for i in range(100)]

# for i in ls_soldiers:
#     if i.team == 'Real':
#         real_sold.append(i)
#     else:
#         barca_sold.append(i)

# print(f'Количество солдатов команды Real: {len(real_sold)}')
# print(f'Количество солдатов команды Barca: {len(barca_sold)}')

# if len(real_sold) > len(barca_sold):
#     john.level_up()
#     s = choice(ls_soldiers)
#     s.go_heroe(john)
#     print(f'Уровень поднялся')
#     print(f'Уникальная айдишка героя: {john.unic_number}, Уникальная айдишка солдата: {s.unic_number}')
# elif len(real_sold) < len(barca_sold):
#     jamie.level_up()
#     s = choice(ls_soldiers)
#     s.go_heroe(jamie)
#     print(f'Уровень поднялся')

#     print(f'Уникальная айдишка героя: {jamie.unic_number}, Уникальная айдишка солдата: {s.unic_number}')
   
# else:
#     print('Расходимся, у нас ничья!')


# a = ls_soldiers[1]
# print(a.unic_number)