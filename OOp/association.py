# Ассоциация - озночает что внутри одного объекта будет существовать другой объект в качетсве атрибута
# 1. Композиция - сильная связь
# 2. Агрегация - слабая связь

# Композиция - это когда стена не существует отдельно от комнаты. Она создается при создании комнаты и полностью управляется классом комнаты
# Агрегация - это когжа экземпляр двигателя создается где то в другом месте, и передается в класс Авто в качетсве параметра


class Battery:
    _power = 100
    def charge(self):
        if self._power < 100:
            self._power = 100
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()# когда мы создаем внутри класса объект от другого класса - композиция
        
a = Iphone('silver')

a.battery.power = 50
print(a.battery.power)
a.battery.charge()
print(a.battery.power)

# del a #При удалении iphone вместе с ним удаляется батарейка



class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery #Когда Объект создается из вне класса и передается внутрь - агрегация

battery = Battery()
nokia1 = Nokia('black', battery)
nokia1.battery.power = 50
print(nokia1.battery.power)
nokia1.battery.charge()
print(nokia1.battery.power)


""" 
# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи. """
from datetime import datetime, timedelta
from time import sleep

class Phone:
    def __init__(self, imei, os):
        self.__imei = imei
        self.__os = os
        self.__battery = 100

    @property
    def battery(self):
        print(f'Уровень баратери: {self.__battery}')

    @property
    def get_info(self):
        if self.__battery < 0.5:
            raise Exception('Телефон зазряжен!')
        print(f'OS: {self.__os}, IMEI: {self.__imei}, battery: {self.__battery}!')
        self.__battery -= 0.5
    
    @property
    def play_music(self):
        if self.__battery < 5:
            raise Exception('Телефон разряжен!')
        print('Слушаем МИрбека Атаюекова')
        self.__battery -= 5

    @property
    def play_video(self):
        if self.__battery < 10:
            raise Exception('Недопустимый уровень заряда!')
        print('Смотрим Топлес и прокачиваем мозги!')
        self.__battery -= 7

    def charge(self, sec):
        # self.__battery += time * 2
        # print('Батарея заряжается....')
        # # print('Батарея зарядилась!')
        # if self.__battery >= 100:
        #     self.__battery = 100
        #     print('Батарея заряжена!')
        now = datetime.now #11:57:20
        end = (now() + timedelta(seconds=sec)).strftime('%H:%M:%S')
        while now().strftime('%H:%M:%S') != end:
            # print(now().strftime('%H:%M:%S'))
            sleep(1)
            print(f'Идет зарядка батаери! Ваш уровень батареи: {self.__battery}!')

            if self.__battery < 100:
                self.__battery += 1
                if self.__battery > 100:
                    self.__battery = 100
                    print('Батарея полностью заряжена!')
                    
                    break


phone = Phone('777', 'iOS 16')

phone.battery
phone.battery
phone.get_info
phone.battery
phone.play_music
# phone.play_music
# phone.play_music
# phone.play_music
# phone.play_music
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
phone.battery


phone.charge(20)