# vis = ("                                    ________________________")
# tru = ("                                   ||        |           ||")
# tru2 = ("                                   ||        |__         ||")
# gol = ('                                   ||       (-_-)        ||')
# ruk = ("                                   ||      /|  |\        ||")
# tors = ('                                   ||     / |__|  \      ||')
# nog = ('                                   ||       |  |         ||')
# nog2 = ("                                   ||       |_ |_        ||")
# word = input('Enter word: ')
# word = word.lower()
# word = list(word)
# b = len(word) * '*'
# b = list(b)
# u = 0
# f = None
# while True:
#     if '*' not in b:
#         print('''
#                 Вы выиграли!
#         ''')
#         break
#     a = input('Enter letter: ')
#     a = a.lower()
#     if a not in word and u == 0:
#         print(vis)
#         u += 1
#     elif a not in word and u == 1:
#         print(tru)
#         u += 1
#     elif a not in word and u == 2:
#         print(tru2)
#         u += 1
#     elif a not in word and u == 3:
#         print(gol)
#         u += 1
#     elif a not in word and u == 4:
#         print(ruk)
#         u += 1
#     elif a not in word and u == 5:
#         print(tors)
#         u += 1
#     elif a not in word and u == 6:
#         print(nog)
#         u += 1
#     elif a not in word and u == 7:
#         print(nog2)
#         u += 1
#         print('''     
#                     Человечек умер;( Вы проиграли!
#                     ''')
#         break
#     elif a in word:
#         b[word.index(a)] = a
#     for i in range(len(word)):
#         if word[i] == a:
#             f = i
#             b[f] = a

    
#     print(b)



# vis = ("""                          ________________________""", """                                                                        ||        |           ||""", """                                                                        ||        |           ||""", """                                                                        ||        |__         ||""", """                                                                        ||       (-_-)        ||""", """                                                                        ||      /|  |\       ||""",     """                                                                        ||     / |__|  \      ||""", """                                                                       ||       |  |         ||""", """                          ||       |_ |_        ||""")

# word = input('Enter word: ')
# word = word.lower()
# word = list(word)
# b = len(word) * '*'
# b = list(b)
# u = 0
# f = None
# while True:
#     if '*' not in b:
#         print('''
#                 Вы выиграли!
#         ''')
#         break
#     a = input('Enter letter: ')
#     a = a.lower()
#     if a not in word and u == 0:
#         print(vis[0])
#         u += 1
#     elif a not in word and u == 1:
#         print(vis[:2])
#         u += 1
#     elif a not in word and u == 2:
#         print(vis[:3])
#         u += 1
#     elif a not in word and u == 3:
#         print(vis[:4])
#         u += 1
#     elif a not in word and u == 4:
#         print(vis[:5])
#         u += 1
#     elif a not in word and u == 5:
#         print(vis[:6])
#         u += 1
#     elif a not in word and u == 6:
#         print(vis[:7])
#         u += 1
#     elif a not in word and u == 7:
#         print(vis[:8])
#         u += 1
#         print('''     
#                     Человечек умер;( Вы проиграли!
#                     ''')
#         break
#     elif a in word:
#         b[word.index(a)] = a
#     for i in range(len(word)):
#         if word[i] == a:
#             f = i
#             b[f] = a

    
#     print(b)


vis = (
    """________________________""", 
    """________________________
    ||        |           ||""", 
    """
    ________________________
    ||        |           ||
    ||        |           ||""", 
    """
    ________________________
    ||        |           ||
    ||        |           ||""",
    """, 
    """||       (-_-)        ||""", 
    """||      /|  |\        ||""",     
    """||     / |__|  \      ||""", 
    """||       |  |         ||""", 
    """||       |_ |_        ||""")

HANGMAN = (
    """
    ------
    ||
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    ||
    |O|
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    ||
    |O|
    |-+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    ||
    |O|
    |/-+-/
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    ||
    |O|
    |/-+-/
    ||
    |
    |
    |
    |
    --------
    """,
    """
    ------
    ||
    |O|
    |/-+-/
    ||
    ||
    ||
    ||
    |
    --------
    """,
    """
    ------
    ||
    |O|
    |/-+-/
    ||
    ||
    |||
    |||
    |
    --------
    """,
)

word = input('Enter word: ')
word = word.lower()
word = list(word)
b = len(word) * '*'
b = list(b)
u = 0
f = None
while True:
    if '*' not in b:
        print('''
                Вы выиграли!
        ''')
        break
    a = input('Enter letter: ')
    a = a.lower()
    if a not in word and u == 0:
        print(vis[0])
        u += 1
    elif a not in word and u == 1:
        print(vis[:2])
        u += 1
    elif a not in word and u == 2:
        print(vis[:3])
        u += 1
    elif a not in word and u == 3:
        print(vis[:4])
        u += 1
    elif a not in word and u == 4:
        print(vis[:5])
        u += 1
    elif a not in word and u == 5:
        print(vis[:6])
        u += 1
    elif a not in word and u == 6:
        print(vis[:7])
        u += 1
    elif a not in word and u == 7:
        print(vis[:8])
        u += 1
        print('''     
                    Человечек умер;( Вы проиграли!
                    ''')
        break # hello
    elif a in word:
        b[word.index(a)] = a
    for i in range(len(word)):
        if word[i] == a:
            f = i
            b[f] = a

    
    print(b)