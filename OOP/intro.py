#ООП - обьектно-ориентированное программирование

#Класс- Описание того как должен выглядет обьект, то есть в классе мы описываем какими свойствами(данными)
#и поведением должен обладать обьект (Экземпляр)

# Обьект- Это сущность (элемент) которые мы создаем от класса, у обьекта есть собственное состояние свойств(данных)

# Свойства(фтрибуты)- называют обычные переменные в классе в которых хранятся данные определенного обьекта

# Поведение - это обычные функции которые описываю поведения обьекта, функции внутри класса называют - методами.

# kirk = {'name': 'Kirk McDack', 'age': 34, 'job': 'Captain', 'salary': 2000}
# snow = {'name': 'John Snow', 'age': 24, 'job': 'Police officer', 'salary': 1500}
# mccoi = {'name': 'leonard Mccoi', 'age': 18, 'job': 'Chief', 'salary': 1000}
# print(F'Name:{kirk["name"]}\nAge: {kirk["age"]}\njob: {kirk["job"]}]nSalary: {kirk["salary"]}')
# print(F'Name:{snow["name"]}\nAge: {snow["age"]}\njob: {snow["job"]}]nSalary: {snow["salary"]}')
# print(F'Name:{mccoi["name"]}\nAge: {mccoi["age"]}\njob: {mccoi["job"]}]nSalary: {mccoi["salary"]}')

# ===============================================================
# class Human:
#     def __init__(self, first_name, last_name, age, job, salary):
#         """Здесь описываются атрибуты обьекта"""
#         self.name = first_name + " " + last_name
#         self.age = age
#         self.job = job
#         self.salary = salary
    
#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}'
# kirk = Human('James', 'Kirk', 34, 'Captain', 2000 )
# snow = Human('John', 'Snow', 24, 'Officer', 1500)
# mccoi = Human('Leonard', 'McCoi', 30, 'Chief', 1000)

# print(kirk.name)
# print(snow.name)
# print(mccoi.name)

# print(kirk.show_info())
# print()
# print(snow.show_info())
# print()
# print(mccoi.show_info())

# ===============================================================

# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name, colour ) -> None:
#         """Иннициализатор, именно здесь создаются аттрибуты обьекта от класса"""
#         self.name = name    #аттрибуты обьекта(экземпляра) от класса
#         self.colour = colour

# bobik = Dog('Bobik', 'Brown')
# yumi = Dog(name='Yumi', colour='yellow')
# aktosh = Dog('Aktosh', 'gray')

# print(f'name: {bobik.name}, age: {bobik.age}, colour: {bobik.colour}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, colour: {yumi.colour}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, colour: {aktosh.colour}, ushi: {aktosh.ushi}')

# bobik.age = 5
# yumi.age = 2.5
# aktosh.age = 12
# aktosh.ushi = False

# print('After:')
# print(f'name: {bobik.name}, age: {bobik.age}, colour: {bobik.colour}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, colour: {yumi.colour}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, colour: {aktosh.colour}, ushi: {aktosh.ushi}')

#  ===================================================================

# class Human:
#     age = 0

#     def __init__(self, name, weight, nationality) -> None:
#         self.name = name 
#         self.weight = weight 
#         self.nation = nationality

#     def birthday(self):
#         import random
#         print(f'\nHappy Birthday, {self.name}!')
#         self.age += 1
#         self.weight += random.randint(3, 7)

# human1 = Human('John Snow', 3.7, 'american')
# human2 = Human('Abu-Bakr', 3, 'Arabian')

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After 1 year')
# human1.birthday()
# human2.birthday()

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After 5 month')
# human1.birthday()

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# ===================================================================
"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная 
переменная класса - процент налога от зарплаты - 15%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. 
Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. 
Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     tax = 0.10

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
    
#     def get_tax(self):
#         res = (self.salary * self.tax) * (12 * self.experience)
#         print(f'Сумма налога составила {res} сомов, за {self.experience} лет работы!')
        
# obj1 = Salary(35000, 13)
# obj1.get_tax()

# obj2 = Salary(150_000, 13)
# obj2.get_tax()


# ===================================================================
# Закрепление задач

