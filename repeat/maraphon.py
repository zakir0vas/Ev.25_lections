# def kv(a):
#     perim = a * 4
#     plosh = a ** 2
#     diag = a * (2 ** 0.5)
#     return f'Периметр: {perim}, Площадь: {plosh}, Диагональ: {diag}'

# print(kv(4))


# a = list(1234)

# for i in a:
#     max_=max(a)
#     print(a)


# a = 1234
# a = str(a)
# list_ = a.split()
# per = list_[0]
# pos = list_[-1]
# ser = list_[1:-1]
# print()





day = int(input())
month = int(input())
year = int(input())
if year < 2022:
    if month < 12:
        if day < 31:
            print(f'{day}.{month}.{year}')
else:
    print('Nevernie dannie') 
