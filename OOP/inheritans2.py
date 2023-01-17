# Множественное наследование - это когда класс насследуется от двух или более классов.

# class A:
#     pass
# print(A.mro())
# print(issubclass(A, object))
# ============================================================================================================
# class Auto:
#     def play_music_at_station(self):
#         print('Musicis plaing')
#     def ride(self):
#         print('We are riding on the ground')

# class Plane:
#     def play_music_at_station(self):
#         print('We started to listen music')
#     def fly(self):
#         print('We are flying')
    
# class FutureAuto(Auto, Plane):     #Какой класс наследуем первым то и принтиться
#     pass

# obj1 = FutureAuto
# obj1.ride()
# obj1.fly()
# obj1.play_music_at_station()
# ============================================================================================================

# MRO(Method Resolution Order) - механизм для корректного поиска родительских методов
# Был создан для того чтобы решить проблему ромба после введения класса object в Питоне

# class Zero:
#     def say(self):
#         print('Class Zero')

# class First(Zero):
#     def say(self):
#         print('Class First')

# class Second(Zero):
#     def say(self):
#         print('Class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()

# obj = MyClass()
# obj.say()
# print(MyClass.mro())
# ============================================================================================================
#################      Ошибка MRO
# class Y:
#     pass

# class X:
#     pass

# class A(X,Y):
#     pass

# class B(Y,X):
#     pass

# class MyMRO(type):
#     def mro(cls):
#         return (object, A, cls, B, X, Y)    #Переопределение MRO

# class C(A, B, metaclass=MyMRO):
#     pass

# obj1 = C()
# print(C.mro())
# ============================================================================================================
# Mixins(Миксиныб Премиси)
# В каких случиях:
# 1. Предоставить множество доп. функции для класса
# 2. использовать одну конкретную функцию во множестве разных классов

# class Machines:
#     def start_engine(self):
#         print('Started engine!')
# class MusicPlayerMixin:
#     def play_music(self):
#         print('Music is playing!')

# class Auto(Machines, MusicPlayerMixin):
#     pass
# class Boat(Machines, MusicPlayerMixin):
#     pass
# class WashinhMachine(Machines):
#     pass

# obj_auto = Auto()
# obj_boat = Boat()
# obj_wash = WashinhMachine()

# obj_auto.start_engine()
# obj_boat.play_music()
# obj_boat.start_engine()
# obj_auto.play_music()
# obj_wash.start_engine()
# ============================================================================================================


