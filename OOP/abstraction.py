# Абстракция (Абстрактный класс) - его можно рассматривать как набор методов 
# которые обязаны быть созданы и реализованы во всех
# дочерних классах которые унаследованы от абстрактного класса 

# Абстрактный метод - это метод у которого есть обьявления но нет реализации (методы пустышки)

# (abc - abstract base class)

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name
    
#     @abstractmethod
#     def area(self):
#         pass                       #-пустышка

#     def fact(self):
#         print('Я фигура в двумерной плоскости')

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         from math import pi
#         return pi * self.radius ** 2


# obj = Square(6)
# obj2 = Circle(3)

# print(obj.area())
# print(obj2.area())


# from abc import ABC, abstractmethod

# class ChessPiece():
#     #общий методб который будет использовать все начледники этого класса
#     def draw(self):
#         print('Drew a chess piece!')
 
#     #Абстрактный метод который необходимо переопределить для каждого дочернего класса
#     @abstractmethod
#     def move(self):
#         pass

# class Queen(ChessPiece):
#     def move(self):
#         print('Queen can move to everywhere: diogonally, vertically, horizantally')

# class Pawn(ChessPiece):
#     def move(self):
#         print('Pawn can move directly to one cell.')

# q = Queen()
# p = Pawn()

# q.draw()
# p.move()

# p.draw()
# q.move()


#class methods, instance, static

# Методы (обьекта) класса (instance methods) - это те методы в ООП которые изменяют состояние обьекта от класса
    #def methods(self) - self это ссылка на обьект 

# Метода класса (class methods) - это методы которые могут изменять состояние самого класса и манипуллировать им
    # @classmethods
    # def methods(cls) - cls - это ссылка на сам класс

# Статические методы (static method) - это те методы котрые не могут изменять состояние, обьект, класс
    # @staticmethod
    # def method()





# class Person:
#     surname = 'Stark'
#     def init(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @staticmethod
#     def is_adult(age):
#         if age >= 21:
#             print('Person is adult')
#         else:
#             print('Not adult!')

#     @classmethod
#     def from_birth_date(cls, name, year):
#         from datetime import date
#         age = date.today().year - year
#         return cls(name, age)

# obj = Person('John', 24)
# obj1 = Person.from_birth_date('Jamie', 1961)
# print(obj.name, obj.age)
# print(obj1.name, obj1.age)