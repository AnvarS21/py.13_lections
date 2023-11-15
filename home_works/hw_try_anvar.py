                             # Задача № 1
def chek_passw(a):
    t = 0
    sym = '!@#$%^&*()_-+=<>?/'
    zaglav = False
    stroch = False
    num = False
    symbol = False
    for i in a:
        if i.isupper():
            zaglav = True
        if i.islower():
            stroch = True
        if i.isdigit():
            num = True
        if i in sym:
            symbol = True

    try:
        if len(a) < 8:
            raise print('Пароль должен быть не менее 8 символов')
        elif zaglav == False:
            raise print('Пароль должен содержать хотя бы одну заглавную букву')
        elif stroch == False:
            raise print('Пароль должее содержать хотя бы одну строчную букву')
        elif num == False:
            raise print('Парлль должен содержать хотябы одну цифру')
        elif symbol == False:
            raise print('Пароль должен содержать хотя бы один символ')
    except Exception:
        print
    else:
        t += 1
        # print(t)
        return t
        
chek_passw('jdnksfszQdzs2_')


                            
                             # Задача №2

# list_ = [1, 2, 7, 6, 9, 0]


# try:
#     print(list_[10])
# except IndexError:
#     print('Такого индекса не существует!')



# try:
#     list_.index(23)
# except ValueError:
#     print('Такого элемента в списке нет!')


# try:
#     print(list_[0] / list_[-1])
# except ZeroDivisionError:
#     print('На ноль делить нельзя')


                                # Задача №3

# dict_ = {'Ваня': 14, 'Степа': '21 год', 'Юра': 18, 'Архангел': 20}
# try:
#     key = input('Введите имя школьника: ')
#     key = key.title()
#     print(f'ему {dict_[key]} лет')
# except KeyError:
#      print('В базе нет школьника!')


