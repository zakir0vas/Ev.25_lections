                                #Как проверить предложение вопросительное ли оно , пример 
                                #ТЕРНАРНЫЙ КОДЫ
# sentence = input('Введите предложение:')
# if sentence [-1] == '?':
#     print('Предложение вопросительное.')
# else:
#     print('Предложение обычное.')

#### sentence = input('Введите предложение:')
#### print('Предложение вопросительное.' if sentence[-1] == '?' else 'Обычное предложение ')

#Ternary operator (Тернарный оператор) - конструкция которая анологична по своим свойствам и
#действию конструкции if/else, но при этом записывается в одну строчку
#<Выражение если в условии True> if <Условие> else <Выражение если  False >

# num = 18
# res = "even num" if num % 2 == 0 else 'odd num'
# print(res)

# number = input("Введите число: ")
# if number.isdigit():
#     number = int(number)
#     print('Да число!' )
# else:
#     print('Вы ввели не число! ')

# from string import digits
# symbols = digits + '-'
# print(symbols)
# number = input("Введите число: ")
# is_correct = True
# for i in number: #567
#     if i not in symbols: #0123456789-
#         is_correct = False


# if is_correct:
#     print('Yes number')
#     number = int(number)
#     print('Your number: ', number)
#     result = number if number >= 0 else -number #-56
#     print(result)
# else:
#     print('Invalid values!')

