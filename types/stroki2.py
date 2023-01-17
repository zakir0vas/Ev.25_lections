#Методы строк
#Аргументы

# print(dir(str))
#replace(old, new, [count]) - меняем в строке old на new, если ввы укажите count тотон заменит его ровно count раз.

# text = 'ha ha ha ha'
# result = text.replace('a', 'i')
# print(text)
# print ( f'result after replace: {result} ')

# str1 = 'Hello World. My name is John Snow!'
# result = str1.replace('John Snow', 'Jammie Lanister')
# print(result)

# Строки чувствительны к регистрам 
# print(id('H'))
# print(id('H'))
# print(id('h'))

# strip() - он убирает пробельные символыы в начале и в конце строки.
# Модификация - rstrip, lstrip

# text = ' Hello'
# text = input('Enter the text: ')
# print(len(text))
# result = text.strip()
# print(result)
# print(len(result)) 

# text = '   Hello World   '
# print(len(text))
# res = text.lstrip()
# # res = text.rstrip()
# print(res)
# print(len(res))

#print(dir(str))

# isdigit ->        эти 3 индекса проверяют 
# isnumeric ->   состоит ли наша строка полностью
# isdecimal ->             из чисел

# text = '57' #(5.7)
# if text.isdigit():
#    num = int(text)
#    print(num)
# else:
#    print('Oop! Invalid symbols')

# text = '\u0031'
# print(text)
# print(text.isnumeric())

# isalnum() -> проверяет состоит ли наша строка из чисел, 
#              латинского алфавита и кирилицы

# str1 = '56a'
# print(str1)
# print(str1.isalnum())
# str2 = '56_a'
# print(str2)
# print(str2.isalnum())

#salpha() -> сотсоит ли наша строка полностью из символов латинского либо кирильского алфавита

# text = 'Hello World'
# print(text.isalpha()) False -> пробел 
# text = 'Hello'
# print(text.isalpha())
# text = 'Hello World'
# print(text[:5].isalpha()) - срез пробела 

# islower нижний регистр
# isupper верхний регистр
# istitle 

# index(value, [start], [end]) -. выводит индекс значение value которое мы передаём в нашей строке

# text = 'Hello World! My name is John Snow'
# print(text.index('John'))
# print(text.index('o', 5))
# print(text[24])

#count(value, [start], [end]) -> выводит индекс значение value которые мы предаем нашей строке 

# text ='Hello o o world'
# print(text.count('Hello'))
# print(text.count('o'))
# print(text.count(' '))

# text = 'Hello World! My name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# res = text.index('o', res+1)
# print(res)
# print(text[24])

# text = 'Hello world! My name is John Snow'
# text = input('Enter the text:')
# i = 0
# res = -1
# while i <= text.count('o'): 
# res = text.index('o',res+1)
# print(res)
# i+= 1 -> Инкримент

# find(valu[start],[end]) -> делает тоже самое что и индекс (i) но есть одно отличие в том случае
#                            если value нет в строке то возвращается индекс -1

# text = 'Hello'
# print(text.find('l'))
# print(text.find('hi')

#swapcase() -> переводит все символы в противоположный регистр
#upper() -> переводит все символы на верхний регистр
#lower() -> переводит все символы на нижний регистр 

# text = "HeLLo world, JOHn SNow"
# print(text.swapcase())
# print(text.lower())
# print(text.upper())
# print(text)

#capitalize() -> переводит первые символы всех слов в первый регистр

# name = input ('Enter your name:').capitalize()
# print(f'Hello{name}')

#title() -> переводит первые символы всех слов в первый регистр 

# text = 'John Jammie Snow'
# print(text.title())
# print(text.capitalize())
# print(text)

# name = input('Enter you name: ')
# print(name.title())

#split(разделитель)-> дробит строку по разделителю который находится в строке все части 
#                      сохроняются в тип данных лист
 
# text = "let me speak from my heart in english cause my name is John Snow"
# ls = text.split()
# print(ls)
# print(len(ls))

#Разделитель #join(interable(list)) ->  соединяет строки по разделителю строки котрые находятся в list
# res = ''.join(list)
# print(res)
