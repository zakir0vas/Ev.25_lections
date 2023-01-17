# JSON - JavaScript Object Notation
# единный формат хранения и передачи данных меду
# компьютерами, сервисами, приложениями и языками программирования через сеть интернет 

# <filename>.json  #Файл в формате json
# {
#     "id": 1
#     "author": "Ed Sheeran"
#     "title": "Perfect"
#     "year": 2015
#     "Hit": true 
# } -> JSON
# Наща задача научиться переводить данные JSON in PYTHON Dictionary

# JS object == {key: value}
# PY dict == {key: value}
# JSON == {key: vakue}

# Процессы сериаоизации и десериализации данных
# сериализауия (Записать данных в JSON ) = ээто перевод из питона в JSNO formate

# сериализация         -   десериализация 

# Методы:      dump -> метод записывает Питон данные в файл в формате JSON
# параллельно сделав сериализацию

#              dumps -> может записывать Питон данные в текст в формат JSON
# парралелтно сделав сериализацию.
# Дессериаоизация(чтение даннызх из JSON) - это процесс перевода JSON a PY dict

# ========================================================================================================

# import json
# dict_ = {
#     'name': 'Snow',
#     'last_name': 'John',
#     'status': True,
#     'wife': False,
#     'childrens': None
# }
# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)

# print()
# print(json_text)
# print(type(json_text))

# # -----------------------------------------------------------------------------------------------------------
# import json
# dict_ = {
#     'name': 'Snow',
#     'last_name': 'John',
#     'status': True,
#     'wife': False,
#     'childrens': None
# }
# print(dict_)
# print(type(dict_))

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)
    
# with open('new.json', 'w') as file:
#     data = file.read()
#     print(data)

# ---------------------------------------------------------------------------------------------------------------
#### Процесс десериализации

# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()
# print(json_data)

# dict_ = json.loads(json_data)
# print(dict_)
# print(type(dict_))

# import json
# with open ('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_)

# =================================================================================================================
# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)

# # print(json_data)
# # print(type(json_data))
# dict_ = json.load(json_data)
# print(dict_)
# print(type(dict_))

