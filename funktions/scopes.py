# #ОБЛАСТЬ ВИДИМОСТИ И ПРОСТРАНСТВО ИМЕН
# #scopes - это технология которая определяет контекст переменной в рамках которого мы можем её использовать и видеть.

# # built-in (встроенная) - print(), len(), math, random, max(), etc.
# # global(Глобальная) - это имена которые определяются в самом файле который вы запусткаете 
# # *enclosed (nonlocal - не локальная)
# # local(локальная область) - определяется внутри функции 

# # x = 200

# # def func(x):
# #     print(x)
# #     a = 500
# #     print(a)

# # func()

# # x = 'global'
# # print(x, '1', 'global')

# # def enclosed(): #global
# #     x = 'enclosed'
# #     def local(): #enclosed
# #         x = 'local' #local
# #         print(x)
# #     print(x)
# #     local()
# #     print(x,'4', 'enlosed')

# # enclosed()
# # print(x, '5', 'global')

# # LEGB
# # local - enclosed - global - built in

# var = 100
# def increment():
#     var = var + 1 #try to update global name inside local scope
#     print(var)
# increment()

# global -  оператор который позволяет изменять значение глобальгой переменной
#           находясь в локальной обслачти видимости 
# nonlocal - оператор который позволяет изменять значение локальной (замкнутой) переменной
#           находясь в локальной обслачти видимости 


# scores = 67      #Инкримент  

# def increment():
#     global scores
#     scores += 1


# def kill_user():
#     print('Вы убили игрока, +1 очко')
#     increment()      #scores = scores + 1

# def kill_bot():
#     print('Вы убили бота, +1 очко')
#     increment()


# def eat_Edems_apple():
#     print('Вы сьели яблоко Эдема,+1 очко') 
#     increment()

# print('Стартовые очки:', scores)
# kill_user()
# kill_user()
# kill_bot()
# kill_bot()
# eat_Edems_apple()
# print('Финальный очки:', scores)

# --------------------------------

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# steps = counter()
# eat  = counter()
# # total = None
# # for i in range(2500):
# #     total = steps()

# # print(f'За день пройдено {total} шагов!')

# # print(steps())
# # print(steps())
# # print(steps())
# # print(steps())
# # print(steps())
# # print(steps())
# # print(eat())
# -------------------------------------------------------------------------------------------------------------------------------------------------4