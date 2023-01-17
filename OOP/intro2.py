# class Student:
#     univer = 'MIT'
#     def __init__(self, first_name, last_name)-> None:
#         self.name = first_name + ' ' + last_name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_point(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             self.is_ready_to_work = True
#             print(f'{self.name} is ready to work!')

#     def ready_book(self, book):
#         self.add_point(50)
#         self.books.append(book)
    
#     def do_lab_works(self):
#         self.add_point(50)

#     def lear_new_languages(self, languages, score):
#         if score in range(60, 101):
#             self.add_point(1000)
#             self.languages.update({languages: score})
#         else:
#             raise Exception('Invakid score for languages!')


# st1 = StopAsyncIteration('James')
# st2 = StopAsyncIteration('Rachel')
# print(st1)
# print(st2)

# print(f'Befor study {st1.name}:\nBooks: {st1.books}\nlanguages: {st1.languages}\nKNowledge:{st1.knowledge},{st1.is_ready_to_work}.')

# st1.read_book('Martin Iden')
# st2.read_book('Eugene Onegin')

# st1.learn_new_language('Python', 100)
# st1.do_lab_works()
# st1.real_projects()
# st1.learn_new_language('JS', 80)
# st1.do_lab_works()
# st1.real_project

# =================================================================================================

# class Car:
#     def __init__(self, abc) -> None:                        #Дондер методы 
#         print('Запустился')
#         print(abc)

# a = Car('John Snow')

# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
#     def __str__(self) -> str:
#         return f'{self.brand} {self.model}'

# a = Car('BMW', '7 series')
# print(a)
# b = Car('Mersedes-Benz', 'w140')
# print(b)

# =================================================================================================

# class Soda:
#     def __init__(self, ingredient: str=None):
#         ### if isinstance(ingredient,str):
#         if type (ingredient) != str:
#             self.ingredient = None
#         else:
#             self.ingredient = ingredient
        
#     def print_my_drink(self):
#         if self.ingredient:
#             print(f'Газировка со свкусом {self.ingredient}')
#         else:
#             print('Обычная газировка')

# drink1 = Soda('Grusha')
# drink1.print_my_drink()

# drink2 = Soda()
# drink2.print_my_drink()

# drink3 = Soda([123])
# drink3.print_my_drink()

# =================================================================================================

# [5,6,7] - True  [1,2,6] - False треугильник
# 
# class TriangleCheker:
#     def __init__(self, sides: list) -> None:
#         self.sides = sides

#     def __str__(self) -> str:
#         if not all(isinstance(x, (int, float)) for x in self.sides):
#             return 'Нельзя построить треугольник! Так как все стороны должны быть числами!'
#         if any(x <= 0 for x in self.sides):
#             return 'Нельзя построить треугильник! Так как все стороны должны быть больше нуля!'
#         self.sides.sort()
#         if self.sides[0] + self.sides[1] <= self.sides[-1]:
#             return 'Нельзя построить треугольник! Так как сумма двух сторон меньше самой длинной стороны!'

# t1 = TriangleCheker([19, 8, 6])

# print(t1)
# print(TriangleCheker([5, 6, 7]))
# print(TriangleCheker([5, 6, '7']))
# print(TriangleCheker([5, 6, -1]))
# print(TriangleCheker([3, 2, 4]))