# # 1

# a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
# b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]
# c = []
# negative_list = []
# p1 = []
# for i in a:
#     if i in b:
#         c.append(i)

# print(f'Похожие числа: {c}')
# for x in c:
#     if x < 0:
#         c.remove(x)
#         negative_list.append(x)
# print(f'Отрицательные числа в списке с: {negative_list}')
# for p in negative_list:
#     p1.append(abs(p))
# print(f'Перевод отрицательного в абсолютное: {p1}')
# c_start = c[0]
# c_end = c[-1]
# print(f'Результат возведения первого элемента в общем списке: {c_start ** 3}')
# print(f'Результат возведения последнего элемента в общем списке: {c_end ** 3}')

# 2
# Banknote = ['Абдылас Малдыбаев', 'Бубусара Бейшеналиева', 'Касым Тыныстанов', 'Тоголок Молдо', 'Курманджан Датка', 'Бенджамин Франклин']
# for i in Banknote:
#     if i == 'Бенджамин Франклин':
#         Banknote[Banknote.index(i)] = 'Токтогул Сатылганов'
# Banknote.append('Алыкул Осмонов')
# Banknote.append('Саякбай Каралаев')
# Banknote.append('Жусуп Баласагын')

# a = int(input('Введите номинал банкноты сом : '))
# if a == 1:
#     print(Banknote[0])
# elif a == 5:
#     print(Banknote[1])
# elif a == 10:
#     print(Banknote[2])
# elif a == 20:
#     print(Banknote[3])
# elif a == 50:
#     print(Banknote[4])
# elif a == 100:
#     print(Banknote[5])
# elif a == 200:
#     print(Banknote[6])
# elif a == 500:
#     print(Banknote[7])
# elif a == 1000:
#     print(Banknote[8])
# else:
#     print('Ошибка! Такой банкноты не существует')


# 3
# a = int(input('Введите день недели: '))
# b = int(input('Сколько часов вы отраработали: '))

# if a == 1:
#     print('Сегодня Понедельник')
#     if b < 8:
#         print(f'Осталось работать: {8 -b} часа')
# elif a == 2:
#     print('Сегодня Вторник')
#     print(f'Осталось работать: {8 -b} часа')
# elif a == 3:
#     print('Сегодня Среда')
#     print(f'Осталось работать: {8 -b} часа')
# elif a == 4:
#     print('Сегодня Четверг')
#     print(f'Осталось работать: {8 -b} часа')
# elif a == 5:
#     print('Сегодня Пятница')
#     if b > 5:
#         print(f'Осталось работать: {8 -b} часа')
#         print('Можно уйти пораньше!')
#     elif b < 5:
#         print(f'Осталось работать: {8 -b} часа')
# elif a == 6:
#     print('Сегодня Суббота')
#     print(f'Осталось работать: {8 -b} часа')
# elif a == 7:
#     print('Сегодня Воскресенье')
#     print(f'Осталось работать: {8 -b} часа')
# else:
#     print('Ошибка')


# 4
# a = int(input('Введите число: '))
# if 9 < a < 100:
#     print(f'Число {a} двузначное!')
# else:
#     print(f'Число {a} не двузначное!')


# 5
# bad = 'Плохо. Марш учиться!'
# good = 'Молодец! можешь отдохнуть'
# rating = int(input('Что получил по математике? '))
# if rating == 2 or rating == 3:
#     print(bad)
# elif rating == 4 or rating == 5:
#     print(good)

    
# 6
count = 0
chet = []
nechet = []
list_ = [1, '2', 3, 4, '5', 'шесть', 'семь']
for i in list_:
    if i == '2':
        list_[list_.index(i)] = 2
    if i == '5':
        list_[list_.index(i)] = 5
    if i == 'шесть':   
        list_[list_.index(i)] = 6
    if i == 'семь':   
        list_[list_.index(i)] = 7
print(f'готовый список: {list_}')

for u in list_:
    count += u
    if u % 2 == 0:
        chet.append(u)
    elif u % 2 != 0:
        nechet.append(u)
    
print(f'Сумма всех элементов списка: {count} \nСписок с нечетными элементами: {nechet} \nСписок с четными элементами: {chet}')



