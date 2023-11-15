
'''
1. Создайте класс, который регистрирует пользователя. Пользователь вводит свою почту, пароль и подтверждение пароля, класс валидирует данные, то есть проверяет совпадает ли пароль с подтверждением пароля, если проверка прошла, то класс регистрирует пользователя и выводит сообщение, в котором оповещает пользователя о регистрации, а также выводит его почту. Также в классе есть метод, который может логинить пользователя, то есть после регистрации, пользователь может залогиниться, метод должен проверить, регистрировался ли пользователь ранее, если такой пользователь регистрировался, залогинить его, если нет, вывести сообщение об этом.
'''

# class Registr:
#     users = []
#     def __init__(self, email, password, chek_password):
#         self.email = email
#         self.password = password.lower()
#         self.chek_password = chek_password.lower()
    
#         validate_password = all([
#             len(self.password) > 7, 
#             len([i for i in self.password if i in 'qwertyuiopasdfghjklzxcvbnm']) > 0, 
#             len([i for i in self.password if i in '1234567890']) > 0, 
#             len([i for i in self.password if i in '!@#$%^&*()_+']) > 0
#         ])

#         validate_email = any([
#             self.email.endswith('@gmail.com'),
#             self.email.endswith('@gmail.ru'),
#             self.email.endswith('@gmail.kg')
#         ])

#         if validate_email == False:
#             raise Exception('Почта должна иметь префикс --> @gmail.com/ru/kg')
#         elif validate_password == False:
#             raise Exception('Пароль не совпадает требованиям!')
#         elif self.password != self.chek_password:
#             raise Exception('Пароли не совпадают!')
#         else:
#             self.users.append({'Login': self.email, 'Password': self.password})
#             print(f'Вы успешно зарегистрировались!\nВаша почта: {self.email}')
    
#     def login(self, login, password):
#         if {'Login': login, 'Password': password} in self.users:
#             print('Вы успешно залогинились!')
#         else:
#             print('Логин или пароль не правильный!')


        
# a = Registr('asdsd0@gmail.kg', 'asdasad7)', 'asdasad7)')
# a.login('asdsd0@gmail.kg', 'asdasad7)')

"""
2.Создайте класс PrivateProject. Внутри этого класса есть атрибуты класса: github_link и developers.
В github_link хранится ссылка на проект (любая), а в developers хранится список с юзернеймами, у которых есть доступ к этой ссылке (атрибуту github_link).
Создайте объект класса PrivateProject, при создании необходимо передать в качестве аргумента username.
Далее, попытайтесь через созданный объект класса получить атрибут github_link. При этом, если данный username есть в списке developers, ему открыт доступ к ссылке.
В противном случае выводится сообщение: Forbidden. Список developers должен быть скрыт.
"""
# class PrivateProject:
#     def __init__(self, username):
#         self.__github_link = 'https://proglib.io/p/40-proektov-na-python-dlya-novichkov-i-prodvinutyh-razrabotchikov-2022-05-13'
#         self.__developers = ['anvar', 'altai', 'marlen', 'kanybek', 'adilet']
#         self.username = username
#     def get_github_link(self):
#         if self.username.lower() in self.__developers:

#             return f'Ссылка: {self.__github_link}'
#         else:
#             return 'Forbidden'

# a = PrivateProject('anvar')
# print(a.get_github_link())

"""
3.Создайте класс User. В этом классе есть защищенный метод _create_user, который принимает email и password. Этот метод вызывается в публичных методах create_user и create_superuser. Оба метода отличаются друг от друга тем, что в методе create_user атрибут is_superuser имеет значение False, а в методе create_superuser - True.
Также в классе есть метод admin_login, который принимает password.
Создайте два объекта от класса User. К первому объекту примените метод create_superuser, а ко второму - create_user. Далее у обоих объектов вызовите метод admin_login, передав правильные пароли.
У первого объекта должно выдаваться сообщение Successfully logged in, а у второго - Forbidden, так как поле is_superuser у второго объекта имеет значение False. Также если даже is_superuser у первого объекта True, ему не удасться залогиниться, если он передал неправильный пароль password в метод admin_login и ему выдается сообщение: Invalid password.
"""
# class User:
    
#     def _create_user(self, email, password):
#         self.password = password
#         self.email = email

#     def create_superuser(self, email, password):
#         is_superuser = True
#         self._create_user(email, password)

#     def create_user(self, email, password):
#         self._create_user(email, password)
#         is_superuser = False

#     def admin_login(self, password):
#         if password == self.password:
#             return '!!!'
#         else:
#             raise Exception('Вы не админ!')
        

# a = User()
# b = User()
# a.create_superuser('anvar@gmail.com', 'qwerty123')
# b.create_user('anvar@gmail.com', 'qwerty123')
# print(a.admin_login('qwerty123'))
'''
4. Создайте программу, которая запрашивает у пользователя 2 ввода данных, 1-й: количество элементов в списке, 2-й: сами элементы списка, разделенные пробелом. Если количество введенных данных превышает количество элементов указанных в первом вводе, необходимо сгенерировать ошибку. Если все данные сходятся, тогда необходимо суммировать все элементы списка и вывести в терминал.
'''
# def check():
#     try:
#         count = int(input())
#         ls = input().split()
#         if len(ls) == count:
#             return sum([int(i) for i in ls])
#         else:
#             raise Exception('Не сходится!')
#     except ValueError:
#         return 'Вводите только цифры'
# print(check())
