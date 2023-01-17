# Встроенные Функции 

# lambda() - Анонимная функция. обычные функций с особенностью - у них нет имён. Функция может принимать сколько угодно параметров 
# но всегда возвращает одно выражение. 
# map() -функции высшего порядка
# filter() -функции высшего порядка
# enumerate()
# zip()
# all(), any()

# def hello(): return 'hello'

# print(hello())

# x  = lambda: 'hello'
# print(x())

# x = lambda  a, b, c: (a*b) % c
# print(x(5, 5, 2))

# x = lambda num1, num2, degree = None: (num1 * num2) ** degree if degree else num1 * num2
# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num:  num * n 

# my_doubler  = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(50))
# print(my_doubler(150))
# print(my_doubler(500))
# print(my_tripler(1000))
# print(my_tripler(4000))

# dict_ = {'John': 500, 'Tirion': 170_000, 'Tom': 150, 'Sam': 20, 'Ayana': 100_000} - lambda 

# new_dict = sorted(dict_.items(), key = lambda x: x[1], reverse=True) - сортировка 
# print(dict(new_dict))
# ----------------------------------------------------------------------------------------------------------------------------

# map(function, iterable)-  применяет к аждому элеииентувнутри iterable функции которому мы ей передаем, 
# закидывая в результате те данные которые возврощает функция, в результате мы получаем mapobject(iterator) 
# в котором хранятся все наши данные 

# Например с помощью map можно преоброзовать все элементы внутри списка.
# Перевести все строкиив верхний регистр.

# ls = ['one', 'two', 'three', 'four', 'five']

# new_ls = list(map(str.capitalize, ls))
# print(new_ls)

# names = ['John', 'Aikol', 'Aizirek', 'Nuraiym', 'Sanzhar']
        # ['Hello mr/mrs Aikol', 'Hello mr/mrs Aikol'..]

# def change_str(name): 
#     result = f'Hello, mr/mrs {name}'
#     return result
# new_ls = list(map(change_str, names))
# print(new_ls)

# new_ls = list(map(lambda x: f'hello, mr/mrs {x},names'))
# print(new_ls)

# dict_ = {1: 2, 3: 4, 5: 6}

# result = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(result)
# --------------------------------------------------------------------------------------------------------------------------------------------

# Filter(function, iterable)-> Применяет ко всем элементам iterable функции которую мы передали и возвращает 
# filrterforodject(интератор) только с элементами для которых функция вернула True

# ls = ['one', 'two', 'one', '', '1', '100', 'John99']
# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ['John', 'one', 'two', 'list', 'makers', 'ev.25', 'fanta']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)
# ------------------------------------------------------------------------------------------------------------------------------------------

# enumerate(iterable) - пронумеровывает каждый элемент внутри iterable eё собственным индексом

# ls = ['str1', 'str2', 'str3']

# # x = list(enumerate(ls))
# # print(x)

# for i , x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}')

# ------------------------------------------------------------------------------------------------------------------------------------------

# zip(iterables) -> она соеденяет каждый элемент итерируемых элементов между собой,
# соединяет в тип данных tuple() и возвращает его.

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]
                                     #Соединение по индексам
# result = list(zip(ls1, ls2))
# print(result)

# Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз. С точки зрения Python - это любой объект, у которого есть метод __next__ .
# Этот метод возвращает следующий элемент, если он есть, или возвращает исключение StopIteration, когда элементы закончились.

# ls1 = [1, 2, 3, 4]
# ls2 = [100, 200, 300, 400, 500]
# ls3 = [10, 20, 30]                                 # zip часто используют для создание словарей 
# res = list(zip(ls1, ls2, ls3))
# print(res)

# x = [(1, 2), (3, 4)]
# dict_ = dict(x)                                      #из кортежей можно создать словари 
# print(dict_)

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# d_values = ['castle_r1', 'winterfell', 'Starks', 'Cisco R1', '10.255.101.10']
# res = dict(zip(d_keys, d_values))
# print(res)

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#         'r1' :['london_r1', '21 New globe Walk', 'DYR-25', 'Cisco', '11.300.101.22'], 
#         'r2': ['london_r2', 'Greenwhich', 'Cisco', 'Cisco', '101.255.20.10'], 
#         'sw2': ['london_sw2', 'Mercyside', '3850-', 'Cisco', '10.255.101.10']
# }
# # for x in data:
# #         print(x)     -> ключи

# london_data = {}
# for key in data:
#         london_data[key] = dict(zip(d_keys, data[key]))

# print(london_data)
# ---------------------------------------------------------------------------------------------------------------------------------

# all(), any() -> Возвращает True, если все обьекты внутри iterable имеют значение True, иначе возвращает False
# [1,2] True
# 0 False
# 5 True
# 's' True
# '' False
# 'пробел' True

# Функция all() возвращает True, если все элементы в итерируемом типе являются истинными.
# Функция any() возвращает значение True, если хотя бы один элемент во всём итерируемом типе истинный.

# item_list = ["mango", "banana", "apple", "orange"]
# print (all(item_list))

# ip = '10.255.1y.108'
# ip1 = '10.255.18.108t'
# ip2 = '118.20.101.108'
# result = all(i.isdigit() for i in ip.split('.'))                               # -проверить каждую через точку
# result1 = all(i.isdigit() for i in ip1.split('.'))
# result2 = all(i.isdigit() for i in ip2.split('.'))
# print(result)
# print(result1)
# print(result2)

# Функция any() возвращает значение True, если хотя бы один элемент во всём итерируемом типе истинный.

# ls = [0, 0, [1, 2], (), '']
# print(any(ls))

# ignore = ['rm -rf', 'reset', 'chmod']
# command = input('Vvedite command: ')

# if any(word in command for word in ignore):
#         raise Exception('Invalid command!')
# else:
#         print('Vse ok!')
# ========================================================================================================



















