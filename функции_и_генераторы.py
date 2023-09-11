# Области видимости
# - встроенная
# - глобальная
# - объемлющая
# - локальная

# изменяемый объект в глобальной области
# изменяется без ключевого слова global
# что бы изменить неизменяемый объект нужно иcпользовать ключевое слово global

"""
lst = [1,2,3]
tuple_ = (1,2,3)
tuple_2 = (1,2,3)
def lst_func():
"""


# изменяемый тип передает ссылку на объект
""" x = lst"""
    # неизменяемый тип передает копию объекта
""" y = tuple_"""
    # tuple_2 теперь будет глобальным объектом
""" global tuple_2
    x.append(4)
    y += (4,)
    tuple_2 += (4,)
    return x, y, tuple_2"""

"""
print(lst_func())"""  # ([1, 2, 3, 4], (1, 2, 3, 4), (1, 2, 3, 4))
"""
print(lst, tuple_, tuple_2)"""  # [1, 2, 3, 4] (1, 2, 3) (1, 2, 3, 4)
# LEGB
# поиск:
# локальная
# объемлющая
# глобальная
# встроенная
"""
global_var = 30
def inner():
    inner_var = 20
    def local():
        local_var = 10
        print(local_var)  # 10
        print(inner_var)  # 20
        print(global_var)  # 30
    return local

fun = inner()
fun()
"""

# замыкания
# maker просто генерирует функцию и возвращает ее,
# не вызывая
"""
def maker(n):
    def action(x):
        return x ** n
    return action
"""
# создается область видимости где maker имеет аргумент n = 2
"""
fun1 = maker(2)"""
# fun1 является ссылкой на action, а 2 сохранилась область видимости maker
"""
print(fun1)"""
# <function maker.<locals>.action at 0x109c84fe0>
# через fun1 мы получаем доступ к action и передаем ей 3
"""
print(fun1(3))"""
# 9
# action запомнила число 2 и возвратила итог операции 2 ** 3
# создается другая область видимости где maker имеет аргумент n = 3
"""
fun2 = maker(3)
print(fun2)"""
# <function maker.<locals>.action at 0x10caf0680>
"""
print(fun2(3))"""
# 27
# # action запомнила число 3 и возвратила итог операции 3 ** 3
"""
def func():
    x = 4"""
    # lambda видит все переменные существующие в функции
""" action = lambda n: x ** n
    return action
func = func()
print(func(2))
"""
"""
def makeAction():
    acts = []
    for i in range(5):"""
        # i будет ссылаться на значение последней итерации цикла - 4
"""     acts.append(lambda x: i ** x)
    return acts

acts = makeAction()"""
"""
print(acts[0](2))"""  # 16
"""
print(acts[1](2))"""  # 16
"""
print(acts[2](2))"""  # 16
"""
def makeAction():
    acts = []
    for i in range(5):"""
        # в lambda нужно передавать текущее значение переменной i
"""     acts.append(lambda x, i=i: i ** x)
    return acts
"""
"""
acts = makeAction()"""
"""
print(acts[0](2))"""  # 0
"""
print(acts[1](2))"""  # 1
"""
print(acts[2](2))"""  # 4
"""
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested
"""
# область видимости f
"""
f = tester(0)"""
# start = 0
# <function tester.<locals>.nested at 0x104ef8fe0>
"""
f('spam')"""  # spam 0
"""
f('spam')"""  # spam 1
"""
f('spam')"""  # spam 2

# область видимости f2
"""
f2 = tester(10)"""
# start = 10
# <function tester.<locals>.nested at 0x105614680>
"""
f2('back')"""  # back 10
"""
f2('back')"""  # back 11
"""
f2('back')"""  # back 12
"""
def tester(start):
    def nested(label):"""
# SyntaxError: no binding for nonlocal 'state' found
#       нелокальные переменные должны сначала быть объявленные ранее
"""     nonlocal state
        print(label, state)
        state += 1
    return nested
"""

"""
def tester(start):
    def nested(label):"""
        # глобальные переменные можно объявлять до их присвоения
"""     global state
        state = 10
        print(label, state)
        state += 1
    return nested
"""

# замыкания с помощью атрибутов функции без использования nonlocal
"""
def tester(start):
    def nested(label):
        print(label, nested.state)

        nested.state += 1"""
""" nested.state = start"""  # инициализация переменной после определения функции
""" return nested"""
"""
f = tester(0)
f('spam')"""  # 0
"""
f1 = tester(10)
f1('msg')"""  # 10
"""
var_int = 10
var_list = [1,2]
def test(x, y):"""
    # x является числом, поэтому создал новый объект
    # y является списком, поэтому изменил объект
""" x = 20
    y.append(3)"""
    # чтобы не изменять сам объект нужно создать копию
""" y = y[:]
    y.append(3)
    print(x)
    print(y)"""
"""
test(var_int,var_list)
print(var_int)
print(var_list)
"""
"""
def test(a, *args, x=None, **kwargs):
    print(a)
    print(args)
    print(x)
    print(kwargs)

test(10, (1,2,3,4), name='lee', age=20)
"""
"""
def test (a,b,c):
    print(a, b, c)
tuple_ = (1,2,3) 
dict_ = {'a': 4, 'b': 5, 'c': 6}"""
"""
test(*tuple_)"""  # 1 2 3
"""
test(**dict_)"""  # 4 5 6
"""
def min(*args):
    res = args[0]
    for i in args[1:]:
        if res > i:
            res = i
    return res

print(min([1,2], [3,4], [1,1]))"""
"""
def min(first, *args):
    for i in args:
        if first > i:
            first = i
    return first
"""
# в first автоматически попадает первый элемент
"""
print(min(1,1,1,1,1,1))"""
"""
def minmax(test, *args):
    res = args[0]
    for i in args[1:]:
        if test(i, res):
            res = i
    return res

def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y

print(minmax(lessthan, 3,2,1))
"""
"""
def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

s1, s2, s3 = 'spam', 'scam', 'slam'
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res
"""

# print(intersect(s1,s2, s3))
# print(union(s1,s2, s3))
"""
def tester(func, items, trace=True):
    for i in range(len(items)):"""
        # на каждой итерации ставит первый объект в конец
"""     items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))"""

# реализация функции print
"""
import sys
def print3(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
"""
# отличие в том что при заданных стандартных параметрах
# в функцию можно будет передать только определенные в этой функции аргументы
# а, в **kwargs можно пережать любое значение

# передача аргументов только по ключевым словам
"""
def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
 """

# рекурсия
"""
def mysum(lst):
    if not lst:
        return 0
    return lst[0] + mysum(lst[1:])

print(mysum([1,2,3,4]))
"""

# любой тип при наличии одного элемента
"""
def mysum(l):
    return l[0] if len(l) == 1 else l[0] + mysum(l[1:])

print(mysum(('1','1', '12')))
"""
"""
def mysum(l):
    first, *args = l
    print(first, args)
    return first if not args else first + mysum(args)

print(mysum(open('datafile.txt')))
"""
"""
<<<<<<< HEAD
=======
def my_sum(l):
    first, *args = l
    return first if not args else first + my_sum(args)

print(my_sum({1,2,3,4,5}))"""
"""
l = [1, [2, [3, 4], 5], 6, [7, 8]]
>>>>>>> CH_2
def sumtree(l):
    tot = 0
    for x in l:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
<<<<<<< HEAD
print(sumtree(l))"""


"""
>>>>>>> CH_2

# очередь с обходом в ширину
# FIFO первым пришел - первым обслужен
"""

"""
# print(sumtree_FIFO(l))

# стек с обходом в глубину
# LIFO последний пришел - первым обслужен
"""

"""

# стек с обходом в глубину
# LIFO последний пришел - первым обслужен

"""

"""
# print(sumtree_LIFO(l))

=======

print(sumtree_LIFO(l))
"""
# абстракции FIFO и LIFO относятся к работе со списком(данными), только разница не в самом списке(данных),
# а в правилах доступа к нему

# FIFO объект добавляется на одном конце списка(данных), а выполнение операций происходит на другом конце
# это понятие очереди: первым пришел - первым обслужен

# LIFO добавления объекта и выполнения над ним операции происходит на одном конце списка(данных)
# это понятие стека: последний пришел - первым обслужен


#  функции

# имя функции это ссылка на объект
"""
def echo(msg):  
    print(msg)"""

"""
print(id(echo))"""  # 4356344224

"""
echo_1 = echo"""  # echo_1 тоже ссылается на объект функции

"""
print(id(echo_1))"""  # 4356344224

# передача функции как аргумент
"""
def echo(msg):
    print(msg)

def indirect(func, arg):
    func(arg)

indirect(echo, 'Argument call')

"""

# помещение функции в структуру данных
"""
def echo(msg):
    print(msg)

schedule = [(echo, 'spam'), (echo, 'message')]
for (func, args) in schedule:
    func(args)

reminder = {
    'spam': echo('spam'),
    'msg': echo('message')
}
"""
# замыкание
"""
def make(label):
    def echo(message):
        print(f'{label}: {message}')
    return echo

f = make('spam')
f('Hello')
"""
"""
def func(a):
    b = 'spam'
    return b * a
"""
"""print(func.__name__)"""  # func
"""print(dir(func))"""  # ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__']
"""print(func.__code__)"""  # <code object func at 0x100bb9550, file "/Users/dry/Lutc_python/функции_и_генераторы.py", line 468>
"""print(func.__code__.co_varnames)"""  # ('a', 'b')
"""print(func.__code__.co_argcount)"""  # 1

# в функции можно добавлять собственные атрибуты
"""
func.count = 1
print(func.count)"""  # 1

# lambda
# лямбда это выражение, а не оператор
# значит ее сразу можно помещать в структуру данных
# предварительно не объявив
# def это оператор вставить напрямую в структуру данных его не получиться

# чтобы описать такой код с оператором def
# нужно будет предварительно в файле объявить 3 функции
# __кодовая близость__
"""
reminder = {
    'already': lambda: 2 + 2,
    'got': lambda: '2'+'2',
    'one': lambda: {1, 2} | {3, 4}
}
key = reminder['one']
print(key())"""  # {1, 2, 3, 4}


# Функциональность lambda
# lambda поддерживает тернарный оператор
"""
lower = lambda x, y: x if x < y else y
print(lower(2,3))"""  # 2

# циклы в lambda можно организовать с помощью map и list comprehension

# map
"""
from math import sqrt
num = [1,4,9]
square = lambda x: list(map(sqrt, x))
print(square(num))"""  # [1.0, 2.0, 3.0]

# list comprehension
"""
square = lambda x: [i**2 for i in x]
num = [1,2,3,4]
print(square(num))"""  # [1, 4, 9, 16]

# lambda часто используются в обработчиках обратного вызова
"""
import sys
from tkinter import Button, mainloop

x = Button(
    text='Press me',
    command=lambda: sys.stdout.write('spam\n')
)
x.pack()
mainloop()
"""

# map
# map менее универсальна чем list comprehension
"""
map_object = list(map(lambda x: x**2, [1,2,3]))
print(map_object)  # [1, 4, 9]
"""
# list comprehension
# так же если добавить круглые скобки, то получится генератор
# который не расходует память
"""
lcm_object = [x**2 for x in [1,2,3]]
print(lcm_object)"""  # [1, 4, 9]

# filter
# принимает функцию, которая должна возвращать булевское значение и итерируемый объект
# все значения в итерируемом объекте будут проходить через булевскую функцию.
# функция filter проходится по итерируемому объекту и возвращает итерируемый объект
# из значений которые оказались True, посредством передаваемой булевской функции в filter
"""
filter_object = list(filter(lambda x: x > 0, range(-5,5)))
print(filter_object)"""  # [1, 2, 3, 4]

# так же можно использовать списковое включение
"""
lcm_object = [x for x in range(-5,5) if x > 0]
print(lcm_object)"""  # [1, 2, 3, 4]

# reduce
# модуль functools, operator
# принимает функцию и итерируемый объект
# возвращает результат
# функция в reduce должна принимать 2 аргумента
"""from functools import reduce"""
"""
reduce_object = reduce(lambda x, y: x+y, range(1,5))
print(reduce_object)
"""
# reduce под капотом
"""
def my_reduce(func, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = func(tally, next)
    return tally
"""
# модуль operator
# предлагает функции соответствующие reduce
"""
import functools, operator

reduce_object = functools.reduce(operator.add, range(5))
print(reduce_object)"""  # 10

# цикл for
# сбор результатов вручную
"""
res = []
for x in 'spam':
    res.append(ord(x))
print(res)"""  # [115, 112, 97, 109]

# map
# применение функции к последовательности
# map обязательно требует функцию
"""
res = list(map(ord, 'spam'))
print(res)"""  # [115, 112, 97, 109]

# list comprehension
# применение выражения к последовательности
"""
res_1 = [ord(x) for x in 'spam']"""  # в списковое включение
# в list comprehension можно вставлять любое выражение
"""
res_1 = [x**2 for x in range(5)]
print(res) """ # [115, 112, 97, 109]

# list comprehension в ряде случаев оказывается быстрее чем map filter,
# и поддерживает более функциональную возможность и простоту написания кода

"""
res = [x + y for x in [0,1,2] for y in [10, 20, 30]]
print(res)
"""
# эквивалент
"""
res = []
for x in [0,1,2]:
    for y in [10,20,30]:
        res.append(x+y)

print(res)
"""

# комбинирование четных и нечетных чисел в кортеже
"""
res = [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res)"""  # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

# эквивалент
"""
res = []
for x in range(5):
    if x%2 == 0:
        for y in range(5):
            if y%2 == 1:
                res.append((x,y))"""
"""
print(res) """  # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

# Matrix
"""
N = 3
M = 3

mrx = [[row for row in range(1, N+1)] for col in range(M)]
print(mrx)"""  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#  эквивалент
"""
res = []
for col in range(M):
    temp = []
    for row in range(1, N+1):
        temp.append(row)
    res.append(temp)

print(res)"""  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""
N = 3
M = 3

mrx = [[row for row in range(1, N+1)] for col in range(M)]
print(mrx)"""  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

"""
col_2 = [row[1] for row in mrx]
print(col_2)"""  # [2, 2, 2]

"""
print(mrx[1][1])"""  # 2

# диагональ
"""
diag = [mrx[i][i] for i in range(len(mrx))]  
print(diag)"""  # [1, 2, 3]

# изменение матрицы путем создания новой
"""
new_mrx = [[col + 10 for col in row] for row in mrx]
print(new_mrx)"""


"""
mrx_1 = [[row for row in range(1, 4)] for col in range(3)]"""  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""
mrx_2 = [[row for row in range(4, 7)] for col in range(3)]"""  # [[4, 5, 6], [4, 5, 6], [4, 5, 6]]

"""
mrx_3 = [[mrx_1[row][col] * mrx_2[row][col] for col in range(len(mrx_2))] for row in range(len(mrx_2))]"""  # [[4, 10, 18], [4, 10, 18], [4, 10, 18]]
#  эквивалент
"""
res = []
for row in range(len(mrx_2)):
    temp = []
    for col in range(len(mrx_2)):
        temp.append(mrx_1[row][col] * mrx_2[row][col])
    res.append(temp)
"""
# [[4, 10, 18], [4, 10, 18], [4, 10, 18]]

# zip
"""
mrx_1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
mrx_2 = [[4, 5, 6], [4, 5, 6], [4, 5, 6]]

res = [[col_1 * col_2 for col_1, col_2 in zip(row_1, row_2)] for row_1, row_2 in zip(mrx_1, mrx_2)]"""  # [[4, 10, 18], [4, 10, 18], [4, 10, 18]]
#  эквивалент
"""
res = []
for row_1, row_2 in zip(mrx_1, mrx_2):
    temp = []
    for col_1, col_2 in zip(row_1, row_2):
        temp.append(col_1 * col_2)
    res.append(temp)"""
# [[4, 10, 18], [4, 10, 18], [4, 10, 18]]

# Генераторы
"""
def gensquares(x):
    for i in range(x):
        yield i ** 2"""
# <function gensquares at 0x10d9649a0>

"""
for i in gensquares(5):
    print(i, end=' : ')"""
# функция генератор не требует вызова iter()
# т.к сами являются итератором
"""
x = gensquares(5)"""
# <generator object gensquares at 0x1052697d0>
"""
print(next(x))"""  # 0
"""
print(next(x))""" # 1
# генераторы лучше в плане памяти и производительности
# позволяют избежать выполнения сразу все работы, когда результирующие списки большие
# и получение каждого значения требуют длительных вычислений

# генераторы автоматически сохраняют область памяти и значение переменных

# могут появляться во всех итерационных контекстах
"""
def ups(line):
    for ups in line.split(','):
        yield ups.upper()
"""
"""
a = ups('aaa,bbb,ccc')"""
"""
print(next(a))"""  # AAA

"""
t = tuple(ups('aaa, bbb, ccc'))"""  # ('AAA', ' BBB', ' CCC')
"""
d = {i: j for i, j in enumerate(ups('aaa, bbb, ccc'))}"""  # {0: 'AAA', 1: ' BBB', 2: ' CCC'}


# выражение yield
# yield теперь является выражением x = yield i
# который возвращает элемент переданный методом send()
# можно применять для написание генератора который прекращает свою работу
# при отправках кода завершения
# либо менять направление путем передачи новой позиции данных, обрабатываемых внутри генератора
"""
def gen():
    for i in range(10):
        x = yield i
        print(x)"""
# что бы запустить генератор необходимо первый раз вызвать метод next()
"""
print(next(g))"""
# затем передавать аргумент выражению x = yield i через метод send()
"""
print(g.send(55))
print(g.send(22))"""
# если продолжать стандартную итерацию метод next() вернет None
"""
print(next(g)) """  # None

# генераторные выражения
# так же обеспечивают оптимизацию расхода памяти
# выдают результат только по запросу
# генерируя значение на лету, запоминая предыдущую итерацию
# работает так же за счет протокола итерации
# работают медленнее чем списковые включения
"""
g = (x**2 for x in range(4))"""
# <generator object <genexpr> at 0x11018d7d0>
# сам является итератором
"""
print(iter(g) is g)"""  # True

# цикл for запускает протокол итерации так же как и:
# sum, map, sorted, any, all, list, tuple, join
"""
for num in (x**2 for x in range(4)):
    print(num)
"""
# join
"""
s = ''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))"""  # AAABBBCCC

# присваивание с распаковкой
"""
a, b, c = (x for x in 'aa,bb,cc'.split(','))"""
"""
print(a)"""  # aa
"""
print(b)"""  # bb
"""
print(c)"""  # cc

"""
s = sum(x**2 for x in range(4))"""
"""
print(s)"""  # 14

"""
s = sorted((x**2 for x in range(4)), reverse=True)"""
"""
print(s)"""  # [9, 4, 1, 0]

# map и генераторные выражения генерируют элементы по запросу
"""
m = list(map(abs, (-1,-2,-3,-4)))"""  # [1, 2, 3, 4]
"""
g = list(abs(x) for x in (-1,-2,-3,-4))"""  # [1, 2, 3, 4]
# map требует функцию
# генераторное выражение работает и с функцией и с выражением
"""
g = list(x**2 for x in (-1,-2,-3,-4))"""  # [1, 4, 9, 16]

# на примере с join можно увидеть преимущество генераторного выражения над списковым включением

# list comprehension
# в памяти создается бессмысленный список который потом будет стерт
"""
lst_cmh = ''.join([x.upper() for x in 'aa,bb,cc'.split(',')])"""  # AABBCC

# генерация происходит по запросу, при этом в памяти значения в генераторе нигде не сохраняются
"""
gen = ''.join(x.upper() for x in 'aa,bb,cc'.split(','))"""

# генераторы являются одноразовыми итераторами
# объекты которые сами являются итераторами, поддерживают одну активную итерацию


"""
gen = (x*2 for x in 'SPAM')"""
# поддержка одной активной итерации
"""
i1 = iter(gen)
i2 = iter(gen)"""
"""
print(next(i1))"""  # находиться на первой позиции

"""
print(next(i2))"""  # 2 итератор теперь также находиться на первой позиции
"""
print(next(i1))
print(next(i1))"""
"""
print(next(i2))"""  # второй вызов i2 вызвал исключение StopIteration
"""
i3 = iter(gen)"""
"""
print(next(i3))"""  # i3 вызвал исключение StopIteration
# что бы начать заново нужно создать новый генератор
"""
i3 = iter(x*2 for x in 'SPAM')"""  # начнет сначала

# генераторные функции работают таким же образом
# все объекты которые сами по себе являются итератором, и не требуют вызова функции iter()
# поддерживают только одну активную итерацию:
# генераторные выражения, генераторные функции файлы

# объекты которые сами по себе не являются итераторами, требующими вызова функции iter()
# поддерживают множество активных итераторов, так как для каждого создается отдельная ячейка памяти
# это определяется магическим методом __iter__ внутри объекта, если он возвращает сам себя
# то объект будет поддерживать одну активную итерацию, если он возвращает новый объект
# то он будет поддерживать множество итерации
"""
l = [1,2,3,4]

i1 = iter(l)
i2 = iter(l)"""
"""
print(next(i1))"""  # 1
"""
print(next(i1))"""  # 2
"""
print(next(i2))"""  # 1

# расширение yield from
"""
def both(n):
    for i in range(n):
        yield i"""
    # при завершении первого цикла for с оператором yield
    # поток переходит на следующий цикл, а не прекращается как с оператором return
""" for i in (n**2 for n in range(n)):
        yield i
"""
"""
print(list(both(5)))"""  # [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]

# Новый синтаксис
"""
def both(n):
    yield from range(n)
    yield from (x**2 for x in range(n))
"""
"""
print(list(both(5)))"""  # [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]
"""
import os
for root, subs, files in os.walk('.'):"""  # инструмент для прохода по каталогам
""" for name in files:
        print(name)"""

# распаковка генератоных выражений
"""
def f(a,b,c):
    print(f'{a}, {b}, {c}')
"""
"""
f(1,2,3)"""  # 1, 2, 3
"""
f(*range(1,4))"""  # 1, 2, 3
"""
f(*(i for i in range(1,4)))"""  # 1, 2, 3
"""
def f(a,b,c):
    print(f'{a}, {b}, {c}')

d = dict(a='bob', b='dev', c=20)
"""
"""
f(a='bob', b='dev', c=20)"""  # bob, dev, 20

# распаковка словаря ключ=значение
"""
f(**d) """  # bob, dev, 20
# распаковка ключей
"""
f(*d)"""  # a, b, c

"""
l, s = [1, 2, 3], 'spam'"""
"""
for i in range(len(s)):
    s = s[1:] + s[:1]
    print(s, end=' ')

for i in range(len(l)):
    l = l[1:] + l[:1]
    print(l, end=' ')"""

"""
def scramble(seq):
    res = []
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        res.append(seq)
    return res

print(scramble('spam'))"""

# простая функция с return
"""
def scramble(seq):
    return [seq[1:] + seq[:1] for i in range(len(seq))]
"""
"""
print(scramble('spam'))"""  # ['pams', 'pams', 'pams', 'pams']

# функция генератор
"""
def scramble(seq):
    for i in range(len(seq)):
        yield seq[1:] + seq[:1]
"""
# <generator object scramble at 0x1004ed0e0>
"""
print(scramble('spam'))"""  # будет выдавать результаты по запросу не храня список в памяти
"""
for i in scramble((1,2,3)):"""  # for будет генерировать результаты
""" print(i)"""


# генераторное выражение
"""
s = 'spam'"""
# в генераторе нельзя присвоить переменной объект 'spam'
# в генераторах не разрешено использовать операторы
"""
gen = (s[1:] + s[:1] for i in range(len(s)))"""  # <generator object <genexpr> at 0x1072d18c0>

# чтобы пользоваться генератором с произвольным объектом,
# нужно поместить его в функцию с передачей аргумента, например lambda
"""
f = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))"""  #  <generator object <lambda>.<locals>.<genexpr> at 0x109274f40>
"""
print(list(f('spam')))"""  # преобразовать сразу в список

"""
for i in f('spam'):"""  # пройтись в цикле
""" print(i)"""
"""
def permute(seq):
    if not seq:
        return [seq]
    res = []
    for i in range(len(seq)):
        rest = seq[:i] + seq[i+1:]
        for x in permute(rest):
            res.append(seq[i:i+1] + x)
    return res

print(permute('abc'))

def permute_2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute_2(rest):
                yield seq[i:i+1] + x

print(permute_2('abc'))
"""

# zip
"""
l = ['name', 'age', 'city']
l2 = ('lee', 20, 'SPB')

zip_obj = zip(l, l2)"""
# <zip object at 0x107b72b00>
"""
d = dict(zip_obj)"""  # {'name': 'lee', 'age': 20, 'city': 'SPB'}

# map
"""
map_obj = list(map(abs, range(-5,-1)))"""  # [5, 4, 3, 2]

"""
def mymap(func, *args):
    res = []
    for arg in zip(*args):
        res.append(func(*arg))
    return res
"""
"""
def mymap(func, *args):
    return [func(*arg) for arg in zip(*args)]"""
# <function mymap at 0x1098309a0>


# генератор эмуляции map
# <generator object gen_map at 0x1065a58c0>
"""
def gen_map(func, *args):  
    for arg in zip(*args):
        yield func(*arg)
"""

# <generator object gen_map.<locals>.<genexpr> at 0x10aac50e0>
"""
def gen_map(func, *args):
    return (func(*arg) for arg in zip(*args))

print(gen_map(pow, (range(2,5)), range(2,5)))
"""


# zip
"""
def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    # print(seqs)
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res

s = 'abc'
s2 = '123456'"""
"""
print(myzip(s,s2))"""  # [('a', '1'), ('b', '2'), ('c', '3')]
"""
def mymapPad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res
"""
"""
print(mymapPad(s,s2, pad='OK'))"""  # [('a', '1'), ('b', '2'), ('c', '3'), ('OK', '4'), ('OK', '5'), ('OK', '6')]

# генератор zip
"""
def myzip(*seqs):
    seqs = [list(s) for s in seqs]"""
    # если хотя бы один элемент будет пустой цикл закончиться
""" while all(seqs):
        yield tuple(s.pop(0) for s in seqs)

s = 'abc'
s1 = '123456'
print(list(myzip(s,s1)))"""

"""
def mymapPad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]"""
    # если хотя бы один элемент будет не пустой цикл не закончиться
""" while any(seqs):
        yield tuple((s.pop(0)if s else pad)for s in seqs)

print(list(mymapPad(s,s1, pad="Ok")))"""

"""
def myzip(*seqs):
    min_len = min(len(s) for s in seqs)
    index = range(min_len)
    return [tuple(s[i] for s in seqs)for i in index]

s = 'abc'
s1 = '123456'
print(list(myzip(s,s1)))
"""
"""
def mymapPad(*seqs, pad=None):
    max_len = max(len(s) for s in seqs)
    index = range(max_len)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index]

print(list(mymapPad(s,s1)))

"""
"""
def myzip(*seqs):
    min_len = min(len(s) for s in seqs)
    index = range(min_len)
    return (tuple(s[i] for s in seqs) for i in index)

s = 'abc'
s1 = '123456'
print(list(myzip(s,s1)))
"""
"""
def myzipPad(*seqs, pad=None):
    max_len = max(len(s) for s in seqs)
    index = range(max_len)
    return (tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index)

print(list(myzipPad(s,s1)))

"""
"""
def myzip2(*args):
    min_len = min(len(s) for s in args)"""
    # i получает последовательность 0,1,2
    # s[i] проходиться по всем переданным последовательностям
    # и проходя по индексам каждой последовательности, добавляет их в кортеж
    # abc[i] + 123456[i] (a, 1) пока не закончится цикл for
"""return (tuple(s[i] for s in args) for i in range(min_len))"""
"""
s = 'abc'
s1 = '123456'
i1 = myzip2(s,s1)
i2 = myzip2(s,s1)
print(next(i1))
print(next(i2))

print('-'*10)"""
"""
def myzip(*args):"""
    # [<str_ascii_iterator object at 0x10ca0fd60>, <str_ascii_iterator object at 0x10ca0ffd0>]
    # iter создаст объекты итераторов
""" iters = list(map(iter, args))
    while iters:"""
        # для каждого объекта итератора будет вызвана функция next,
        #  которая вернет значение из каждого итератора и сохранит в res
"""     res = [next(i) for i in iters]"""
        # yield преобразует значения из итерируемых объектов в кортеж
        # возвратит его и заморозит функцию сохраняя свои последние значения
"""     yield tuple(res)"""
    # цикл while остановится когда next израсходует значения в списке и вызовет StopIteration
    # у самого короткого итерируемого объекта
"""
s = 'abc'
s1 = '123456'
i1 = myzip(s, s1)
i2 = myzip(s, s1)
print(next(i1))
print(next(i2))
"""

# область видимости генераторных выражений


"""
x = 99"""
# все включения локализуют область видимости, не изменяя внешние переменные
"""
g = [x for x in range(3)]"""

"""
print(g)"""  # [0, 1, 2]
"""
print(x)"""  # 99

# операторы циклов не локализуют имена, изменяя внешние переменные
"""
y = 99
for y in range(3): pass"""
"""
print(y)"""  # 2



"""
x = 'aaa'""" # глобальная область видимости
"""
def func():"""
""" y = '123'"""  # локальная область видимости
""" print(''.join(z for z in y+x))""" # z в области видимости включения
"""
func()
"""
"""
d = {}
for x in range(4):
    d[x] = x**2
"""
"""
print(d)"""  # {0: 0, 1: 1, 2: 4, 3: 9}
"""
print(x)"""  # 3 цикл for не локализует переменные - x доступна в глобальной области видимости
             # ее значение = последнией итерации range(4) то есть 3

"""
d = {x: x**2 for x in range(4)}"""
"""
print(d)"""  # {0: 0, 1: 1, 2: 4, 3: 9}
"""
print(x)"""  # NameError: name 'x' is not defined
             # включения локализуют свои переменные

# включения работают с итерируемыми объектами, но сами не являются генераторами,
# а сразу строят полные объекты
"""
lst = [x**2 for x in range(4)]
d = {x: x**2 for x in range(4)}"""
"""
print(lst)"""  # [0, 1, 4, 9]
"""
print(d)"""  # {0: 0, 1: 1, 2: 4, 3: 9}

# что бы выдавать значения по запросу нужно создавать генератор
"""
g = ((x, x**2) for x in range(4))
print(next(g))"""

# все разновидности включений могут выполнять проход по любым итерируемым объектам которые поддерживают протокол итерации

"""
def adder(*args):"""
    # не зависимо от того какой тип был передан в args
    # за счет того что мы объявили первый элемент началом конкатенации результат
    # операции + будет выполняться в зависимости от типа этого объекта
""" res = [0]
    for arg in args[1:]:
        res += arg
    return res"""
"""
def adder2(**kwargs):
    key = list(kwargs)
    tot = kwargs[key[0]]
    for key in key[1:]:
        tot += kwargs[key]
    return tot
"""
"""
def adder3(**kwargs):
    value = list(kwargs.values())
    tot = value[0]
    for value in value[1:]:
        tot += value
    return tot
"""
"""
print(adder2(a=[1,2,3], b=[4,5],c=[6]))"""  # [1, 2, 3, 4, 5, 6]
"""
print(adder3(a=(1,2,3), b=(4,5), c=(6,)))"""  # (1, 2, 3, 4, 5, 6)
