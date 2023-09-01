# функции высшего порядка
# принимают на вхож другие функции или возвращают функции
#  функция map
"""
def sum(x,y):
     return x + y
"""
# map принимает на вход функцию и итерируемый объект
# количество итерируемых объектов должно совпадать
# с количеством обязательных параметров в функции
# она быстрее чем цикл фор
"""
sum_int = list(map(sum, [1,2,3], [1,2,3]))
print(sum_int)"""
# [2, 4, 6]

"""map_obj = map(lambda *args: args, ['name', 'age'], ['lee', 20])"""
# в args будут храниться ('name', 'lee'), ('age', 20)
"""dict_ = dict(map_obj)"""
# {'name': 'lee', 'age': 20}
"""import random
lst1 = [random.randrange(10) for i in range(10)]
map_obj = list(map(pow, sorted(lst1), [2]*len(lst1)))
print(map_obj)"""

# функция zip
"""zip_obj = zip(['name', 'age'], ['lee', 20])"""
# возвращает итератор кортежей ('name', 'lee'), ('age', 20)
"""dict_ = dict(zip_obj)"""
# {'name': 'lee', 'age': 20}
a = 10



