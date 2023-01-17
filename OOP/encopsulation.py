# Анотации свойств (@property(getter, setter))

# class Person:
#     __age = 22
    
#     @property
#     def age(self):
#         """The property(getter)"""
#         print('getter')
#         return self.__age
    
#     @age.setter
#     def age(self, value):
#         """The age setter """
#         print('setter')
#         if not isinstance(value,int) or not 0 <= value < 170:
#             raise ValueError('Invalid value for human age!')
#         self.__age = value

# obj = Person()
# print(obj.age)
# obj.age = 18
# print(obj.age)
# ====================================================================
# class Circle: 
#     def __init__(self, radius) -> None:
#         self._radius = radius

#     def _get_radius(self):
#         print('Getter, _get_radius')
#         return self._radius
#     def _set_redius(self, value):
#         print('Setter, _set_radius')
#         if not isinstance(value, (int, float)):
#             raise ValueError('Radius must be an int or float object!')
#         self._radius = value

#     def _del_radius(self):
#         print('Deketer, _dek_radius')
#         question = input('Are you sure to delete radius(yes/no)?')
#         if question.strip().lower() == 'yes':
#             del self._radius    
#             print('Deleted!')
#         else:
#             print('Not deketed! Operetion denay!')                                                       #Для удвления

#     radius = property(fget=_get_radius, fset=_set_redius, fdel=_del_radius, doc='The rad protected property')
    
# circle = Circle(15)
# print(circle.radius)
# circle.radius = 36
# print(circle.radius)
# del circle.radius
# print(circle.radius)
# ====================================================================

# class CoordinationWriteError(Exception):     # Read only, Write onle, Read & Write
#     pass

# class Point:
#     def __init__(self, x, y) -> None:
#         self.__x = x
#         self.__y = y 

#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, value):
#         raise ConnectionAbortedError('x coordinate is read only field!')

#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, value):
#         raise ConnectionAbortedError('y coordinate is read only field!')

# obj = Point(15, -225)
# print(obj.x)
# print(obj.y)
# obj.x = 36
# obj.y = 100

# ====================================================================
# WRITE only 

# import hashlib
# import os

# class User:
#     def  __init__(self, username, password) -> None:
#         self.username = username
#         self.password = password

#     @property
#     def password(self):
#         raise AttributeError('Password field is erite only! You cant see the password')

#     @password.setter
#     def password(self, value):
#         if not isinstance(value, (str)):
#             raise ValueError('Invalid value for password!')
#         salt = os.urandom(32)
#         self._hashed_password = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'), salt, 100_000)

# john = User('JohnSnow', 'secretkey')
# print(john.username)
# # print(john.password)
# print(john._hashed_password)

# ====================================================================

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       