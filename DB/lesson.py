# PostgresSQL - Система управления базами данных (СУБД/BDMS)
# Это ряд программ и инструментов позволяющих создать БД управлять ею манипулировать данными внутри БД(CRUD)

# Postgres - Сама база данных, она обьекта-реалиционная, то есть данных хранятся в виде таблиц и таблицы имеют связь между собой(relations)

# SQL(Structured Query Language) - декларитивный язык структурированных запросов, он применяется для создания и получения данных при помощи запросов в БД

# ==============================================================================================
# Типы полей в Postgres:

# # 1. Numeric types: 
#         a. smallint(2 bytes) -> -32767 to 32767
#         b. integer(4 bytes) -> -214000 ro 2140000
#         c. begint (8 bytes) -> ...
#         d. serial (4 bytes) -> auto-incriment
#         e. reak(4 bytes) -> число с плавающей точкой, вещественное число
#         f. double precision(8 bytes) -> real но только с двойной точкой.

# 2. Character types(Строковые типы):     
        # a. varchar(кол-во 255 символов) - можем укаазать максимальное кол-во символов.Если мы указали мак кол-во символов в 50.
        #    -заполнили только 4 = остальные 46 остануться пустыми.
        # b. char (255) - Если не заполним все символы то остальные заполняться пробелами (white space) 

# 3. Boolean types:
#       boolean(1 byte) -> True/False4

# (Дополнительные)Самопроизвольные
#  4. Date -  календарная дата (год.месяц.день)
# 5. Location - координатная точка -> (245, -12 (x, y))
# ==============================================================================================
 
#### ubuntu: sudo -u postgres psql -> команда для входа в прогрес через корневого пользователя postgres
# psql -> Для вхожа в СУБД через своего юзера 

# \q -> Выход из СУБД

# \du -> Список всех юзеров

# \l -> Список всех баз данных

# \c  (dbname) -> команда подключения в БД
#     \dt -> список всех таблиц в БД 

# \d <dbname> -> подробная информация про БД


#### Импорт данных:
# psql -U <ваш юзер нэйм> -d <база данных создайте предварительно> -f <путь до файла>
 
# CREATE USER <username> WITH PASSWORD <password>; -> команда ждя создания юзера

# ALTER USER <username> WITH SUPERUSER; -> команда для изменения статуча юзера на суперюзера

# SELECT <row/column> FROM <tablename>; 
    #  * (ALL)
# -> Команда для получения данных их таблиц
# ============================================================================================================================================

# WHERE: используется для фильтрации по полям. Будут выводиться только те данные которые соответсвуют условию опера WHERE
## Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему-либо'

# BETWEEN: Условия "между"
# SELECT * FROM products WHERE id BETWEEN 3 and 8;
# AND: оператор и, для множества условий

# LIKE: выводит результат который соответсвует введенному шаблону для строк.Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра 

# ORDER BY: Сортировка по входящим данным по убываю или возрастанию.
            # ASC(по возрвствнию) и  DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <ROW> [ASC/DESC]

# Агригационные функции - AVG(), COUNT(), MIN(), MAX(), SUM()
# AS (если)
