# num = 1
# while num >= 0:
#     try:
#         num = int(input(' Введите число:'))
#     except ValueError:
#         pass
# else:
#     print('Встретилось отрицательное число!')
# ---------------------------------------------------------------------------------------------------
# from random import randint
# ls  = []
# for x in range (0, 100):
#     ls.append (randint(1,50))

# # print(ls)
# ls = list(set(ls))
# res = sorted(ls)
# print(res)
# ---------------------------------------------------------------------------------------------------

# def introduce(name, last_name, wife='холост', **kwargs):
#     print(f"Привет это {name} {last_name}")
#     print(f'Он {wife}!')
#     if kwargs:
#         print(f'Инициалы его жены {" ".join(kwargs.values())}')
# introduce('John', 'Snow')
# introduce('Tirion', 'Lanister', 'Женат', wife_name='Sansa', wife_last_name='Stark')

# ====================================================================================================

# Вам дан файл article.txt
# Требуется реализовать функцию longest_words(filename: str), которая выводит слово,
#  имеющее максимальную длину (или список слов, если таковых несколько).

# def longest_word(filename):
#     with open(filename) as file:
#         words  = file.read().split()
#     words.sort(key=len, reverse=True)
#     max_len = len(words[0])
#     res = []
#     for i in words:
#         if len(i) == max_len:
#             res.append(i)
#         else:
#             break
#     return  res if len(res) > 1 else res.pop()

# print(longest_word('test.txt'))

# ======================================================================================================
# 1.Вам дан список accounts, элементами которого являются другие списки
# Каждый список представляет собой количество денег на счету клиента.
# Напишите функцию которая выводит максимальное количество денег на счету самого богатого клиента.

# Пример:
# accounts = [[1,5],[7,3],[3,5]]
# Ожидаемый вывод: 10

# accounts = [[1,5],[7,3],[3,5]]
# res = []
# for i in accounts:
#     res.append(sum(i))
# print(max(res))                         Цикл 

# res = [sum(i) for i in accounts]
# print(max(res))                           Comprehension

# ======================================================================================================

# 2.Вам даны две строки:
# Word - слово, ch - буква.
#  Напишите функцию которая будет переварачивать сегмент слова (word),который 
# начинается с индекса 0 и заканчивается индексом первого вхождения ch(включительно). 
# Если ch не существует в слове, возвратите переменную word.
# Пример:
# Ввод: word = "abcdefd", ch= "d"
#  Ожидаемый вывод: "dcbaefd"
# Объяснение:
# Первое вхождение "d" находится в индексе 3.
# Переверните часть слова от 0 до 3 (включительно), в результате получится строка «dcbaefd».

# word = 'abcdef'
# ch = 'd'
# def func(word, ch):
#     mid = word.index(ch)    # = 3
#     s1 = word[0:mid+1]      # abcd[::-1]
#     s2 = word[mid+1:]       # efd
#     return s1[::-1] + s2
# print(func(word,ch)



# =============================================================================================================================================
# Работа с файлами

# | -> каретка - указатель - курсор

# open(<путь до файла>)

# file = open('/home/User/Desctop/en/files/lections/files.py')# абсолютный путь
# file = open(files.py)# относительный путь (относительно к той директории в которой вы работаете)

# Режимы работы с файлами

# 1. чтения -> r/r+(read)
# 2. записи -> w/w + (write)
# 3. добавления -> a/a+(append)
# b x t

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(len(data))
# file.close

# контекстный менеджер

# with open('test.txt') as file:
#     print(file.tell())
#     data = file.read()
#     index = data.index('My')
#     print(file.tell())
#     file.seek(index)
#     print(file.read())
#     print(file.tell())

# file.tell() -> возвращает индекс где находится 
# указатель (курсор/каретка) 
# file.seek(index) -> перемещает каретку на индекс 
# который вы передали

# with open('test.txt', 'r') as file:
#     print(file.readlines())
#     file.seek(0)
#     print(file.readline())
#     print(file.readline())
    
# print(file.read()) # Ошибка

# with open('test.txt', 'a+') as f:
#     f.write('\nHe is bastard of Ned Stark')
#     f.write('\nThis is lesson about files')
#     f.seek(0)
#     print(f.read())

# with open('test.txt', 'w') as file:
#     file.write('Hello, was opened with open!')

# ---------------------------------------------------
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_codes(image):
#         string = pytesseract.image_to_string(image)
#         # print(string)
#         list_of_imei = re.findall(r'IME.\d.\s\d+', string)
#         print(list_of_imei)
#         with open('imei_codes.txt', 'w') as file:
#             for x in list_of_imei:
#                 file.write(f'{x}\n')


# ls = 'imei.jpg'
# get_imei_codes(ls)
