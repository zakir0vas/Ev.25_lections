#Операторы сравнения 
# <, >, ==, <=, >=, !=(не равно)

# 1 < 5 -> True
# 7 > 9 -> False

# num = 15
# num2 = 15
# print(num <= num2)
# num1 = 20
# num2 = 17
# print(num1 >= num2)

# stroka1 = 'Hello'
# stroka2 = 'World'  #ascii codes
# print(stroka1 <= stroka2)

# print(ord('H'))    ord - для просмотра АСКИИ кода  
# print(ord('а'))
# print(ord('A'))
# print(ord(' '))

# print(chr(1080), (chr(1048)))  chr - для просмотра символа по коду 

# strok1 = 'Hello!'
# strok2 = 'World'
# print(len(strok1) > len(strok2)) С использованием [len] можно сравнить сколько символов в строке 

#Условные операторы
# if 
# elif
# else 
# num = int(input)
# if num > 18:
#     print('Access')
#     else:
#         print('Denied')

# if <condition>:  #Выражение всегда должно возвращать либо да либо нет 
#    <body if>    #сработает если в выражений if будет   True
# elif <condition>:
#      <body elif>
# else <condition>:
#      <body else>  #срабатывает если во всех выше стоящих условиях пришло False

# string = input('Enter smt: ')
# if string.lower() == 'hello':
#     print('Hello stranger')
# elif string.lower() == 'john':
#     print('Welcome back John Snow.')
# elif string.lower() == 'abrakadabra':
#     print('Simsalabim')
# else:
#     print('Совпадений не найдено.')

# print(string)

# b = 0
# a = 50
# n = 98
# if n < 100:
#    b = n + a 
# print(b)

# email = input('Enter email: ')
# password1 = input('Enter password: ')
# if len(password1) < 8: 
#     raise ValueError('Password too short!')
# password2 = input('Enter password confirmation: ')
# if password2 != password1:
#     raise ValueError('Password didn\t match')
# else:
#     print('Successfully signed up!') 

# age = int(input('Enter your age:')) WRONG 
# age = input('Enter your age:')  WRONG  + .isdigit

# age = input('Enter your age:') 
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid values!')
# if age < 18:
#     print(f'Access denied!Come again  after {18 - age} age!')
# else:
#     print('You can buy it!')

# Логический операторы and, or, not

# my_age = 20
# your_age = 18
# # result = my_age == 20 and your_age == 18
# # print(result)
# # result = my_age == 20 or your_age == 20 #True будет либо этот лиюо другой 
# # print(result)
# # result = not my_age == 20 #Числа кроме 20 будут True 
# # print(result)
# result = not my_age == 30 and not your_age == 30
# print(result)


#Repet
# user = 'John'
# is_google_user = True
# is_github_user = True     #should change every answer (True/False)
# is_age_greater_21 = False
# user_coins = 4000 
# #(либо user google or github или возраст выше 21, либо бабки 800)

# if (is_google_user or is_github_user) and (is_age_greater_21 or user_coins > 8000):
#     print(f'You can enter the system Mr/Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enrter')  

      #операторы идентификации 
#  is- проверяет наличие элемента внутри какого либо масива (интерируемого обьекта)[строки, списки и т.д.]
#  in- сравнивает ячейки памяти двух обьектов
#     == -> сравнивает по значению
# is not - отрицательные ячейки памяти 

# str1 = 'Hello World'
# print(str1)
# choise = input ('Enter cymbol:')
# if choise in str1:  #chage to 'not in' -> 
#     print(f'The symbol: {choise} exist!') #change to doesn\t exist
# else:
#     print(f'The symbol: {choise}  doesn\'t exist!') #change to doesn\t exist



