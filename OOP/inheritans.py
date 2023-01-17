# Принципы  ООП 
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм 
# 4. Абстракция 
# 5. Композиция 
# 6. Агрегация 
# 7. Ассоциация 
# =====================================================================================================================

#НАСЛЕДОВАНИЕ- это механизм позволяет принимать родительские методы и атрибуты для дочернего класса. 
# Родительский класс 
# Дочерний класс

# class Animal:
#     def print_info(self):
#         print("I'm an animal!")
# class Croco(Animal):
#     pass

# croco = Croco()
# croco.print_info()
# ====================================================================================

# class Animal:       # Родительский класс
#     name = None
#     voice = None
#     meal = None
#     def say(self):
#         print(f'This animal is {self.name}: {self.voice}')
    
#     def eat(self):
#         print(f'This animal {self.name} eats {self.meal}!')

# class Lion(Animal): #Дочерний класс
#     name = 'Lion'
#     meal = 'meat'
#     voice = 'rrrarr!'

# class Dog(Animal):
#     name = 'dog'
#     meal = 'meat'
#     voice = 'bark!'

# class Koala(Animal):
#     name = 'koala'
#     meal = 'Eucalyptus'
#     voice = 'roar'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# simba.say()
# simba.eat()

# julian.say()
# julian.eat()
# =====================================================================================================================

# class Emploee:
#     bonus = 1.5

#     def __init__(self, name, last_name, salary):
#         self.name = name + " " + last_name
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'

#     def give_increase(self):
#         self.salary = self.salary * self.bonus

# class Developer(Emploee):
#     def __init__(self, name, last_name, salary, languages):
#         super().__init__(name, last_name, salary)
#         self.prog_lang = languages

# class Manager(Emploee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
        
#         if not emps:
#             self.emps = []
#         else:
#             self.emps = emps 

#     def add_emps(self, employee):
#         self.emps.append(employee)

#     def show_emps(self):
#         return [x.get_info() for x in self.emps]

# dev1 = Developer('John', 'Snow', 1000, 'Python')
# print(dev1.salary)
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Pags', 1500, 'JS')
# dev4 = Developer('RAychel', 'Cruse', 1000, 'Pyrhon')

# man1 = Manager('Ivan','Ivanov', 2000 )
# man2 = Manager('Dastan', 'Velikii', 4000, [dev1, dev4])

# man1.add_emps(dev2)
# man1.add_emps(dev3)
# man2.add_emps(dev2)

# print(f'Manager {man1.get_info()}, has {man1.show_emps()} developers.')
# print(f'Manager {man2.get_info()}, has {man2.show_emps()} developers.')

# man2.give_increase()
# dev2.give_increase()

# print(man2.get_info())
# print(dev2.get_info())

# =====================================================================================================================

# class Laptop:
#     def __init__(self, brand, model, description, price):
#         self.brand = brand
#         self.model = model
#         self.desc = description
#         self.price = price

#     def get_info(self):
#         return{'brand': self.brand, 'model': self.model, 'description': self.desc, 'price': self.price}

# class MacBook(Laptop):
#     def __init__(self, brand, model, description, price, year, provider):
#         super().__init__(brand, model, description, price)
#         self.year = year
#         self.provider = provider

#     def  get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['provider'] = self.provider 
#         return repr
# class Acer(Laptop):
#     def __init__(self, brand, model, description, price, videocard, display):
#         super().__init__(brand, model, description, price)
#         self.videocard = videocard
#         self.display = display
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr

# odj1 = Laptop('Acer', 'M330', '8gd, 512 SSD', 800)
# odj2 = MacBook('Apple', 'Air', '13, 8gb, 256 SSD', 1000, 2020, 'China')
# obj3 = Acer('Acer', 'Inspire', '16gb, 1tb ssd', 1000, 'gtx geforce nvidia', '15.6 Full RGB')


# print (odj1.get_info())
# print (odj2.get_info())
# print (obj3.get_info())

# =====================================================================================================================
# class Post:
#     def __init__(self, user) -> None:
#         self.user = user 
#         self.posts = []
#         self.id = 0

# #CRUD
#     def create_post(self, title, body, image):
#       self.id += 1
#       post = dict(id=self.id, title=title, body=body, image=image)
#       self.posts.append(post)
#       return {'status': 201, 'msg': 'Successfullu created!'}

#     def list_posts(self):
#         repr = []
#         for post in self.posts:
#             repr.append({'id':post['id'],'title': post['title'],'image':post['image']})
#         return{'status': 200, 'msg': repr}

#     def detail_post(self, id):
#         for post in self.posts:
#             if post.get('id') == id:
#                 return{'status': 200, 'msg': post}
#         return {'status': 404, 'msg': 'Not Found!'}

#     def update_post(self, id, **kwargs):
#         for post in self.posts:
#             if post['id'] == id:
#                 post.update(kwargs)
#                 return {'status': 206, 'msg': 'Successfully updated'}
#         return{'status': 404, 'msg': 'Not Found!'}
    
#     def delete_post(self, id):
#         for post in self.posts:
#             if post['id'] == id:
#                 try:
#                     self.posts.remove(post)
#                     return{'status': 204, "msg": 'Successfully deleted!'} 
#                 except:
#                    return{'status': 500, "msg": 'Pni svogo backa!'}
#         return{'status': 404, 'msg': 'Not Found!'}


# account1 = Post('JamesKirk')
# print(account1.create_post('Good news!', 'dvnl', 'https://photo.jpg'))
# print(account1.create_post('na chile!', 'fdnv','https://photo123.jpg'))
# print(account1.create_post('I was walking', 'weather was wonderfull','https://image.jpg'))

# print(account1.list_posts())
# print(account1.detail_post(2))
# print()
# print(account1.detail_post(3))
# account1.update_post(3, title = 'We were walking!')
# print(account1.update_post(8, title = 'We were walking!'))
# print(account1.detail_post(3))
# print()
# print(account1.delete_post(1))
# print()
# print(account1.list_posts())

# =====================================================================================================================
# Инкапсуляция 
# 1. Связь данных с методами которые ддолжны управлять этими данными
# 2. Механизм при помощи которого можно ограничить доступ одних компонентов программы к другим компонентам(сокрытие данных)

# class Phone:
#     number = '+996 503-503-503'

#     def print_number(self):
#         print(f'Мой номер:{self.number}')
    
# my_phone = Phone()
# my_phone.print_number()

#Инкапсуляция как упрвление доступом
# 3 уровня доступа в Питоне
#   1. Публичный (public) = self.number, def get
#   2. Зaщищенный (protected, parent/child) = _number, def _get
#   3. Приватный (__private, частный. используем ттолько в текущем классе) = _number, def __get


# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.brand = 'BMW' #public
#         self._model = '7 Series' #protected
#         self.__motor = 'ABS' #private

#     def _get_date(self):
#         print('1 September')
# class Audi(Car):
#     pass

# class Auto(Audi):
#     pass

# obj = Auto()
# print(obj._country)

# audi = Audi()
# print(audi.brand)
# print(audi._country)
# print(audi._model)
# # print(audi._Audi__motor)

# car = Car()
# print(car.brand)
# print(car._country)
# print(car._model)
# print(car._Car__motor)
# car._get_date()

# ===================================================================================

# class Phone:
#     username = 'John'
#     _caller = 'Jammie'
#     __count_of_talks = 15

#     def call(self):
#         print(f'{self._caller} звонит вам ')
#         question  = input('Сбросить или взять: yes/no: ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку')
 
#     def __turn_on(self):
#         self.__count_of_talks += 1
#         print('Alo!')
#         print(f'Count of talks with JAmmie {self.__count_of_talks}')

# john = Phone()
# john.call()
# john.call()

# ===================================================================================

# class Person():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def display_info():
#         print(f'My anme is {self.name}, I am {self.age}.')
# obj = Person('James', 18)
# obj.display_info()
# obj.name = 'RAychel'
# obj.age = -18
# obj.display_info()

# #getter & setter
# Они используются для солучения и установка значения чтобы добавить логику валидации(проверки)
# данные которые будут установлены в атрибуты которые имееют защиту 

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     def display_info(self):
#         print(f'Ma name is {self.__name}, and i am {self.__age} years old.')

#     #getter
#     def get_name(self): return self.__name
#     #setter
#     def set_name(self, value):
#         if not isinstance(value, str):
#             raise ValueError('Name must be str object!')
#         self.__name = value

#     def get_age(self):
#         return self.__age

#     def set_age(self, value):
#         if not isinstance(value, int) or not 0 <= value < 150:
#             raise Exception('Invalid value for age')
#         self.__age = value 


# obj = Person('John', 18)
# print(obj.get_age())
# obj.display_info()
# obj.set_age(25)
# obj.display_info()

# ===================================================================================
 
# class Kyrgyzstan:
#     __name = "Kyrgyz Republic"
#     __population = 0

#     def get_population(self): return self.__population

#     def set_population(self, number):
#         if not isinstance(number, int) or number < 0:
#             raise ValueError('The given value is not valid!')
#         self.__population = number

#     def display_population(self):
#         print(f'Population of {self.__name}: {self.get_population()}')

# obj = Kyrgyzstan()
# obj.set_population(7_000_000)
# obj.display_population()

# ===================================================================================
"""Создайте класс MyString, который будет наследоваться от str.
Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Затем, создайте экземпляр example от класса MyString со значением String. 
Добавьте к example строку 'hello' методом append, затем примените метод pop.
"""
# class MyString(str):
#     def __init__(self, value ) -> None:
#         self.string = value 

#     def append(self, value:str):
#          self.string = self.string + value
    
#     def pop(self):
#         removed = self.string[-1]
#         self.string = self.string[:-1]
#         return removed

#     def __str__(self) -> str:
#         return self.string

# obj = MyString('String')
# print(obj)
# obj.append('hello')
# print(obj)
# print(obj.pop())
# print(obj)

""""Напишите класс CustomError который наследуется от встроенного класса исключений Exception.
Переопределите __init__ таким образом чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.
Создайте исключение от этого класса в переменной capitals_error с сообщением:"""
# class CustomError(Exception):
#     def __init__(self, error_name) -> None:
#         self.error = error_name

#     def __str__(self) -> str:
#         return f'{self.error}'

# def check_latters(str1):
#     if str1.isupper():
#         print(f'ВСЕ ОТЛИЧНО!{str1}')
#     else:
#         raise capitals_error

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# print(check_latters("hello"))


