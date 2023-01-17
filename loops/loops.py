# Циклы - это конструкция при помощи которых можно организовать многократное исполнение определенного кода
# while <expression>:
#     <body>
# <else:>
#     <body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз!')
#     i += 1
# else:
#     print('Конец цикла!')

# print('Нфчало кода ')

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' and name2.lower() != 'Jamie':
#     name1 = input('Введите имя:')
#     name2 = input('Введите второе имя:')
#     i += 1 
#     if i > 4:
#         print('цикл остановлен')
#         break
# else:
#     print('Вы ввели правильное имя!')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None

# while username != admin[0] or password  != admin[1]:
#     username = input('Введите ussername:')
#     password = input('Введите password:')
#     i -= 1
#     if i == 0:
#         print('Вы заблокированы на 5 минут!')
#         break
# else:
#     print(f'{admin[0]} Вы успешно зашли в систему!')

# ----------------------------------------------------------------------------------------

# for <variable> in <iterable object>:
#     <body>
# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for x in list_:
#     print(x)
# ------------------------------------------------------------------------------------------
# Пример вытаскивания индекс элемента из списка используя While / For
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# # for x in ls:
# #     print(f'Elemnt: {x}')

# i = 0
# while i < len(ls):
#     print(f'Elemnt: {ls[i]}')
#     i += 1
# ---------------------------------------------------------------------------------------------

# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('Введите секретный код:')

# while word not in secret_list:
#     print('Incorrect word! Try one more time!')
#     word = input('Введите секретный код:')
# print(f"You're welcome, my dear friend! {word}")
# ----------------------------------------------------------------------------------------------

