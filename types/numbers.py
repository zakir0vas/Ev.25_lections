# Типы данных - Числа int(), float()

# = - оператор присваивания 

# number = 51 
# print(number)
# стили переменной 
# tommorow_day - snake case
# tommorowDay - camel case
# abc - нижний регистр 
# ABC - верхний регистр 
# +
# a = 5
# b = 15
# result = a + b
# print(result)
 
# print('Результат суммы 5 и 15:', 5+15)

# a = 100 
# b = 1000
# c = 500
# d = 50.20
# print( a + b + c + d)

# num1 = 996
# num2 = 62.55
# print(num2 - num1)

# num1 = 55
# num2 = 199988
# result = num1 * num2
# print (result)

# num1 = input ('Введите слово:')
# num1 = 15.17
# print(type(num1))

# num = '15'
# num = int(num) # '15' - 15
# print(type(num))

# num1 - int(input('Введите чсило 1: '))
# num2 - int(input('Введите число 2: '))
# result = num1 * num2 


# / and // and %
# / - Обычное деление 
# // - Целочисленное деление (деление без остатка)
# % - Модульное деление (остаток от деления)

# num1 = 5
# num2 = 2
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2) 

# ** - Разведение в степень 

# num1 = 5
# print(num1 ** 10)

# pow( a, b,  <mod>) -Функция возведения в степень числа а в степень b
#print(pow(2, 5, 5)) # 2 * 5 % 5 -> 2

#diwmod(a, b) -> Она выводит два числа, первое число это результат целочисленного деления (//), а 
#второе число это модульное деление (%) двух чисел

# res = divmod(30, 5 )
# print(res)

#round() -> функция округления
# res= 24 / 13 
# print(res)

# res= 24 / 13 
# print(round(res, 2))

#abs() -> Абсолютное значение числа -> abd(-5)=5 -> |-5| = 5
# print(abs(-101))
# print(abs(50))

# # import math 
# from math import pi, sqrt
# # print(math.pi) 

# # math.sqrt -> корень числа 

# print(sqrt(1001))



# dir -> возвращает методы обьекта или функции 
# import math 
# print(dir(math ))

# """
# Множественное присваивание 
# """
# a = 5
# # a, b, c, = 1, 2, 3
#  v = 5
#  n = 7
#  d = 3
#  v, n, d = d, v, n

 
# num1 = 10
# num2 = 3
# num3 = num1 
# num1 = num2
# num2 = num3 
# print(num1, num2) (без множественного приисвание )


# print('Hello' * 3) (Дублирование строк)

# str1 = '12'
# num1 = 2
# print(str1 + str(num1)) (Error )

"""
инкримент и дикримент 
"""
#Инкримент -> увеличение значения како-либо переменной. Пример a = 1 (a +=1 -> a + a+1)
 #a +=1(2,3,4,5,6,7,8...)
# a = 0
# a += 1
# print(a)

#Дикримент - ументшение значение какой-либо переменной (a -= 1 -> a = a - 1)

# a = 0 
# a -= 3
# print (a)

# a = 2
# a *= 2
# print(a)

# a = 2
# a /= 2
# print(a)

"""
id()-> номер в ячейке памяти
"""
# a = 1
# b = a 
# print (b)

""" 
Type -> выводит тип  заданной переменную 
"""
# a = 9
# b = 'Hello' 
# print (a, b)

#var = int (input('Введите число:'))

# num1 = int(input('Введите число:'))
# num2 = int(input('Введите степень:"'))
# print(num1 ** num2) 

""" 
Модуль random - предостовляет нам фукции для генерации случайных чисел, так же буквы или другие элементы.
"""
# import random
# print(dir(random))
# num = random.randint(1111, 9999)
# print(num)

# from random import choice
# import string
# # print (string.ascii_letters)

# a = choice(string.ascii_letters)
# print(a)

# import math 
# from math import pi 

# r = int(input('Введите радиус:'))
# # print(2 * r * pi )
# # print(pi * (r **2))

# result_P = 2 * r * pi
# result_S = pi * (r ** 2)
# print('Площадь окружности', round(result_S))
# print('Периметр окружности', round(result_P))




