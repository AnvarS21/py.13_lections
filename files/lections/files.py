# работа с файлами

# Каретка - Указатель - Курсор

# open(<путь до файла>)

# file = open('files.py') #Относительный путь
# ~ working -> Desktop/sf/files/lections/files.py
# files -> lections/files.py
# 
# 
# base_dir = '/Users/anvar/Desktop/sf/files/' 
# file = open(base_dir + 'lections/files.py')

# file = open('files.py')
# data = file.read()
# print(data, type(data))
# file.close()


# Режимы работы с файлами

# 1. r/r+/rb -> read - для чтения файлов
# 2. w/w+/wb -> write - для записи данных
# 3. a/a+ -> для добавления данных
# b, x


# file = open('test.txt', 'r')
# print(file.readline())
# print(file.readline())

# file.close()


# file.tell() - Возвращает индекс где находится Курсор(Указатель)
# file.seek() - Перемещает курсор на индекс который вы передали


# file = open('test.txt', 'r')
# print(file.tell())
# data = file.read()
# print(data)
# print(file.tell())
# file.seek(0)
# print(file.tell())
# print(file.read())
# print(file.tell())
# file.close()


# Контекстный менеджер

# with open('test.txt', 'r') as file: # file = open()
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file.read(), 'outside')


# with open('test.txt', 'w') as file:
#     file.write('Pervaya stroka')
#     file.write('\nHe is bastard of Ned Stark!\n')
#     file.write('This is lection about files!\n')
#     file.seek(0)
#     data = ['Test 1 stroka\n', 'Test 2 stroka\n']
#     file.writelines(data)


# with open('test.txt', 'a+') as f:
#     f.write('\nJohn Snow is King of North\n')
#     f.write('\nYou know nothing John Snow')
#     f.seek(0)
#     print(f.read())


try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re

base_url = '/home/anvar/Desktop/sf/files/lections/'

def get_imei_code(image):
    string = pytesseract.image_to_string(image)
    print(string)
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    print(list_of_imei)

    with open('imei_cods.txt', 'w') as file:
        for x in list_of_imei:
            file.write(f'{x}\n')

image = base_url + 'imei.jpg'
get_imei_code(image)
