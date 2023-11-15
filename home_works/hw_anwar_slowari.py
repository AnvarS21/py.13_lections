
# Задача 1

# morza = {'A': ' .- ', 'J': ' .--- ', 'S': ' ... ', '1': ' .---- ',
# 'B': ' -... ', 'K': ' -.- ', 'T': ' - ', '2': ' ..--- ',
# 'C': ' -.-. ', 'L': ' .-.. ', 'U': ' ..- ', '3': ' ...-- ',
# 'D': ' -.. ', 'M': ' -- ', 'V': ' ...- ', '4': ' ….- ',
# 'E': ' . ', 'N': ' -. ', 'W': ' .-- ', '5': ' ….. ',
# 'F': ' ..-. ', 'O': ' --- ', 'X': ' -..- ', '6': ' -…. ', 
# 'G': ' -. ', 'P': ' .--. ', 'Y': ' -.-- ', '7': ' --... ',
# 'H': ' …. ', 'R': ' --.- ', 'Z': ' --.. ', '8': ' ---.. ',
# 'I': ' .. ', 'S': ' .-. ', '0': ' ----- ', '9': ' ----. '}

# b = ''
# a = input('Введите шифруемое слово: ')
# for i in a:
#     i = i.upper()
#     if i in morza.keys():
#         b += morza[i]
#     else:
#         continue
# print(b)


# ______________________________________________________________________________________
# # Задача 2
# import random
# gen = [str(x) for x in range(1, 76) ]
# random.shuffle(gen)
# # print(f'рандомные числа (бочки с числами: {gen}')

# bilet = [str(random.randint(1, 76)) for x in range(15)]
# # print(f'элементы билета: {bilet}')

    

# _____________________________________________________________
# import random

# b = {
#     'B': [2, 3, 4, 5, 6],
#     'I': [7, 8, 9, 10, 11],
#     'N': [23, 45, 32, 21, 12],
#     'G': [22, 20, 24, 25, 26],
#     'O': [35, 36, 37, 38, 39]
# }
# a = list(range(1, 76))
# random.shuffle(a)
# # print(a)
# p = 0
# for h in range(25):
#     c = a[h]
#     for k, v in b.items():
#         for i in v:
#             if c == i:
#                 v[v.index(i)] = 'X'+str(c)+'X'
        
# print(b)


# print(b)

# {
#     'B': [2, 3, 4, 5, 6],
#     'I': [7, 8, 9, 10, 11],
#     'N': [23, 45, 32, 21, 12],
#     'G': [22, 23, 24, 25, 26],
#     'O': [35, 36, 37, 38, 39]

# {
# 'B': ['X2X', 'X3X', 'X4X', 'X5X', 'X6X'], 
# 'I': ['X7X', 'X8X', 'X9X', 'X10X', 'X11X'], 
# 'N': ['X23X', 'X45X', 'X32X', 'X21X', 'X12X'], 
# 'G': ['X22X', 'X20X', 'X24X', 'X25X', 'X26X'], 
# 'O': ['X35X', 'X36X', 'X37X', 'X38X', 'X39X']
# }

import random

b = {
    'B': [2, 3, 4, 5, 6],
    'I': [7, 8, 9, 10, 11],
    'N': [23, 45, 32, 21, 12],
    'G': [22, 20, 24, 25, 26],
    'O': [35, 36, 37, 38, 39]
}
run = [x for x in range(1, 75)]

random.shuffle(run)
# print(b)
boole = True
stolb = []
count = 0
o = 0
s =''
while boole:
    rund = run[0]
    run.remove(rund)
    for k, v in b.items():
        for q in v:
            if q == rund:
                v[v.index(q)] = 'X'  
            if len(set(v)) == 1:
                boole = False
    for i in range(5):
        stolb = [v[i] for v in b.values()]
        if len(set(stolb)) == 1:
                boole = False
    
             
    count += 1   
        
    print(boole)
    print(b)
    print(count)
