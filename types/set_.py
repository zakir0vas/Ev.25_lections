#Множества в питоне это некий контейнер в котором храняться множетва данных, уникальные элементы в неупорядоченном виде. 

# Литералы - {}
# a = {1: 'a'} - dictionary
# a = {1, 2, 3} - множество 

# set_ = {8, 7, 6, 5, 4, 3, 6, 8, 6, 6, 6, 6, 6}
# print(set_)
# print(type(set_))

# ls = [1, 2, 'a', 0, False, True, 'n']
# str1 = 'My name is John Snow'     
# ls.extend(str1)     
#-для добавления каждого элемента в ls
# print(ls)
# res = set(ls)   - множетсва в лист
# print(res)
# res = list(set(ls))
# print(ls)    # для возвращения листа во множество, выводит уникальный элемент каждого(без дубликатов)

# print(ls)
# set1 = {*ls}    #- оператор распаковки '*'
# res = [*set1]
# print(set1)
# print(type(set))
# print(res)
# print(type(res))

# FIFO / LIFO
# a = {1, 2, 3, 4, 5}
# print(dir(a))
# a.pop()  -удаляет первый элемент
# print(a)

# discard - не выводит ршибку - None     поэлементное удаление 
# remove - выводит ошибку - error

# set_ = {1, 2, 3, 4, 5, 6, 7}
# print(set_.discard(5))
# print(set_)

# set_ = {1, 2, 3, 4, 5, 6, 7}
# set_.remove(5)
# print(set_.remove(9))
# print(set_)

# frozenset - неизменяемый
# a = {1, 2, 3, 4, 5}
# f_set = frozenset([1,2,3,4,5])
# print(type(a))
# print(type(f_set))
# print(a)
# print(f_set)