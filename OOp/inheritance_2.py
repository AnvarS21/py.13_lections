# Множественное наследование - это когда класс наследуется от двух или более классов, порядок наследования определяется при помощи MRO

# class Plane:
#     def play_music(self):
#         print('Музыка у нас играет')
#     def fly(self):
#         print('Мы с вами летаем')
    
# class Car:
#     def play_music(self):
#         print('Музыка играет на радио')
# class Auto(Car):
#     def ride(self):
#         print('Едем на вершину')

# class Boat:
#     def play_music(self):
#         print('Музыка играет на караоке')
#     def swim(self):
#         print('Мы с вами плывем в океане')
    
# class FutureAuto(Auto, Boat, Plane):
#     pass

# obj = FutureAuto()
# obj.fly()
# obj.swim()

# obj.ride()

# obj.play_music()




#---------------------------#---------------------------#---------------------------#---------------------------#---------------------------]
object
print(object)
print(dir(object))
h = input()
class A:
    pass

print(issubclass(A, object))


#---------------------------#---------------------------#---------------------------#---------------------------#---------------------------]

# Проблема ромба - когда поиск шел в родительский класс прежде чем искать у соседнего общего потомка (решена при помощи MRO)
# MRO(Metod resolution order) - механизм для корректного поиска родительских методов. Поиск идет таким образом, что если у родительских классов есть общий  предок то поиск идет в ширину, другими словами сначала у потомков а потом у общего предка


# class Zero:
#     def say(self):
#         print('class Zero!')
# class First(Zero):
#     def say(self):
#         print('class First!')

# class Second(Zero):
#     def say(self):
#         print('class Second!')

# class Myclass(First, Second):
#     pass

# obj = Myclass()
# obj.say()

#---------------------------#---------------------------#---------------------------#---------------------------#---------------------------]


# Проблема перекрестного наследования

# class X:
#     pass
# class Y:
#     pass
# class A(Y, X):
#     pass
# class B(X, Y):
#     pass
# class MyMRO(type):
#     def mro(cls):
#         return [cls, A, B, X, Y, object]
# class MyClass(A, B, metaclass=MyMRO):
#     pass

# print(MyClass.mro())



