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


















