#List - (список, массив) это изменяемый, последовательный 
# тип данных который предстовляет из себя коллекцию каких либо обьектов/значений
#итералы 

# my_list = [1, 'string', False, None, [1, 2, 3]]
# print(my_list)
# print(type(my_list))

#range - возвращает последовательность элементов (чисел)

# ls = list(range(1, 101))
# print(ls)
# print(type(ls))

# ls1 = list(range(0, 101, 2)) #третий аргумент отвечает за шаг, тут до 100 будет считать через один
# print(ls1)

#####Циклы For / While
# ls = list(range(1, 101))
# for num in ls: 
#     print(num ** 2 if  num % 2 == 0 else num ** 3)
#     # if num % 2 == 0:
#     #     print(f'Число {num} четное, квадрата: {num ** 2}')
#     # else:
#     #     print(f'Число {num} нечетное, куб: {num ** 2}')
#     # #<body>
    
#-------------------------------------------------------------
#Методы списков #dir -  открывает содержание,  Все Методы добывляются через точку ls.append
# print(dir([])

#append (element) -  Добавляет элемент в конец списка
# ls = [1, 2, 3]
# print(ls)
# ls.append(5)
# ls.append([6, 7, 8])
# print(ls)

#extend(iterable) -> расширяет список элементами из iterable object 
# ls = [1, 2, 3]
# ls.append(['Hello'])
# print (ls)
# ls.extend('Hello')
# print(ls)

#insert (<index>, <element>) - добавляет элемент по указанному индексу, передвигает (встает на место указанного индекса), все эл сдвигаются на право 
# ls = ['string', 2, 3, False]
# ls.insert(1, 4)
# # ls.insert(-1, True)
# # ls.insert(15, True)
# ls.insert(15, [1, 2, 3])
# print(ls)

# ------------------------------------------------------------
#index(element, [start], [end]) -> возвращает index элемнта в списке

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John']
# print(ls.index('name'))
# res = ls.index ('name')
# print(res)
# # # print(res[ls])
# print(ls[0:2])
# print(ls[-1][0])

# ---------------------------------------------------------------
#count(element) - возвращает кол-во вхождений elementв списке

# ls = [1, 2, 3, 4, 5, 6, 5, 5]
# result = ls.count(5)
# print(result)

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John', 'North', 'King', 'Queen', 'USA']
# str1 = input('Введите слово: ')
# print(ls)
# if str1 in ls:
#     print(f'"{str1}" есть в списке и его индекс {ls.index(str1)}')
# else:
#     print('No!')
    
# -----------------------------------------------------------------
#sort() - сортирует список если в аргументах передать reverse=True
#         список будет отсартирован в убывающем порядке

# import random

# ls = []
# for x in range (0, 50):
#     ls.append(random.randint(0,1000))

# print(ls)
# print()
# ls.sort(reverse=True)
#  print(ls)

# ls = ['Apple','Hello', 'World', 'my', 'name', 'is', 'John', 'North', 'King', 'Queen', 'USA', 'dog', 'makers']
# ls.sort(reverse=True, key=len) key=len -> по колличестве букв
# print(ls)

# -------------------------------------------------------
#remove(element) -  удаляет element из списка, если такого нет,ю то вводиться ошибка

#pop([index]) - удаляет и возвращает index, но если индекс не указан то удаляет последний элемент

# ls = [1, 2, 3, 4, 5, 5, 5, 6, 5]
# ls.remove(5)
# print(ls)
# while 5 in ls: 
#     ls.remove(5)
# print(ls)

# ls = [1, 2, 3, 4, 5, 5, 5, 6, 5, 99]
# deleted = ls.pop(0)
# print(ls)
# print(deleted)
# print(ls.pop())
# print(ls)

# # update -------------------- Обновление значений 
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)



	

# from    random  import randint



