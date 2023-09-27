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



# протокол свойств позваляет направлять операции извлечения,установки, удаления значений конкретного атрибута
# в определяемые нами методами, что дает возможность вставлять логику, которая автоматически выполнится
# при доступе к атрибуту
class Super:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(getName, setName, delName, "name property docs")  # свойство всегда требует в методе передачи self


class Person(Super): pass  # свойства наследуются
"""
bob = Person('Bob smith')
bob.name
bob.name = 'Tom Smith'"""


# декоратор Property
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name
"""
bob = Person('Bob smith')
print(bob.name)
bob.name = 'Tom'
"""


# дескрипторы

class Descriptor:
    """docstring goes here"""
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')
    def __set__(self, instance, value): pass
    # def __delete__(self, instance): pass

class Subject:
    attr = Descriptor()
"""
x = Subject()
x.attr"""


class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')

class C:
    a = D()
"""
x = C()
x.a
C.a
x.a = 99
print(x.a)
print(list(x.__dict__.keys()))
"""

# альтернатива Дескриптор

class Name:
    """name descriptor docs"""
    # self - Экземпляр class Name
    # instance - экземпляр class Human
    # owner - class Human
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Human:
    def __init__(self, name):
        self._name = name

    name = Name()
"""
bob = Human('Bob smith')
print(bob.name)
bob.name = 'Tom'
print(bob.name)
"""


class DescSquare:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    x = DescSquare(2)

class Client2:
    x = DescSquare(4)




class DescState:  # использование состояние дескриптора
    # self для передачи атрибута
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescState get')
        return self.value ** 2

    def __set__(self, instance, value):
        print('DescState set')
        self.value = value

# клиентский класс
class CalcAttrs:
    x = DescState(3)  # атрибут класса дескриптора
    y = 3  # атрибут класса
    def __init__(self):
        self.z = 4  # атрибут экземпляра

obj = CalcAttrs()
"""
print(obj.x, obj.y, obj.z)"""


# obj.x = 5  # вычисляется при извлечении, но его значение будет одинаковым для всех экземпляров класса
           # так же как и атрибут класса Y
# CalcAttrs.y = 6
# obj.z = 7
# print(obj.x, obj.y, obj.z)  # 25 6 7

# obj2 = CalcAttrs()
# print(obj2.x, obj2.y, obj2.z)  # 25 6 4


class InstanceState:  # использование состояние экземпляра
                      # instance
    def __get__(self, instance, owner):
        print('InstanceState get')
        return instance._x
    def __set__(self, instance, value):
        print('InstanceState set')
        instance._x = value


class CalcAttrs2:
    x = InstanceState()  # х будет вычисляться у каждого экземпляра отдельно
    y = 3
    def __init__(self):
        self._x = 2
        self.z = 4  # атрибут экземпляра

"""
obj3 = CalcAttrs2()
print(obj3.x, obj3.y, obj3.z)"""  # 2 3 4
"""
obj3.x = 5  
CalcAttrs2.y = 6
obj.z = 7
print(obj3.x, obj3.y, obj3.z)"""  # 5 6 4
"""
obj4 = CalcAttrs2()
print(obj4.x, obj4.y, obj4.z)"""  # 2 6 4


# может использоваться сразу оба состояние атрибута в self.data и instance.data

class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return f"{self.data}, {instance.data}"
    def __set__(self, instance, value):
        instance.data = value

class Client:
    def __init__(self, data):
        self.data = data

    managed = DescBoth('spam')

"""
i = Client('eggs')
print(i.managed)"""  # spam, eggs
"""
i.managed = 'SPAM'
print(i.managed)"""
"""
print(i.__dict__)"""  # не видны атрибуты дескриптора
"""
print([x for x in dir(i) if not x.startswith('__')])"""  # dir() ['data', 'managed']



class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('cant get attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('cant set attribute')
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('cant delete attribute')
        self.fdel(instance)


class Person4:
    def getName(self): print('get Name ...', 4)
    def setName(self): print('set Name ...')
    name = Property(getName, setName)
"""
x = Person4()
x.name"""


#  __getattr__  __getattribute__
# применяются для перехвата операции любого атрибута экземпляра,
# а не только конкретного имени как свойство или дескрипторы


def __getattr__(self, name): pass  # при извлечении неопределенных атрибутов obj.name
def __getattribute__(self, name): pass  # при извлечении всех атрибутов obj.name
def __setattr__(self, name): pass  # при присваивании всех атрибутов
def __delattr__(self, name): pass # при удалении всех атрибутов

# делегирование

class Wrapper:
    def __init__(self, obj):
        self.obj = obj
    def __getattr__(self, item):
        print(f'Trace: {item}')
        return getattr(self.obj, item)

    def __setattr__(self, key, value):
        print('__setattr__')
        object.__setattr__(self, key, value)
"""
x = Wrapper([1,2,3,4])
x.append(5)
x.obj = 'aqwer'
print(x.obj)"""  # [1, 2, 3, 4, 5]


# извлечение, установка и удаление с помощью
# __getattr__, __setattr__, __delattr__


class Person1:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        print(f'__getattr__: {attr}')
        if attr == 'name':
            return self._name
        raise AttributeError(attr)

    def __setattr__(self, attr, value):
        print(f"__setattr__: {attr}, {value}")
        if attr == 'name':
            attr = '_name'
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        print(f"__delattr__ {attr}")
        if attr == 'name':
            attr = '_name'
        object.__delattr__(self, attr)

"""
bob = Person1('Bob Smith')"""  # __setattr__: _name, Bob Smith
"""
bob.name """  # __getattr__: name

class PropertySquare:
    def __init__(self, start):
        self.value = start

    @property
    def x(self):
        return self.value ** 2
    @x.setter
    def x(self, value2):
        self.value = value2
"""
x = PropertySquare(2)
print(x.x)
x.x = 10
print(x.x)
"""

class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattr__(self, attr):
        if attr == 'x':
            return self.value ** 2
        raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'x':
            attr = 'value'
        return object.__setattr__(self, attr, value)
"""
a = AttrSquare(3)
b = AttrSquare(4)
print(a.x)
a.x = 10
print(a.x)
"""

# динамически вычисляемые атрибуты, реализованные с помощью свойств

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def get_square(self):
        return self._square ** 2

    def set_square(self, value):
        self._square = value

    square = property(get_square, set_square)

    def get_cube(self):
        return self._cube ** 3

    cube = property(get_cube)

"""
x = Powers(3,4)
print('Property')
print(x.get_square()) """  # 3
"""
x.square = 5
print(x.get_square()) """  # 25
"""
print(x.get_cube())"""  # 64
"""
print('-' * 20)"""

# динамически вычисляемые атрибуты, реализованные с помощью дескрипторов

class DescSquare1:
    def __get__(self, instance, owner):
        return instance.square ** 2

    def __set__(self, instance, value):
        instance.square = value

class DescCube(DescSquare1):
     def __get__(self, instance, owner):
         return instance.cube ** 3

class Power1:
    square = DescSquare1()
    cube = DescCube()
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
"""
x = Powers(3,4)
print('Descriptor')
print(x.get_square())"""  # 3
"""
x.square = 5
print(x.get_square())"""  # 25
"""
print(x.get_cube())"""  # 64
"""
print('-' * 20)"""


# свойства


def printer_holder(who):
    print(f'{who.__class__.__name__}:', who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')


def test(class_):
    bob = class_('1234-5678', 'Bob Smith', 40, '123 main st')
    printer_holder(bob)


class CardHolder:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def get_name(self):
        return self.__name

    def set_name(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = Property(get_name, set_name)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 0 > value > 150:
            raise ValueError('INVALID AGE')
        self.__age = value

    age = Property(get_age, set_age)

    def get_acct(self):
        return self.__acct

    def set_acct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acct_len:
            raise TypeError('INVALID ACCT NUMBER')
        value = value[:-3] + '***'
        self.__acct = value

    acct = Property(get_acct, set_acct)

    def remain_get(self):
        return self.retire_age - self.age
    # remain виртуальный атрибут, вычисляется по запросу
    remain = Property(remain_get)


# test(CardHolder)


# дескрипторы
# разделяемое состояние атрибуты создаются в дескрипторе по средствам self
# это значит что изменение атрибута в одном экземпляре изменит его и в другом
class CardHolder2:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if 0 > value > 150:
                raise ValueError('INVALID AGE')
            self.age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acct_len:
                raise TypeError('INVALID ACCT NUMBER')
            value = value[:-3] + '***'
            self.acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retire_age - instance.age

        def __set__(self, instance, value):
            raise TypeError('cannot set remain')
    remain = Remain()


# test(CardHolder2)

tom = CardHolder2('12345678', 'Tom', 12, 'asd')
"""
print(tom.__dict__)""" # {'addr': 'asd'} вычисляемые атрибуты принадлежат объекту дескриптора из-за self в дескрипторе
# это значит что изменение атрибута в одном экземпляре изменит его в другом
rob = CardHolder2('12345678', 'Tom', 30, 'asd')

# дескриптор с хранением атрибутов для каждого клиентского класса
# у каждого клиентского класса будет свое состояние атрибутов
class CardHolder3:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return instance.__name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance.__name = value
    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return instance.__age

        def __set__(self, instance, value):
            if 0 > value > 150:
                raise ValueError('INVALID AGE')
            instance.__age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return instance.__acct

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acct_len:
                raise TypeError('INVALID ACCT NUMBER')
            value = value[:-3] + '***'
            instance.__acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retire_age - instance.age

        def __set__(self, instance, value):
            raise TypeError('cannot set remain')
    remain = Remain()


# test(CardHolder3)

tom = CardHolder3('12345678', 'Tom', 12, 'asd')
rob = CardHolder3('12345678', 'Tom', 30, 'asd')

# версия с __getattr__


class CardHolder4:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, name):
        if name == 'acct':
            return self._acct[:-3] + '***'
        elif name == 'remain':
            return self.retire_age - self.age
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'age':
            if 0 > value > 150:
                raise ValueError('INVALID AGE')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acct_len:
                raise TypeError('INVALID ACCT NUMBER')
        elif name == 'remain':
            raise TypeError('cannot set remain')

        # obj.__setattr__(name, value)
        self.__dict__[name] = value


# test(CardHolder4)
