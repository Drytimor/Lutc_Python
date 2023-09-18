"""
class Number:
    def __init__(self, start):
        self.start = start

    def __sub__(self, other):
        return Number(self.start - other)
"""

# индексация и срезы
# __getitem__, __setitem__

class Indexer:
    def __getitem__(self, index):
        return index ** 2

x = Indexer()
"""
print(x[2])"""  # для x[2]  вызывается x.__getitem__(2)

class Indexer2:
    data = [1,2,3,4,5,6]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

x = Indexer2()  # __getitem__ передает срез в объект среза slice
"""
print(x[1:3])"""  # getitem: slice(1, 3, None)
               # [2, 3]

class Indexer3:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

x = Indexer3()
# x[99] indexing 99
# x[1:2:3] slicing 1 2 3
# x[1:] slicing 1 None None

class IndexSetter:
    data = [1,2,3,4,5]
    def __setitem__(self, index, value):
        self.data[index] = value


x = IndexSetter()
"""
x[0] = 10
print(x.data) """ # [10, 2, 3, 4, 5]



class StepperIndex:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]


x = StepperIndex('spam')
# цикл фор может работать вызывая __getitem__
"""
for item in x:
    print(item, end=' ') """ # s p a m


# все итерационные инструменты будут работать с __getitem__
"""
print('p' in x)"""  # True
"""
print([x for x in x])"""  # ['s', 'p', 'a', 'm']
"""
print(list(map(str.upper, x)))"""  # ['S', 'P', 'A', 'M']
"""
a,b,*c = x
print(a, b, c)"""  # s p ['a', 'm']
"""
print(list(x), tuple(x), ':'.join(x))"""  # ['s', 'p', 'a', 'm'] ('s', 'p', 'a', 'm') s:p:a:m

# одноразовый итератор
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

"""
x = Squares(1,5)
y = iter(x)"""  # iter  вызывает __iter__
"""
print(next(y))"""  # 1 next вызывает __next__
"""
c = iter(x)
print(next(c))"""  # 2 продолжает итерацию (одноразовая итерация), потому что __iter__ возвращает сам себя

# множественная итерация

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        item = self.wrapped[self.offset]
        self.offset += 2
        return item


s = SkipObject('spam')
i = iter(s)
i2 = iter(s)  # создается новый объект итератора
"""
print(next(i))"""  # s
"""
print(next(i2))"""  # s

# iter + yield
# при использовании оператора yield при вызове iter() каждый раз будет создан новый объект генератора (множественная итерация)
# со своей области видимости для сохранения своего состояния
# это не требует создания дополнительного класса для реализации такого поведения
class Square:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    #     нет необходимости создавать __next__ он подразумевается в операторе yield
    def __iter__(self):
        for value in range(self.start, self.stop+1):
            yield value ** 2

# создается множественная итерация
"""
s = Square(1,4)
i = iter(s)"""  # <generator object Square.__iter__ at 0x10aabdee0>
"""
print(next(i))
i2 = iter(s)
print(next(i2))"""



class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        offset = 0
        if offset >= len(self.wrapped):
            raise StopIteration
        item = self.wrapped[offset]
        offset += 1
        yield item

s = SkipObject('spam')
i = iter(s)  # <generator object SkipObject.__iter__ at 0x105ff6180>
i2 = iter(s)  # <generator object SkipObject.__iter__ at 0x105ff5e00>
"""
print(next(i))"""  # s
"""
print(next(i2))"""  # s


# __getattr__, __setattr__

class Empty:
    def __getattr__(self, attr):
        if attr == 'age':
            return 40
        raise AttributeError(attr)

x = Empty()
"""
print(x.__dict__)"""  # {}
"""
print(x.age)"""  # 40
"""
print(x.name)"""  # AttributeError: name



class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + 'not allowed')

y = Accesscontrol()
y.age = 30
"""
print(y.__dict__)"""  # {'age': 40}




class Commuter1:
    def __init__(self, value=0):
        self.data = value
    #  не поддерживает использование объектов экземпляров с правой стороны операции +
    def __add__(self, other):
        return self.data + other
    #  позволяет выполнять операцию + с объектом экземпляра с правой стороны
    def __radd__(self, other):
        return other + self.data

x = Commuter1(5)
"""
print(x + 2)"""  # 7
"""
print(2 + x)"""  # TypeError: unsupported operand type(s) for +: 'int' and 'Adder'


class Commuter2:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        return self.data + other
    # можно явно вызвать .__add__(other)
    def __radd__(self, other):
        return self.__add__(other)


class Commuter3:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        return self.data + other

    __radd__ = __add__  # использовать псевдоним

# при сложениях результаты будут классом int
"""
x = Commuter3(5)
c = Commuter3(4)
a = x+c
print(a.__class__)"""  # <class 'int'>
"""
y = x + 2
print(x.__class__)"""  # <class '__main__.Commuter3'>
"""
print(y.__class__)"""  #v <class 'int'>
"""
print(x + 2)"""  # 7
"""
print(2 + x)"""  # 7


class Commuter4:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter4):
            other = other.val
        return Commuter4(self.val + other)

    def __radd__(self, other):
        return Commuter4(other + self.val)

    def __str__(self):
        return f'Commuter4: {self.val}'
"""

x = Commuter4(5)
y = Commuter4(3)
c = x+y
print(c, c.__class__)"""  # <class '__main__.Commuter4'>
"""
a = x + 1
print(a, a.__class__)"""  # <class '__main__.Commuter4'>


# __iadd__  - сложение на месте выполняется быстрее чем __add__

class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self

x = Number([1,2,3])
x += [4]  # [1, 2, 3, 4]

# __call__ вызывается при вызове экземпляра класса
# все что передается экземпляру - передается в __call__

class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)

"""
c = Callee()
c(1,2,3, y=4) """ # Called: (1, 2, 3) {'y': 4}


class Prod:
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.value * other

"""
x = Prod(2)
print(x.__dict__)"""  # {'value': 2}
"""
print(x(2))"""  # 4   2 попала в __call__ как other

"""
class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)
        
# обработчики

cb1 = Callback('blue')
cb2 = Callback('green')
b1 = Button(command=cb1)
b2 = Button(command=cb2)
"""

# аналог с замыканием
def callback(color):
    # color('green') находится в этой области видимости
    def oncall():
        # у oncall есть доступ к объемлющей функции callback к переменной color
        print('turn', color)
    return oncall

"""
cb3 = callback('green')
cb3()"""  # turn green


# lambda замыкание
cb4 = lambda color='red': 'turn ' + color
"""
print(cb4())"""  # turn red

class Life:
    def __init__(self, name):
        print(f'hello {name}')
        self.name = name
    def live(self):
        print(self.name)
    def __del__(self):
        print(f'Goodbye {self.name}')


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return f'Employee {self.name}, {self.salary}'


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, 'interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'makes pizza')


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


"""
scene = PizzaShop()
scene.order('Homer')
print('...')"""

#
# Homer orders from Employee Pat, 40000
# Bob makes pizza
# oven bakes
# Homer pays for item to Employee Pat, 40000

"""
bob = PizzaRobot('Bob')"""
"""
print(bob)
bob.work()
bob.give_raise(0.20)
print(bob)"""
"""
for cls in Employee, Chef, Server, PizzaRobot:
    obj = cls(cls.__name__)
    obj.work()"""


# делегирование

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attr):
        print('trace:' + attr)
        # getattr ищет переданный атрибут у экземпляра класса (как типа данных)
        # т.е у list он найдет метод append, который отловил __getattr__
        # list.__dict__['append']
        return getattr(self.wrapped, attr)
"""
x = Wrapper([1,2,3])
x.append(4)"""  # trace:append
"""
print(x.wrapped)"""  # [1, 2, 3, 4]
"""
y = Wrapper({'a': 1, 'b': 2})"""  # trace:keys
"""
print(list(y.keys()))"""  # ['a', 'b']
"""
print('append' in list.__dict__)"""  # True