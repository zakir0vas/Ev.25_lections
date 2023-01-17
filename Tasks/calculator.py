# #eassiest calculator
# lang = 'EN'
# lang_opt = input('Enter L to change language or other key to continue:  ')
# while lang_opt == 'l':
#     if lang == 'RU':
#         lang = 'EN'
#         lang_opt = input('Enter L to change language or other key to continue:  ')
#     else:
#         lang = 'RU'
#         lang_opt = input('Введите L, чтобы сменить язык, или любую клавишу, чтобы продолжить:  ')
# if lang == 'EN':
#     f = 'Enter first number:  '
#     o = 'Enter operation (+,-, /, *):  '
#     s = 'Enter second number:  '
#     r = 'Result: '
#     e = 'Error'
#     v = 'Enter "yes" to continue and other key to finish:  '
# if lang == 'RU':
#     f = 'Введите первое число:  '
#     o = 'Введите операцию (+,-, /, *):  '
#     s = 'Введите второе число:  '
#     r = 'Результат: '
#     e = 'Ошибка'
#     v = 'Введите "yes", чтобы продолжить, и любую клавишу, чтобы закончить:  '
# cont = 'yes'
# while cont == 'yes':
#     f_num = float(input(f))
#     oper = input(o)
#     sec_num = float(input(s))
#     if oper == '+':
#         print(r, f_num + sec_num)
#     elif oper == '-':
#         print(r, f_num - sec_num)
#     elif oper == '/':
#         print(r, f_num / sec_num)
#     elif oper == '*':
#         print(r, f_num * sec_num)
#     else:
#         print(e)
# cont = input(v)

#----------------------------------------------------------

# from string import digits 
# flag = True
# symbols = digits + '-' + '.'

# # while True: Цикл повторения

# while flag:
#     # choice = input('Введите Yes или Not: ')
#     # if choice == 'Not':
#     #     flag = False 
#     is_correct_number = True
#     num1 = input('Введите первое число: ')
#     num2 = input('Введите второе число: ')

#     if len(num1) == 1 and (num1 == '.' or num1 == '-') and num1:  #if len(num1) = 1 and (num1 == '.' or num1 == '-') and num1:
#         is_correct_number = False #Ошибка , чтобы код не останавливался(не выводил ошибку)

#     for x in num1:
#         if x not in symbols:
#             print("Вы ввели неправильное число!")
#             is_correct_number = False
#             break #Чтобы фраза не повторялась при неправельном введений(к примеру ввели букву)


#     if len(num2) == 1 and (num2 == '.' or num2 == '-') and num2:  
#         is_correct_number = False 
#     for x in num2:
#         if x not in symbols:
#             print("Вы ввели неправильное число!")
#             is_correct_number = False
#             break 

#     if not is_correct_number:
#         continue 

#     num1 = float(num1) if '.' in num1 else int(num1)
#     print(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     print(num2)
#     operator = input('Введите оператор(+, -, *, /): ')

#     if operator == '+': 
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else: 
#             print(f'Результат: {num1 / num2}')
    
#     else:
#         print('Вы ввели неправильный оператор!')

#     choice = input('Хотите остановить (yes): ')
#     if choice.lower() == 'yes':
#         flag = False
#         print('Пока!')