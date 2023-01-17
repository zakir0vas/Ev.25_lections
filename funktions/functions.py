        #  Функции - Именновая часть программы которая может называться в других частых
        # программы столько раз, сколько нужно. 
                                                                              # Dont repeat yourself DRY
# def name_of_function(<a , b> #параметры):
    # body - код, какя-то логика, котрая будет запусткаться при обращений к функции
    # [<return>] - оператор для возращения результата

# name_of_function(5, 6 #аргументы)
# Параметры Функции - переменные котрорые будут принимать ваша фукция для того чтобы мы смогли работать 
# с данными которые попадают в нашу функцию, данные сохраняются в параметрах.

# Аргументы - это данные котрые мы передаем для параметров при вызове функции.

# Return - это оператор котрыq нужен чтобы функция возварщала результат если ретёрна нет 
# в функции, то по умолчанию возвращает None
 
# res = max/min(range(1,100)) -  возвращение результата минимальное/максимальное значениеи
# print(res)

# def (sumTwoNums)(sum_two_nums)  - пользоваться camelCase/snakeCase

# def sum_two_nums(num1, num2): #параметры      Можно также передать в другуя папку указывая путь 
#     result = num1 + num2
#     return result

# print(sum_two_nums(5, 6))

# def our_len(a):
#     try:
#         res = 0
#         for x in a:
#             res += 1
#         return res
#     except TypeError:
#         return 'Value is not iterable!'

ls  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
str1 = 'Hello world! My name is John Snow'
print(len(ls))
print(len(str1))
print(len(True))

def isEven(num):
    if num % 2 == 0:
        return True
    return False
print(isEven(16))
b = int(input('Введите число: '))

print(isEven(15))
print(isEven(b))
print(isEven(14))
print(isEven(24))


def get_polindroms(words):
    result = []
    for x in words:
        if x.lower() == x[::-1].lower():
            result.append(x)
        return result

some_words = ['John', 'ono', 'Kazak', 'peter', 'Dovod', 'tenet', 'anna', 'kak', 'piko']
polindroms = get_polindroms(some_words)
print(polindroms)

# --------------------------------------------------------------------------------------------------------------------------------------------

