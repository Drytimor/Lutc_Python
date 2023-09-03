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
import sys

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
def sumtree(l):
    tot = 0
    for x in l:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
print(sumtree(l))"""


# очередь с обходом в ширину
# FIFO первым пришел - первым обслужен
"""
def sumtree_FIFO(l):
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

l = [1, [2, [3, 4], 5], 6, [7, 8]]
"""
# print(sumtree_FIFO(l))

# стек с обходом в глубину
# LIFO последний пришел - первым обслужен
"""
def sumtree_LIFO(l):
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot
"""
# print(sumtree_LIFO(l))

# абстракции FIFO и LIFO относятся к работе со списком(данными), только разница не в самом списке(данных),
# а в правилах доступа к нему

# FIFO объект добавляется на одном конце списка(данных), а выполнение операций происходит на другом конце
# это понятие очереди: первым пришел - первым обслужен

# LIFO добавления объекта и выполнения над ним операции происходит на одном конце списка(данных)
# это понятие стека: последний пришел - первым обслужен

