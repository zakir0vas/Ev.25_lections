        #Срезы
#Даны две переменные s1 = "America" и s2 = "Japan".  Выведите новую строку в который будут записаны первый, средний и последний элемент двух переменных.  Необходимо использовать срезы.
# # Вывод: "AJrpan"
# s1 = "America"
# s2 = "Japan"
# #res = '1s1-1s2-ms1-ms2-ls1-ls2'  
# #количество строки / 2 = средняя сумма 
# first_s1 = s1[0]
# first_s2 = s2[0]
# middle_s1 = s1[len(s1) // 2]
# middle_s2 = s2[len(s2) // 2]
# last_s1 = s1[-1]
# last_s2 = s2[-1]
# # res = first_s1 + first_s2 + middle_s1 + middle_s2 + last_s1 + last_s2
# # print(res)

# res = s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
# print(res)

# str1 = '#makers#bootcamp#it#programming#github'
# res = str1[1:].split('#')
# print(res)

# dano -> {1-100}
# Число /3 - fu
# Число /5 - ba
# Число /3, /5 - fuba
# Вывод: 9 fu
#        25 Ba
#        15 fuba
# for number in range(1, 100):
#     # print(number)
#     if number % 3 == 0 and number % 5 == 0:
#         print(f'{number} fuba')
#     elif number % 3 == 0:
#         print(f'{number} fu')
#     elif number % 5 == 0:
#         print(f'{number} ba')

# --------------------------------------------------------------------------------

#Example 
# Name: Maya Angelou
# Name: Chimamanda Ngozi Adichie
# Name: Tobias wolff
# Name: Sherman Alexie
# Name: Jane Austen
# Результат:
# ['Adichie', 'Alexie', 'Angelou', 'Austen', 'Wolff', 'Sherman Alexie', 'Jane Austen'] 


# names = ['Maya Angelou', 'Chimamanda Ngozi Adichie', 'Tobias Wolff', 'Sherman Alexie', 'Jane Austen']
# result = []
# for x in names:
#     x = x.split(' ')
#     print(x)
#     result.append(x[-1])

# result.sort()
# print(result)

# range(start, stop, [step]) - возвращает
#последовательность из целых чисел, начиная с start до stop, возвращает итерируемый тип данных range
# x = range (1, 10)
# print(x)
# for num in x:
#    print(num)

# res = 0
# for num in range (1, 101):      Сумма всех чисел от 1 до 101 
#     res += num
# print(res)


# Создайте список с 3 вложенными списками списками, где внутри должно быть три 0
# Результат:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# res = []
# for x in range (0, 3):
#     ls = []
#     for x in range (0, 3):
#         ls.append(0)
#     res.append(ls)
# print(res)


# -----------------------------------------------------
# Dictionary
# Составьте код которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».

# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона: 
# - для зимы «За окном падал белый снег»,
# - для весны «Птицы пели прекрасные песни»,
# - для лета «Солнце светило ярче чем когда-либо»,
# - для осени «Урожай был невероятным».
# Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента 
# (не попадитесь на этом и предупредите о том, что «Требуется ввести реальный номер месяца»).


# month = {
#     1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'July',
#     8: 'August',
#     9: 'September',
#     10: 'October',
#     11: 'November',
#     12: 'December',
# }
# while True:
#     number = input('Введите номер месяца:')
#     if number == 'John':
#         break

#     if not number.isdigit():
#         print('Требуется ввести реальный номер месяца1')
#         continue
#     number = int(number)
#     if number not in range (1,13):
#          print('Требуется ввести реальный номер месяца1')

#     if number in range (3, 6):
#         print(f'Вы родилисьв {month[number]}. Птицы пели прекрасные песни. ')
#     elif number in range (6,9):
#         print(f'Вы родились в {month[number]}. Солнце светило ярче чем когда-либо ')
#     elif number in range (9,12):
#         print(f'Вы родились в {month[number]}. Урожай был невероятным ')
#     else:
#         print(f'Вы родились в {month[number]}. За окном падал белый снег')





# -----------------------------------------------------------------------------------------------
# 13/10/2022
# Обработка исключений
# Операторы try...except
# Ошибки Erros -> связаны с кодом:
# SyntaxError
# IndentationError
# TabError

# # Исключения Exceptions -> связаны с неправильными данными которые передаются в код
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException # прородитель всех исключений



# try:
#         num = int(input('Enter the number:'))
#         print(num)
#         num2 = int(input('Enter the number2:'))
#         print(num2)
#         print(num / num2)
# except:
#         print('Неправильные данные!')
# print('Очень важная строчка кода.')
# ------------------------------------------------------------------------------------

# try ... except
# try:
# <body try>

# except:
# <body except> сработает только если ошибка в Try

# <else> 
#     <body else> - сработает если в оператору try нет ошибки

# <finally:>
# <body finally> - сработает в лбом случае


# try:
#         num1 = int(input('Enter the number:'))
# except:
#         print('Invalid values!')
# print(num1)
# print(num1 + 5)
# ------------------------------------------------------------------------------------
# Отображение ошибки

#1. Import sys

# list_ = [1, 2, 3, 4, 5]
# index = int(input('Enter index:'))
# try:
#         res = list_[index]
#         print(res)
# except:
#         import sys 
#         print(f"oops, we catched{sys.exc_info()[0]} eror!")


#2. Exceprion as e/ (error)
# list_ = [1, 2, 3, 4, 5]
# while True:
#         try:

#             index = int(input('Enter index: '))
#             print(list_[index])
#         except Exception as e:
#                 print(f"oops, we catched {e} eror!")





# except ZeroDivisionError:

# print ('Divide by 0!')
# try:
#     num1 = int (input ( 'Enter: '))
#     num2 = int (input ('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делть нельзя!')
# except ValueError:
#     print('Invalid symbols!')
# else:
#     print(result)
# finally:
#     print ('The end!')

# --------------------------------------------------------------------------------------------------------------------
#  Функции

# ls = [2, '2', '4', 4, 45, '101']
# res = [x**2 for x in filter(lambda x: type(x)== int, ls)]
# res1 =[x**2 for x in ls if type(x)==int]
# print(res)
# print(res1)
# =============================================================================
# # Рандомный пароль

# from random import choices
# from string import ascii_letters as latters , digits
# from itertools import repeat
# from statistics import mean 

# q_pass = int(input('Vvedite kollichestvo paroley: '))
# symbols = '_$()-'
# result = {f(choices(latters, k=10),choices(digits, k=5), choices(symbols, k=1))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)}

# print(result)
# print(f'Quantity: {len(result)}')
# lens = [len(x) for x in result]
# print(f'Avarage len of passwords: {mean(lens)}')



