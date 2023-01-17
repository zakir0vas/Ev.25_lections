# dist() - Словарь(структура,обьект) - упорядоченная коллекция элементов, (python3.7 - ordered). каждый элемент в словаре храниться в виде пары:
# # {ключ: значение}
# Ассоциативный массив, hash tadles,  object(js), strure == disctionary(py)

# Ключами могуут выступать неизменяемые типы данных, и в словаре храняться уникальные ключи. 
# Тогда как значениями могут выступать любые типы данных. 

# thisdict = {
# 'brand': 'Ford',
# 'model': 'Mustang',
# 'year': 1967
# }
# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])

# a = dict() #(пустой словарь)
# b = {}
# c = {1, 2}
# print(a, b, c)
# print(type(a))
# print(type(b))
# print(type(c))

# ls = [('key1','value1'), ('key2', 'value2')] К сведению
# dict_ = dict(ls)
# print(dict_)

# -----------------------------------Dict Methods---------------------------------------------------------------

# print(dir(dict))
#                              items/ keys/ values

# user_info = {
#     'first_name': 'John', 
#     'last_name': 'Snow',
#     'age': 24, 
#     'email': 'jahnsnow@gmail.com', 
#     'role': 'admin',
# }
# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():       key - (k)   value - (v)
#     print(value)
# print(user_info)
# for key, value in user_info.items():
#     print(f'key:{key}, value: {value}')

# ls = list(user_info.items())    #Вывод одного значения 
# print(ls[0][1])     #Без key само значение 

#----------------------Изменение элементов в словаре------------------

# dict_ =  {'name': 'Jack', 'age': 24}
# print(dict_['name'])
# dict_['name'] = 'John'     #Изменени значений. 
# print(dict_)
# dict_['address'] = 'Winterfell' #Добавление ключа
# print(dict_)

# dict_.update{'name': 'Jack', 'age': 24, 'address': 'Winterfell'}  #Второй способ добавления нового ключа
# a = 5
# print(a)    Присваивание 
# a = 7
# print(a)
 
#-----------------------------Создание-Fromkeys

# dict_={}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'value')   Создание большого словаря, где valueне повторяются
# print(new_dict)

##### get - получение по ключу
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Staek'}
# print(dict_.get(2))
# print(dict_[2])

####setdefault - работает так же как и  get, но если нет такого ключа он создаёт новую пару из этого ключа
# dict_ = {'name': 'Eddard', 'last_name': 'Stark'}
# print(dict_)
# print(dict_.setdefault('age', 38))
# print(dict_)

# print(dict_.get('age'))

#-------------Удаление элементов---------
# pop-удаляет по ключу              popitem- удаляет последнюю пару

# pop (<key>)   
# dict_ = {'name': 'John', 'last_name': 'Snow'}

# removed = dict_.pop('address', 'Такого ключа нет!')
# print(dict_)
# print(removed)

# dict_ = {'name': 'John', 'last_name': 'Snow'}

# removed = dict_.popitem()
# print(dict_)
# print(removed)


