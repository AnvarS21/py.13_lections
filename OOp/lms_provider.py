                    # Задача 1
class Subscriber:
    def __init__(self, firstname, lastname):
        self.name = firstname
        self.last = lastname
    def __repr__(self):
        b = self.name + ' ' + self.last
        return b
a = Subscriber('Anvar', 'Shamasutdinov')
c = Subscriber('sdfsdf', 'adsffddsa')



                    # Задача 2
class Provider:
    subscribers = []
    payments = {}
    def __init__(self, name, *subscriber):
        self.name = name
        self.subscribers = [i for i in subscriber]

    def register_payment(self, a, sum):
        if a in self.subscribers:
            self.payments[a] = sum
        else:
            raise ValueError('qwerty')
        return True

b = Provider('Beeline', a)
b1 = Provider('Beeline', a)

                # Задача 3

class Terminal:
    def __init__(self):
        self.amount = 0
        self.providers = []

    def register(self, a):
        if isinstance(a, Provider):
            self.providers.append(a)

    def pay(self, pro, sub, amount):
        if pro.register_payment(sub, amount):
            self.amount += amount

v = Terminal()
v.register(b)
v.register(b1)
v.pay(b, a, 100)
print(v.amount)
print(v.providers)