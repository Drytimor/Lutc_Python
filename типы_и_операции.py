# отрицательная индексация
"""
line = 'string'
print(line[len(line)-1]) # g
"""
# неизменяемые объекты
#  - str
#  - int
#  - tuple
#  - frozenset

#  изменяемые объекты
#  - list
#  - set
#  - dict
#  - bytearray


# изменение строки через список
"""
line = 'string'
lst = list(line)
lst[0] = 'S'
line = ''.join(lst)
print(line)  # String
"""

# изменение строки через bytearray
"""
line = bytearray(b'spam')
line.extend(b'egg')
print(line) # bytearray(b'spamegg')
print(line.decode()) #  spamegg
"""
# методы строк возвращают новый объект
"""
line = 'string'
print(id(line))
# 4390204600
line = line.replace('s', 'S')
print(id(line))
# 4381530416
line = line.rpartition('i')
# ('Str', 'i', 'ng')
print(line)
line = ''
print(help(line.replace))
"""
"""
M = 3
N = 3
mtx = []
for i in range(M):
    mtx.append([0]*N)

for i in range(M):
    for j in range(N):
        mtx[i][j] = 1

print(mtx)
"""
"""
mtx = [[row for row in range(1, 4)] for col in range(3)]
for i in mtx:
    print(i)

print('-'*10)

col2 = [row[1] for row in mtx]

print(col2)
"""
# списковые включения
# list
"""mtx = [[row for row in range(1, 4)] for col in range(3)]"""
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# dict
"""dict_ = {key: value for key, value in [('bob', 24), ('lee', 20)]}"""
# {'bob': 24, 'lee': 20}
# set
"""set_ = {i for i in range(10) if i % 2 ==0}"""
# {0, 2, 4, 6, 8}

# итерируемый объект - объект который имеет сохраненную последовательность [1,2,3] в памяти
# либо генерируемую последовательность (i for i in range(10)) у обоих реализован протокол итерации
# объект файл тоже является итерируемым объектом
# цикл for задействует протокол итерации

# множества
"""
a = {1,2,3}
b = {1,2,3,4}
"""
# & пересечение множеств {1,2,3}
# ^ разность множеств {4}
# | объединение множеств {1,2,3,4}
# множества хранит только неизменяемые типы данных "хэшируемые"
# неизменяемое множество - frozenset тоже может входить во множество

# в списках порядок имеет значение при сравнении
"""
lst = [1,2,3,4]
lst1 = [1,4,3,2]
print(lst == lst1)
False
"""
# во множестве порядок не имеет значение при сравнении
"""
lst = [1,2,3,4]
lst1 = [1,4,3,2]"""
# преобразуем список во множество
"""
print(set(lst) == set(lst1))
True
"""
# объект хранит в себе тип объекта и количество ссылок на него
"""
import sys
print(sys.getrefcount(1)) # 1000000155"""


# строки
# неявная конкатенация
"""
title = "hello"' '"my"' '"friend"
print(title)"""

# f - строки
"""
import datetime
name = 'lee'
age = 20
money = 100000"""
"""
print(f'{name=}, {age=}')"""
# name='lee', age=20
"""
print(f"{money=:,d}")"""
# money=100,000
"""today = datetime.datetime.now()"""
"""
print(f"{today:%Y-%m-%d %H:%M:%S}")"""
# 2023-09-02 08:44:4
"""from math import pi
b = 202020"""
"""
print(f"{pi:.3f}")"""
# 3.142
"""
print(f'{b:*^20,d}')"""
# ******202,020*******
"""
perc = 35/64
print(f'{perc:.2%}')"""
# 54.69%
"""
greetings = 'hello'
print(f'{greetings:>10}')"""
#      hello
"""
print(f'{greetings:<10}friend')"""
# hello     friend
"""
big_num = 1000000004
print(f'{big_num:,}')"""
# 1,000,000,004
"""
num = 2343552.6516251625
print(f"{num:,.3f}")"""
# '2,343,552.652'

# dict
# ключи словаря уникальны и поддерживают те же методы, что и множества
"""
dict_1 = {key: value for key,value in zip(['a','b','c'],[1,2,3])}
dict_2 = {key: value for key,value in zip(['a','b','c','d'],[1,2,3,4])}
print(dict_1.keys() & duct_2.keys())
# результатом будет set а не dict
dict_3 = dict_1.keys() ^ dict_2.keys()
"""
# при использовании операций множеств ^ & |, у словарей с вызовом метода items()
# можно создавать новые словари
# с учетом того что значения хэшируемые, то есть неизменяемые
"""
dict_1 = {key: value for key,value in zip(['a','b','c'],[1,2,3])}
dict_2 = {key: value for key,value in zip(['a','b','c','d'],[1,2,3])}
dict_3 = dict_1.items() ^ dict_2.items()
print(type(dict_3))
print(dict(dict_3))"""

# именованный кортеж namedtuple
# представляет собой гибрид кортежа/класса/словаря
"""
from collections import namedtuple

rec = namedtuple('user',['name', 'age','jobs'])
bob = rec('bob', 20, 'work')"""
# можно обращаться по атрибуту
"""print(bob.name)"""  # bob
# по индексу
"""print(bob[1])"""  # 20
# можно преобразовать в словарь
"""print(type(bob._asdict()))"""

# file
# в файл записываются только строки которые необходимо заранее преобразовать
# переносы строк нужно прописывать вручную
"""
x,y,z = 10,20,30
list = [1,2,3]

f = open('datafile.txt', 'w')
f.write((f'{x}\n{y}\n{z}\n'))
f.write(str(list))
a = 'asdd'
for i in open('datafile.txt').read():
"""
#    strip() удаляет \n
""" 
    a += i.strip()
print(a)"""

"""
line = open('datafile.txt').readline()
print(line) """  # [1, 2, 3] является строкой
# eval() трактует строку как объект Python
"""
list_python = eval(line)
print(list_python, type(list_python))"""  # [1, 2, 3] <class 'list'>

# модуль pickle
# записывает и читает файл без предварительного преобразования в строки и использования eval()
"""import pickle"""
"""
dict_ = {'name': 'lee', 'age': 20}
f = open('datafile.pkl', 'wb')
"""
# picle преобразовал словарь в строку
"""
pickle.dump(dict_, f)"""
"""
f = open('datafile.pkl', 'rb')"""
# picle преобразовал строку в словарь
"""
pic = pickle.load(f)
print(type(pic), pic) """
"""
import copy

lee = {'name':'lee', 'hobby': [1,2,3,4]}
# метод deepcopy() создает полную копию объекта со всей его вложенности 
bob = copy.deepcopy(lee)
"""

# сравнение
#  == сравнивает эквивалентность значений
# is проверяет идентичность объектов, то есть являются ли объекты на самом деле одним и тем же
# (распологаются по одному адрессу в памяти)
"""
lst = [1,2,3,6]
lst1 = [1,2,3,5]
print(lst>lst1)
"""
# сравнение словарей на < / > возможно только с отсортированными ключами
"""
d = {'a': 1, 'b': 10}
d1 = {'a': 1, 'b': 3}
print(sorted(d) > sorted(d1))
"""

"""
l = [1,2,3]"""
# создается новый объект
"""
x = l * 4
l.append(4)"""
"""
print(id(l), l, id(x), x)"""
# [1, 2, 3, 4] 4543371328 [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] 4543430080
"""
l = [1,2,3]
l.append(4)"""
# создается новый объект который содержит ссылки на созданный раннее объект
# изменение списка L повлияет на вложенные списки у списка x
"""
x = [l] * 4
print(l, id(l), x, id(x))"""
# решение
"""
l = [1,2,3]"""
# создается полностью новый объект с уникальностью во всех уровнях вложенности
"""
x = [list(l) for i in range(4)]
print(l, id(l), x, id(x))
l.append(4)"""
"""
print(l, id(l)) """  # [1, 2, 3, 4] 4532459584
"""
print(x[0], id(x[0]))"""  # [1, 2, 3] 4531972992

"""
t = (4,5,6)

t1 = (1,) + t[1:]
print(t1)"""
"""
l = [1,2,4,5,6,7]
l[5] = 2
c = l[-1: 1000]"""
# ! IndexError: list assignment index out of range
"""l[3:1] = '?'"""
# [1, 2, 4, '?', 5, 6, 2]
"""
x = 'spam'
y = 'eggs'
print(x, id(x), y, id(y))"""
# появляется кортеж (x, y)
# затем кортеж меняет последовательность (y, x)
"""
x, y = y, x
print(x, id(x), y, id(y))"""
"""
l = [1,2,4,5,6,7]
c = [8, 9, 10]
"""
# при конкатенации списков, кортежей, множеств, строк создается новый объект
"""
x = l + c
print(x, id(x))
print(l, id(l))
print(c, id(c))"""
# [1, 2, 4, 5, 6, 7, 8, 9, 10] 4528366144
# [1, 2, 4, 5, 6, 7] 4528625728
# [8, 9, 10] 4528684480
"""
d = {'name': 'lee', 'age': 20}
d1 = {'city': 'spb'}
d2 = d | d1
print(d2, id(d2))
print(d, id(d))
print(d1, id(d1))"""
# {'name': 'lee', 'age': 20, 'city': 'spb'} 4341257280
# {'name': 'lee', 'age': 20} 4340229632
# {'city': 'spb'} 4340161024
"""
a = (1,2)
c = (3,4)
v = a + c
print(a, id(a))
print(c, id(c))
print(v, id(v))"""
# неупорядоченные коллекции данных не поддерживают конкатенацию, срезы, индексацию
"""
a = {1, 2}
c = {3, 4}
v = a | c
print(a, id(a))
print(c, id(c))
print(v, id(v))"""
# объедение словарей и множеств выполняется с помощью методов множеств | ^ &
#  | - объединение
#  ^ - разность
#  & - пересечение
"""
a = {1, 2, 4}
c = {3, 4}
v = a & c
print(v, id(v))"""
"""
a = [1,2,3,4]
# print(a, id(a))
b = [5,6,7,8]
# print(b, id(b))
b[:0] = a
# print(b, id(b))
# [1, 2, 3, 4, 5, 6, 7, 8]

a.extend(b)
# print(a, id(a))

# [1, 2, 3, 4, 5, 6, 7, 8]
"""
"""
a = [1,2,3]
b = [4,5,6]
a = a + b
print(a)
"""
"""
a = (1,2,3)
b = (4,5,6)
a[:0] = b"""
# TypeError: 'tuple' object does not support item assignment

# срезы поддерживают только упорядоченные коллекции
# присвоение по индексации поддерживают только изменяемые типы данных
# конкатенацию поддерживают все последовательности - list, tuple, str
# dict и set так же соединяются, но по методам множеств
# при конкатенации списков, кортежей, множеств, строк создается новый объект

# list
"""
a = [1,2,3,4]
print(a, id(a))"""  # [1, 2, 3, 4] 4379516864
"""
a = a + [5,6,7]
print(a, id(a))"""  # [1, 2, 3, 4, 5, 6, 7] 4380632064

# tuple
"""
a = (1,2,3,4)
print(a, id(a))"""  # (1, 2, 3, 4) 4323330624
"""
a = a + (5,6,7)
print(a, id(a))"""  # (1, 2, 3, 4, 5, 6, 7) 4322908704

# set
"""
a = {1, 2, 3, 4}  
print(a, id(a))"""  # {1, 2, 3, 4} 4498756032
"""
a = a | {5, 6, 7}  
print(a, id(a))"""  # {1, 2, 3, 4, 5, 6, 7} 4498757824

# dict
"""
a = {'name': 'lee'}
print(a, id(a))"""  # {'name': 'lee'} 4299971328
"""
a = a | {'age': 20}
print(a, id(a))"""  # {'name': 'lee', 'age': 20} 4300702080

# str
"""
a = 'hello'
print(a, id(a)) """  # hello 4421882032
"""
a = a + ' friend'
print(a, id(a))"""  # hello friend 4421883888
