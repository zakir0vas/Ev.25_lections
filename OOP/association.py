# Ассоциация,  Компазиция,  Агрегация
# Все эти три принципа - анологичны! Они озночают что внутри одного обьекта будет существовать другой обьект
# отличаются реализацией

# Композиция 
# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'

# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# obj = Room()
# print(obj.west_wall)

# Ассоциация
# class Stream:
#     pass

# class Logger:
#     def __init__(self) -> None:
#         self.stream = None

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream!')

# logger = Logger()
# logger.print_the_stream() 
# logger.stream = Stream()   - # передается через дургой атрибут 
# logger.print_the_stream()

#  Агрегация
# class Stream:
#     def __str__(self) -> str:
#         return 'Stream object!'

# class Logger:
#     def __init__(self, stream=None) -> None:
#         self.stream = stream

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream!')

# stream = Stream()
# logger = Logger(stream)
# logger.print_the_stream()

# ================================================================
# class Engine:
#     country ='Germany'

#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Power: {self.power}'

# class AudiCar:
#     brand = 'Audi'
#     country = 'Germany'

#     def __init__(self, model, power) -> None:
#         self.engine = Engine(power)
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} -> {self.engine} -> Engine country: {self.engine.country}. Country of car: {self.country}'

# car = AudiCar('A8', 600)
# print(car)






