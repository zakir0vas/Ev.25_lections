#String  - тип данных Строки 

# это выражение (или константа), которое создает (генерирует) объект. 
# Если в тексте программы встречается литерал, то для этого литерала создается отдельный объект некоторого типа. 

# 'Hello World'
# "Hello World"
# """
# Hello World
# My name is Sam 
# """

# Строки - это набор последовательныйх символов, которые мы используем для хранения 
# и прредстовления текстовой информации, любая текстовая информация хранится в Строках 
# Набор методов и операции которые мы можем использовать с данными в виде текста 

#Индексация в строке - у каждого символа свой индекс (0,1,2...14)
#name =  'John'
#       J = 0 = -4
#       o = 1 = -3
#       h = 2 = -2
#       n = 3 = -1
# print(name )
# print(name(1))
# print(name(-1))

# str = 'birthday'
# print(str[5]), print(str[6]), print(str[7])
# print(str[-3]), print(str[-2]), print(str[-1])
# print(str[0]), print(str[1]), print(str[2]),print(str[3]),print(str[4]),print(str[5]),print(str[6]),print(str[7])

# Срезы по индексам - ДО последнего индекса 
#[start: , end: <step>]
# str1 = 'birthday'
# str2 = str1[0: 5]
# print(str2)
# print (str1[5:8])
# print(len(str1)) (Len-длина строки)
# print(str1[5:])
# print(str1[:5])

# text = "Hello World. My name is John! i'm North king" #= 'I\'m '
# print (text)
# print(len(text)) 

# print (text[:12])
# print(text[13:29])
# print(text[30:])
#Step - показывает те буквы которые указывается в третьем аргументе  [0:10:2]
#print(text[:12:2])
#print(text[::-1])
#print(text[:12:-1])

# Конкатенация строк (слияние, соединение)

# word1 = 'Hello'
# word2 = 'World'
# probel = ' '

# result = word1 + probel + word2 
# print(result)
# print(word1 + probel + word2 +'!')

#Форматирование строк 
# 1. с помощью % 
# 2. с помощью (.format())
# 3. интерполяция строк (f-строки)

# %
# name = input('Enter your name:')
# last_name = input('Enter your last name:')
# print('Hell, my name is', name, last_name)
# print('Hello, my name is %s %s ' %(name, last_name)) 

# .format
# name = input ('Enter your name:')
# last_name = input ('Enter your last name:')
# print('Hello, my name is {} {} ' .format (name, last_name))

# # f - строка
# name = input ('Enter your name:')
# last_name = input ('Enter your last name:')
# print(f'Hello, my name is {name} {last_name}')

# Экранирование строк - механизм при помощи которого можно вставлять 
#символы, которые сложно ввести с клавиатуры в строку
# \n - перенос строки
# \t - горизонтальная табуляция 4 пробела
# \v - вертикальная табуляция одна строка вниз 

# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name = '\t Snow'
# print (name)
# print(lastName)
# print(last_name)

# number = 10
# string = 'makers'
# print(string * number)











