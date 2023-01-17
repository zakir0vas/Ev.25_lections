# tuple() - кортеж, неизменяемый тип данных
#
# В языке программирования Python ЛИТЕРАЛ – это выражение (или константа), которое создает (генерирует) объект. 
# Если в тексте программы встречается литерал, то для этого литерала создается отдельный объект некоторого типа.

# thistupele = 'apple', 'banana', 'cherry'
# print(thistupele)
# print(type(thistupele))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# not change
# tuple_ = (1, 'h', 3)
# tuple_ [1] = 2
# print(tuple_)

# print(dir(tuple))

# a = 1
# b = 2
# c = 3
# result = (a, b , c)
# print(result)

# new1, new2, new3 = result
# print(new1)
# print(new2)
# # print(new3)

# a  = (1, 2, 3)
# print(a)
# a = list(a)
# a.append(4)
# a = tuple(a)
# print(a)

# tuple_ = (1, 2, 3, 4, 5, 6, 7, 8, 5, 5)
# print(tuple_.count(5))
# print(tuple_.index(7))
#--------------------------------------------------------------
#iputs1
# tuple_ = (1, 2, 3, 4, 5, 6, 8, 8 ,9, 2)
# target = 8
# output:
# result = (8, 3, 4, 5, 6, 8)
# tuple_ = (1, 2, 8, 3, 4, 5, 6, 8, 8, 9, 2)
# target = 8
# if tuple_.count(8) > 1:
#     first = tuple_.index(8)
#     second = tuple_.index(8, first + 1)
#     result = tuple_[first: second + 1]
# else:
#     second = tuple_.index(8)
#     result = tuple_[first:]

# print(result)

#inputs2
# tuple_ = (1, 2, 3, 8, 5, 1, 2)
# target = 8
# output:
# result = (8, 5, 1, 2)
# tuple_ = (1, 2, 3, 8, 5, 1, 2)
# target = 8
# if tuple_.count(8) > 1:
#      first = tuple_.index(8)
#      second = tuple_.index(8, first + 1)
#      result = tuple_[first: second + 1]
# else:
#      second = tuple_.index(target)
#      result = tuple_[first:]

# print(result)
# ____________________________________________________________________________________________________________

# students =(
#     ('Елена', '13', 9, 'Москва'),
#     ('Ольга', '11', 7.9, 'Иваново'),
#     ('Елизавета', '14', 9.1, 'Тверь'),
#     ('Дмитрий', '12', 5.2, 'Челябинск'),
#     ('Максим', '15', 6.1, 'Самара'),
#     ('Николай', '11', 8.7, 'Владивосток'),
#     ('Артур', '13', 5.8, 'Екатеринбург'),
#     ('John', '13', 10, 'WinterFell')
# )
# total_mark = 0
# for student in students:
#     # print(student)
#     total_mark += student[2]

# avg_mark = total_mark / len(students)
# print(avg_mark)

# good_students = []
# for student in students:
#     if student[2] > avg_mark:
#         good_students.append(student[0])

# # print(f'Ученики {',',join(good_students)} в этом семестре хорошо учатся!')
# print(f'Ученики:', ', '.join(good_students), ' в этом семестре хорошо учатся!')

    

# from collections import namedtuple
# Student = namedtuple('Student', 'name age mark city')
# students = (
#    Student('Елена', '13', 7.1, 'Москва'),
#    Student('Ольга', '11', 7.9, 'Иваново'),
#    Student('Елизавета', '14', 9.1, 'Тверь'),
#    Student('Дмитрий', '12', 5.2, 'Челябинск'),
#    Student('Максим', '15', 6.1, 'Самара'),
#    Student('Николай', '11', 8.7, 'Владивосток'),
#    Student('Артур', '13', 5.8, 'Екатеринбург')
# )

