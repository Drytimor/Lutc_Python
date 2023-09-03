import timer_my as t
import timeit
from functools import reduce

"""
reps = 1000
repslist = list(range(reps))

def F(x): return x

"""
# функция с циклом
"""
def forLoop():
    res = []
    for x in repslist:
        res.append(F(x))
    return res
"""
# List comprehension
"""
def listComp():
    return [F(x) for x in repslist]
"""
# функция map
"""
def mapCall():
    return list(map(F, repslist))
"""
# выражение генератор
"""
def genExpr():
    return list(F(x) for x in repslist)
"""
# функция генератор
"""
def genFunc():
    def gen():
        for x in repslist:
            yield F(x)
    return list(gen())"""
"""
for test in forLoop, listComp, mapCall,genExpr, genFunc:
    bestof, result = t.best_of_total(test)
    print(f"{test.__name__}: {bestof:.5f} [{result[0]}...{result[-1]}]")

"""

# числовая функция abs для каждого элемента последовательности из 1000 элементов
# forLoop: 0.05164 [0...999]
# listComp: 0.04956 [0...999]
# mapCall: 0.02375 [0...999]
# genExpr: 0.07049 [0...999]
# genFunc: 0.06912 [0...999]



# операция сложения для каждого элемента последовательности из 1000 элементов
# вызова map с самописной функцией снижает скорость выполнения более чем в 3 раза
# forLoop: 0.05145 [10...1009]
# listComp: 0.04381 [10...1009]
# mapCall: 0.07847 [10...1009]
# genExpr: 0.07171 [10...1009]
# genFunc: 0.07155 [10...1009]



# передача функции для вычесления для каждой последовательноти из 1000 элементов
# если передавать функцию для итерационных инструментов map оказывается быстрее всех,
# forLoop: 0.07917 [0...999]
# listComp: 0.07036 [0...999]
# mapCall: 0.06047 [0...999]
# genExpr: 0.09470 [0...999]
# genFunc: 0.09198 [0...999]




# Из-за того что map может принимать на вход только функцию, а остальные могут работать и с выражениями
# то скорость выполнения, с передачей того же функционала, но посредствам выражения остальные итерационные инструменты
# опережают map в 1.5 - 2 раза так как не требуют дополнительного времени на вызов функции
"""
print(round(min(timeit.repeat(stmt=forLoop, number=1000, repeat=5)), 5))
print(round(min(timeit.repeat(stmt=listComp, number=1000, repeat=5)), 5))
print(round(min(timeit.repeat(stmt=mapCall, number=1000, repeat=5)), 5))
print(round(min(timeit.repeat(stmt=genExpr, number=1000, repeat=5)), 5))
print(round(min(timeit.repeat(stmt=genFunc, number=1000, repeat=5)), 5))"""

# pystone.py — программа, предназначенная для измерения скорости Python в широком диапазоне кода
# (https://github.com/blackberry/Python/ blob/master/Python-З/Lib/test/pystone.py);


"""
def copyDict(dict):
    return {x: y for x,y in dict.items()}

d1 = {'name':'lee', 'age':20}
d2 = copyDict({'name':'lee', 'age':20})"""
"""
print(id(d1), d1)"""  # 4345889664 {'name': 'lee', 'age': 20}
"""
print(id(d2), d2)"""  # 4345521600 {'name': 'lee', 'age': 20}
"""
def dou_dict(dict1, dict2):
    return dict1 | dict2

d1 = {'name':'lee', 'age':20}
d2 = {'city': 'SPB'}
d3 = dou_dict(d1,d2)"""
"""
print(id(d1), d1)"""  # 4355104512 {'name': 'lee', 'age': 20}
"""
print(id(d2), d2)"""  # 4355596480 {'city': 'SPB'}
"""
print(id(d3), d3)"""  # 4355955136 {'name': 'lee', 'age': 20, 'city': 'SPB'}



# рекурсия
"""
def rec_fact(n: int):
    return n if n == 1 else n * rec_fact(n-1)
"""

# цикл
"""
def for_fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
"""
# reduce
"""
def reduce_(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
"""
# стандартная библиотека
"""
import math
def fact_lib(n):
    return math.factorial(n)
"""
# print(round(min(timeit.repeat(stmt=rec_fact, number=1000, repeat=5)), 5))
# print(round(min(timeit.repeat(stmt=for_fact, number=1000, repeat=5)), 5))
"""
for test in for_fact, rec_fact, reduce_, fact_lib:
    bestof, result = t.best_of_total(test, 40)
    print(f'{test.__name__}: {bestof:.5f} {result}')
"""
# for_fact: 0.00285 815915283247897734345611269596115894272000000000
# rec_fact: 0.00395 815915283247897734345611269596115894272000000000
# reduce_: 0.00437 815915283247897734345611269596115894272000000000
# библиотечный модуль работает гораздо быстрее всех остальных инструментов
# fact_lib: 0.00052 815915283247897734345611269596115894272000000000


# вычисление наибольшего объекта в списка
"""
from random import randint
seqs = [randint(1, 10000) for i in range(10000)]

def reduce_(seqs):
    return reduce(lambda x,y: x if x > y else y, seqs)

def max_(seqs):
    return max(seqs)
"""
"""
fastest_result = 2**20
for test in max_, reduce_:
    result_func = round(min(timeit.repeat(stmt=lambda: test(seqs), number=100, repeat=3)), 5)
    fastest_result = result_func if result_func < fastest_result else fastest_result
    print(test.__name__, result_func)"""
    # reduce_ 0.08037
    # max_ 0.01487

"""
print(fastest_result)"""  # max_ 0.01724
