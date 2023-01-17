# Магические методы MAgic Methods
# Dunder methods(double underscore) -> __doc__, __init__
# служебные методы

# res = 5 + 5  __add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

#Магические методы сравнения:
#__eq__(self, other) ->  5 == 8
#__ne__(self, other) ->  !=
#__lt__(self, other) ->  <
#__gt__(self, other) ->  >
#__le__(self, other) ->  <=
#__ge__(self, other) ->  >=

# class Word(str):
#     def __new__(cls, obj):
#         # print(cls, '!!!!!!!')
#         # print(object, '--------')
#         obj = obj.replace(" ", '')
#         return super().__new__(cls, obj)
#     # def __init__(self, word) -> None:
#     #     super().__init__()
#     #     self.word =  word

#     def __gt__(self, other: str) -> bool:
#         print('gt is working')
#         print(self, '!!!')
#         print(other, 'xxxx')
#         return len(self) > len(other)

# obj = Word('Hello World   ')
# obj1 = Word('   Salam   ')
# print(obj > obj1)
# print(obj <= obj1)
# print(obj == obj1)
# print(obj, len(obj))
# print(obj1, len(obj1))
# =============================================================================

# Конструктор -> __new__
# Инициализатор -> __init__

# class Conventer(float):
#     def __new__(cls, x):
#         print('new is working')
#         if x < 50:
#             raise ValueError('x меньше 50')
#         return super().__new__(cls, x)
    
#     def __init__(self, x):
#         print('init is working')
#         self.number = x

# obj = Conventer(49)
# print(obj.number)
# ==============================================================================
#  Dunder method - для стракового отображения методов
#__str__ , __repr__

# class Base:
#     def __init__(self, stroka):
#         self.string = stroka

#     def __str__(self) -> str:
#         return f'Object: {self.string}'

#     def __repr__(self) -> str:
#         return f'Base("{self.string}")'
  

# obj = Base('Jasy')
# print(obj)
# print(repr(obj))
# obj2 = eval(repr(obj))
# print(obj2, '!!!')
# ==============================================================================

# Dunder методы арифмитических операции
#   +  -> __add__
#   -  -> __sub__
#   *  -> __mul__
#   //  -> __floordiv__
#   /  -> __div__
#   %  -> __mod__
#   **  -> __pow__

# class Cifra(int):
#     def __new__(cls, number):
#         if not 0 < number < 100:
#             raise ValueError('Enter the numbers in range 0-100')
#         isinstance = super().__new__(cls, number)
#         return isinstance
    
#     def __init__(self, number) -> None:
#         self.number = number

#     def __add__(self, other: int) -> int:
#         print('add is working')
#         print(f'Result: {self} + {other} = {self.number + other.number}')

# value1 = Cifra(17)
# # value2 = Cifra(56)
# # value1 + value2

# class User:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self):
#         print(f'User object: {self.name}')

# user1 = User('Jasy Lili')
# user2 = User('SHerman Mclaren')
# print(callable(user1))
# user1()
# user2()

# class LockSetFile:
#     def __init__(self, file) -> None:
#         self.file = file
#         self.number = 0
    
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             from datetime import datetime
#             self.number += 1
#             with open(self.file, 'a') as file:
#                file.write(f'{self.number})Func name: {func.__name__}, Called time: {datetime.now().time()}\n')
#             return func(*args, **kwargs)
#         return wrapper

# test = LockSetFile('log.txt')

# @test
# def start_test():
#     pass

# @test
# def hello():
#     pass

# @test
# def world():
#     pass

# start_test()
# hello()
# world()
# start_test()
# # ==============================================================================

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls

#     def __getitem__(self, index):
#         if index == 0:
#             print('Invalid index')
#         elif index < 0:
#             print(self.ls[index])
#         else:
#             print(self.ls[index -1])

# x = MyList([1, 2, 3, 4, 5])
# x[1]
# x[4]
# x[2]
# x[-1]
# x[0]



# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_moneta(self, moneta):
#         self.total += moneta
#         self.coins.append(moneta)
    
#     def __len__ (self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index]

# obj = Kopilka()
# print(len([1,2,3]))
# print()
# obj.add_moneta(25)
# obj.add_moneta(50)
# print(obj.coins)
# print()
# print(len(obj))
# print(obj[0])
# for x in obj:
#     print(x)


# a = [1,2,3,4]
# for x in a:
#     print(x)

# i = 0
# while i < len(a):
#     print(a[i])
#     i+=1

# ==========================================================================================
# SINGLETON
# class Singleton:
#     isinstance = None

#     def __new__(cls):
#         if not cls.isinstance:
#             cls.isinstance = super().__new__(cls)
#         return cls.isinstance

# obj = Singleton()
# print(obj)
# obj2 = Singleton()
# print(obj2)

# ==========================================================================================
# class Car:
#     def __init__(self) -> None:
#         self.model = "Honda"

#     def __delattr__(self, name) -> None:
#         value = getattr(self, name)
#         choice = input(f'Are sure to delete attr: {value}?')
#         if choice.strip().lower() == 'yes':
#             super().__delattr__(name)
#             print(f'{value} removed!')
#         else:
#             print('Ok, not removed!')

# honda = Car()
# print(honda.model)
# del honda.model
# print(honda.model)
    