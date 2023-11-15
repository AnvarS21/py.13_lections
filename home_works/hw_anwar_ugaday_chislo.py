a = 12
dark_list = ['нурсултан', 'вероника', 'айкена']
name = input('Введите имя: ').lower()

while True:
    if name in dark_list:
        print(f'{name.title()},  ты не являешься студентом, тебе данной программой - игрой пользоваться нельзя!')
        break
        
    elif name not in dark_list and name != '':
        num = int(input('Введите число: '))
        if num == a:
            print('Ура, ты угадал!')
            break
        elif a > num and a - num < 10 or num > a and num - a < 10:
            print('Ты был очень близок!')
        elif a > num and 10 <= a - num < 50 or a < num and 10 <= num - a < 50:
            print('Ты был несовсем далек!')
        else:
            print('Ты очень далеко!')
    if name == '':
        print('Вы не ввели имя!')
        break

        
