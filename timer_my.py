# списковые включения быстрее чем циклы
# генераторные функции или выражения могут быть медленнее списковых включений,
# но экономят память, не заставляя ожидать генерацию всех результатов, когда их действительно много

import time
timer = time.perf_counter


def total(func, *args, _reps=1000, **kwargs):
    """
    :param _reps: количество вызовов функций
    :param func: тестируемая функция
    :param args: позиционные аргументы
    :param kwargs: именованные аргументы
    :return: суммарное истекшее время для всех вызовов и последний результат функции
    """
    start = timer()
    for i in range(_reps):
        result = func(*args, **kwargs)
    finish = timer() - start
    return finish, result


def bestof(func, *args, _reps=5, **kwargs):
    """
    :param _reps: количество вызовов функций
    :param func: тестируемая функция
    :param args: позиционные аргументы
    :param kwargs: именованные аргументы
    :return: лучшее время из всех вызовов и последний результат функции
    """
    best_time = 2**32
    for i in range(_reps):
        start = timer()
        result = func(*args, **kwargs)
        finish = timer() - start
        if finish < best_time: best_time = finish
    return best_time, result


def best_of_total(func, *args, _reps1=5, **kwargs):
    """
    :param _reps1: количество вызовов bestof
    :param func: тестируемая функция
    :param args: позиционные аргументы
    :param kwargs: именованные аргументы
    :return: лучшее суммарное время - наименьшее время из resp1 прогонов каждый
    из которых измеряет суммарное время из resp2 вызовов
    """
    return min(total(func, *args, **kwargs) for i in range(_reps1))




# модуль timeit для определения скорости выполнения функций
"""
import timeit"""

# repeat возвращает список суммарного времени которое заняло выполнение теста number раз для каждого из прогонов repeat
# вызов min позволяет получить лучшее время среди прогонов

#
# res = min(timeit.repeat(number=1000, repeat=5, stmt="""
# def permute(seq):
#     if not seq:
#         return [seq]
#     res = []
#     for i in range(len(seq)):
#         rest = seq[:i] + seq[i+1:]
#         for x in permute(rest):
#             res.append(seq[i:i+1] + x)
#     return res
# permute('abc')"""))
# print(res)

# вызов из терминала
# python -m timeit -n 1000 -r 3 "l = [1,2,3,4]" 'i=0' 'while i < len(l):' '    l[i]+=1' '    i+=1'

"""
res = timeit.timeit(stmt='[x**2 for x in range(1000)]', number=1000)
print(res)
"""

# API- интерфейс класса модуля
"""
res = timeit.Timer(stmt='[x**2 for x in range(1000)]').timeit(1000)"""
"""
def f():
    y = [x**2 for x in range(1000)]

res = min(timeit.repeat(stmt=f, number=1000, repeat=4))
"""

