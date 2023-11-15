# dict() - словарь -> это упорядоченная коллекция элементов (python 3.7 -> orbered). каждый элемент внутри словаря хранится в виде пары --> {ключ: значение}

# ассоциативный массив, hash table, object(js) == dictionary(python)

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967,
# }
# print(thisdict, type(thisdict))
# print(thisdict['brand'], thisdict['model'])

# thisdict['motor'] = 'v12 Turbo'
# print(thisdict['motor']) # Ошибка
# thisdict['color'] = 'yellow'
# print(thisdict)

#______________________________________________________________________________

# print(dir(dict))
# # items, keys, values
# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
#     'age': 25,


# print(user_info)
# kluchi = user_info.keys()
# print(kluchi, type(kluchi))
# ls = list(kluchi)
# print(ls, ls[0], ls[3:])


# ls = list(user_info.keys())
# print(ls, type(ls))
# print(ls, ls[0], ls[3:])

# elementy = user_info.items()
# print(user_info)
# print(elementy)
# for k, v in user_info.items():
#     print(k, v)

#___________________________________________________

#изменение
# dict_ = {'name': 'Jack', 'age': 17,}
# print(dict_)
# dict_['name'] = 'John'
# dict_['age'] = 24
# print(dict_)
# dict_.update({'name': 'Tirion', 'addres': 'Westeros'})
# print(dict_)


#____________________________________________
# Получение данных со словаря
# get

# dict_ = {1: 'pizza', 2: 'burger', 3: 'streak',}
# print(dict_[3], '!!!') #Error
# print(dict_.get(3)) #None

# setdefault - работает также как и get, но если нет такого ключа то создает новую пару из этого ключа

# dict_ = {1: 'pizza', 2: 'burger', 3: 'streak',}
# print(dict_)
# print(dict_.setdefault(5, 'Manty'))
# print(dict_)
 #________________________________________________________

# fromkeys
# ls = list(range(1, 100))
# print(ls)
# new_dict = dict.fromkeys(ls, 'value')
# print(new_dict)


#______________________________________________________

# удаление элементов
# pop, popitem
# pop(<key>) - удаляет пару по ключу
# dict_ = {'name': 'John', 'lat_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('name')
# print(removed)
# print(dict_)

# popitem - удаляет и позварщает последнюю пару
# dict_ = {'name': 'John', 'lat_name': 'Snow'}
# print(dict_)
# removed = dict_.popitem()
# print(removed)
# print(dict_)


# ________________________________________________

# roles = {
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor'
# }

# product = {
#     'id': 31,
#     'title': 'MackBook Air M1',
#     'description': 'Lorem Ipsum',
#     'price': 900
# }

# users = {
#     16: {'username': 'johnsnow_12', 
#     'password': 'bastard123',
#     'role': roles[1]},
#     34: {'username': 'Tirion', 
#     'password': 'short123',
#     'role': roles[3]},
#     54: {'username': 'serseya', 
#     'password': 'terminator123',
#     'role': roles[2]}
# }

# print(users)
# username = input('Введите свой username: ')
# user_exists = False
# for key, dict_ in users.items():
#     if username == dict_['username']:
#         id = key
#         user_exists = True
       

# if not user_exists:
#     raise ValueError('Username not Found!')

# password = input('Введите свой rassword').lower()
# if users[id]['password'] != password:
#     raise ValueError('Passwords did not match!')

# if users[id]['role'] == roles[1]:
#     product['description'] = input('Введите новое описание:')
# else:
#     raise Exception('You do not have permission!')

# print(product)


