# Наследование

# механизм ООП в python это по сути две операции:
# - получение объекта на котором произведен вызов по средствам self
# - поиск атрибута в иерархии наследования
#
# Поиск выполняется снизу вверх, слева на право
#
# нижестоящие классы наследуют атрибуты вышестоящих классов
#
# python извлечет первый попавшийся атрибут
# нижестоящие классы могут переопределять атрибуты

# Полиморфизм

# полиморфизм выражается при помощи перезаписи атрибута в классе унаследовавшего в его суперклассе, т.е
# один метод будет выполнять разные операции в зависимости от объекта с которым он работает
"""
class Employee:"""  # superclass
"""    
    def computeSalary(self):
        pass
    def giveRaise(self):
        pass
    def promote(self):
        pass
"""
"""
class Engineer(Employee):"""
"""
    def computeSalary(self):"""  # переопределение метода
"""    pass"""


#     класс из которого будет создан экземпляр определяет уровень откуда будет начинаться поиск атрибутов
# и какие версии методов он будет задействовать
"""
bob = Employee()

tim = Engineer()
"""


# Объект класса
# обеспечивает стандартное поведение и служит фабрикой для объектов экземпляра
# происходят из операторов class



# Объект экземпляра
# представляет собой самостоятельно пространство имен, но наследует имена от класса от которого был создан
# происходят из вызова класса



# у класса свое пространство имен
# у атрибутов свое пространство имен
"""
class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

"""
# каждый атрибут имеет свое пространство имен
# можно изменять или добавлять атрибуты в эти пространства через класс по средствам self
# или за пределами класса напрямую у экземпляра
"""
x = FirstClass()
y = FirstClass()
"""
"""
print([atr for atr in dir(x) if atr[-1:-3:-1] != '__'])"""  # ['display', 'setdata']
"""
x.setdata(1998)"""
"""
print([atr for atr in dir(x) if atr[-1:-3:-1] != '__'])"""  # ['data', 'display', 'setdata']
"""
x.__delattr__('data')
print([atr for atr in dir(x) if atr[-1:-3:-1] != '__'])"""  # ['display', 'setdata']
"""
x.data = 1998
print([atr for atr in dir(x) if atr[-1:-3:-1] != '__'])"""  # ['data', 'display', 'setdata']

# Специализация - переопределение унаследованных имен
# за счет повторного определения в расширениях ниже в дереве классов
"""
class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):

    def display(self):
        print(f"Current value = {self.data}")
"""

"""
a = SecondClass()"""  # создается экземпляр класса
"""
a.setdata(42)"""  # метод setdata находится в суперклассе FirstClass
"""
a.display()"""  # а метод display теперь находиться в SecondClass который наследовался от FirstClass и переопределил его у себя

# Специализация введенная в SecondClass касается только этого класса, она не будет затрагивать существующие или будущие
# объекты FirstClass, то есть вместо изменения супер класса, мы можем создать дочерний класс, и настроить его
# как необходимо

# классы являются атрибутами в модулях
# модуль отражает целый файл, а класс является оператором внутри модуля

"""
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
"""
"""
    def __add__(self, other):"""  # создает новый экземпляр ThirdClass
"""    return ThirdClass(self.data + other)"""
"""
    def __str__(self):
        return f"ThirdClass: {self.data}"

    def __mul__(self, other):"""
"""     self.data *= other"""  # изменяет объект на месте
"""
a = ThirdClass('abc')
"""
"""
print(a, id(a))"""  # ThirdClass: abc 4455849104
"""
b = a + 'cde'"""
"""
print(b, id(b))"""  # ThirdClass: abccde 4455847952

# можно присваивать атрибуты напрямую
"""
class res: pass

res.name = 'Bob'
res.age = 30"""

"""
print([atr for atr in dir(res) if atr[-1:-3:-1] != '__'])"""  # ['age', 'name'] атрибуты класса

"""
x = res()"""
"""
y = res()"""  # новые пространства имен, они не имеет атрибутов 'age', 'name', но их имеет класс
# поэтому поиск по иерархии классов найдет и выведет их у класса, у x и y они будут одинаковые
"""
print(x.name, y.name) """  # Bob Bob
"""
print([atr for atr in dir(x) if atr[-1:-3:-1] != '__'])"""

# изменение атрибута у одного экземпляра не повлияет на другой экземпляр т.к,
# изменения были введены только в пространстве имен этого экземпляра
"""
x.name = 'Tim'"""
"""
print(x.name, y.name)"""  # Tim Bob

"""
print(x.__dict__)"""  # {'name': 'Tim'}
"""
print(y.__dict__)"""  # {}
"""
print({key: value for key, value in res.__dict__.items() if not key.startswith('__')})"""  # {'name': 'Bob', 'age': 30}

# запись на основе словаря
"""
rec = {}

rec['name'] = 'Bob'
rec['age'] = 30
rec['jobs'] = ['dev', 'mgr']
"""
"""
print(rec)"""  # {'name': 'Bob', 'age': 30, 'jobs': ['dev', 'mgr']}


# запись на основе class
"""
class rec: pass

pers1 = rec()
pers1.name = 'bob'
pers1.age = 20
pers1.jobs = ['dev', 'mgr']

pers2 = rec()
pers2.name = 'tim'
pers2.age = 30
pers2.jobs = ['sto', 'mgr']
"""
"""
print(pers2.__dict__)"""  # {'name': 'tim', 'age': 30, 'jobs': ['sto', 'mgr']}
"""
print(pers1.__dict__)"""  # {'name': 'bob', 'age': 20, 'jobs': ['dev', 'mgr']}

# запись + логика
"""
class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age        
    def info(self):
        return self.name , self.jobs
"""

"""
class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined'

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('i Replacer.method')

class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')
"""
"""
for _class in (Inheritor, Replacer, Extender,Provider):
    print(f'\n{_class.__name__} ...')
    _class().method()
"""
"""
x = Provider()
x.delegate()"""
"""
x = Extender()
x.delegate()"""
"""
from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
"""
""" @abstractmethod"""
""" def action(self):"""  # абстрактные методы в супер классах создаются для того чтобы все дочерние классы
"""     pass """          # обязательно реализовывали указанные абстрактные методы
"""
class Sub(Super):"""  # приведет к ошибке т.к не был создан абстрактный метод action
""" pass"""
"""
x = Sub()"""  # TypeError: Can't instantiate abstract class Sub with abstract method action




