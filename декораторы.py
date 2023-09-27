"""
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        return self.func(*args)
"""

"""
@Tracer"""  # spam = Tracer(spam)
"""
def spam(a,b,c):"""  # функция spam попадает в класс Tracer в его метод __call__
""" return a+b+c"""
"""
print(spam(1,2,3))"""
"""
print(spam)"""  # <__main__.Tracer object at 0x101b92890>


"""
def tracer_(func):
    def oncall(*args):
        oncall.calls += 1
        print(f"call {oncall.calls} to {func.__name__}")
        return func(*args)
    oncall.calls = 0
    return oncall


class C:
    @tracer_
    def spam(self, a,b,c): return a+b+c"""
"""
x = C()
print(x.spam(1,2,3))
print(x.spam('a','d','a'))
y = C()
print(y.spam(6,2,6))"""


"""
def count(aClass):
    aClass.numInstance = 0
    return aClass

@count
class Spam: pass

@count
class Sub(Spam): pass

@count
class Other(Spam): pass

@count
def spam():pass

a = Spam()"""
"""
print(Spam.__dict__) """ # 'numInstance': 0
"""
print(Spam.numInstance)"""  # 0
"""
print(spam.numInstance)"""  # 0


def decorator(cls):  # сохраняет исходный класс в объемлющей области видимости
    class Wrapper:
        def __init__(self, *args):
            self.wrapper = cls(*args)
        def __getattr__(self, name):
            print('decorator __getattr__')
            return getattr(self.wrapper, name)
    return Wrapper

@decorator
class C:
    def __init__(self, x,y):
        self.attr = 'spam'
"""

x = C(6,7)
print(x.attr)"""

# вложенные декораторы

def d1(f): return lambda: 'X' + f()
def d2(f): return lambda: 'Y' + f()
def d3(f): return lambda: 'Z' + f()

@d3
@d2
@d1
def func():
    return 'spam'

# print(func())

# декораторы функций

class Tracer:
    def __init__(self, func):
        self.call = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.call += 1
        print(f"call {self.call} to {self.func.__name__}")
        self.func(*args, **kwargs)

# функция спам становиться аргументом класса Tracer
# вызов этого аргумента с параметрами отлавливается методом __call__
# затем в методе __call__ выполняется логика
"""
@Tracer
def spam(a,b,c): """ # spam = Tracer(spam)
""" print(a+b+c)"""

"""@Tracer
def func(x,y):
    print(x+y)"""
"""
spam(a=3, b=4, c=2)"""
"""
print(spam)"""  # <__main__.Tracer object at 0x1048b9690>
"""
spam(1, 2, 3)"""  # вызывается метод __call__ у Tracer
"""
func(1, 2)"""   # у каждого объекта свое пространство имен

# объемлющие области видимости и глобальные переменные

calls = 0
def tracer(func):  # функкия будет разделать общий счетчик
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print(f"call {calls} to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a,b,c):
    print(a+b+c)

@tracer
def egs(x):
    print(x**2)
"""
spam(1,2,3)
egs(2)"""

# объемлющие области видимости и локальные переменные


def tracer(func):  # каждая функция будет иметь собственную область видимости со счетчиком
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"call {calls} to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper



import time
class Timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print(f"{self.func.__name__}: {elapsed:.5f}, {self.alltime:.5f}")
        return result


@Timer
def listcomp(n):
    return [x*2 for x in range(n)]


@Timer
def mapcall(n):
    return list(map(lambda x: x*2, range(n)))

"""
listcomp(50000)
listcomp(500000)
listcomp(5000000)
print(f"alltime: {listcomp.alltime}")


mapcall(50000)
mapcall(500000)
mapcall(5000000)
print(f"alltime: {mapcall.alltime}")
"""


# добавление аргументов декоратору

def timer(label='', trace=True):  # сохраняет аргументы декоратора в объемлющей области видимости функции
    # для каждого экземпляра
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.perf_counter()
            result = self.func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                print(f"{label}, {self.func.__name__}:, {elapsed:.5f}, {self.alltime:.5f}")
            return result
    return Timer


@timer(label='[CCC]==>')
def listcomp(n):
    return [x*2 for x in range(n)]


@timer(label='[MMM]==>')
def mapcall(n):
    return list(map(lambda x: x*2, range(n)))

"""
for func in listcomp, mapcall:
    func(50000)
    func(500000)
    func(5000000)
    print(f'alltime:{round(func.alltime,5)}')"""


# паттерн одиночка
  # будет сохраняться только один экземпляр класса
instances = {}

def singleton(aClass):
    def on_call(*args, **kwargs):
        if aClass not in instances:  # проверка, что в словаре еще нет данного класса
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return on_call

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, value):
        self.attr = value

bob = Person('Bob', 40, 10)
tom = Person('Tom', 50 , 20)
x = Spam(12)
# создается только один экземпляр
"""
print(tom.name, tom.hours, tom.rate)"""  # Bob 40 10
"""
print(Person)
print(instances)"""

# объемлющая область видимости
# instances установит только один экземпляр каждого класса
def singleton(aClass):
    instances = None
    def on_local(*args, **kwargs):
        nonlocal instances
        if instances is None:
            instances = aClass(*args, **kwargs)
        return instances
    return on_local


@singleton
class Spam:
    def __init__(self, value):
        self.attr = value

x = Spam(12)
y = Spam(13)
"""
print(y.attr)"""  # 12


# отслеживание интерфейсов с помощью декораторов класса

def tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapper = aClass(*args, **kwargs)

        def __getattr__(self, attr_name):
            self.fetches += 1
            print(f"Trace: {attr_name}")
            return getattr(self.wrapper, attr_name)
    return Wrapper


@tracer
class Spam:
    def display(self):
        print('Spam!' * 8)

@tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

"""
food = Spam()"""  # объект Wrapper
"""food.display()"""  #  вызывает метод __getattr__, который делегирует вызов метода классу Spam

"""
bob = Person('Bob', 40, 50)"""  # объект Wrapper
"""
print(bob.name)"""
"""
print(bob.pay())"""
"""
print(bob.rate)"""
# каждый имеет собственный счетчик делегирования атрибутов
"""
print(food.fetches, bob.fetches)"""


# регистрация декорированных объектов

registry = {}

def register(obj):
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return x*2
@register
def ham(x):
    return x * 3
@register
class Eggs:
    def __init__(self,x):
        self.data = x*4

    def __str__(self):
        return str(self.data)

"""
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))"""

# spam => <function spam at 0x10099e0c0> <class 'function'>
# ham => <function ham at 0x10099dd00> <class 'function'>
# Eggs => <class '__main__.Eggs'> <class 'type'>

# дополнение декорированных объектов напрямую


def decorate(func):
    func.marked = True
    return func

@decorate
def spam(a,b):
    return a+b
"""
print(spam.__dict__) """  # {'marked': True}


# аргумент декоратора является атрибутов декорируемой функции

def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate


@annotate(text='spam data')
def spam(a,b):
    return a + b
"""
print(spam.__dict__) """  # {'label': 'spam data'}


# реализация закрытых атрибутов
trace_me = False
def trace(*args):
    if trace_me: print('['+ ''.join(map(str, args))+']')
def private(*privates):
    def on_decorator(aClass):
        class OnInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:  # проверка атрибута в privates
                    raise TypeError(f'private attribute fetch: {attr}')  # запрет доступа (исключение)
                return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set: ', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError(f'private attribute fetch: {attr}')
                else:
                    self.__dict__[attr] = value
        return OnInstance
    return on_decorator


trace_me = True
@private('data', 'size')
class Doubler:
    def __init__(self, label, data):
        self.label = label
        self.data = data
    def size(self):
        return len(self.data)
    def double(self):
        for i in range(self.size()):
            self.data[i] = self.data[i] * 2
    def display(self):
        print(f"{self.label} => {self.data}")
"""
x = Doubler('X is', [1,2,3])"""  # объект OnInstance
"""
print(x)"""  # <__main__.private.<locals>.on_decorator.<locals>.OnInstance object at 0x103f9f950>
"""
x.double()"""  # [get:double]  делегирование метода классу клиента
"""
x.display()"""  # [get:display]


# декораторы с объявлением атрибутов Private и Public

trace_me = False
def trace(*args):
    if trace_me: print('['+ ' '.join(map(str, args)) + ']')

def access_control(fail_if):
    def on_decorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace(f'get: {attr}')
                if fail_if(attr):
                    raise TypeError(f'private attribute fetch: {attr}')
                return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif fail_if(attr):
                    raise TypeError(f'private attribute fetch: {attr}')
                else:
                    setattr(self.__wrapped, attr, value)


        return onInstance
    return on_decorator


def Private(*attributes):
    return access_control(fail_if=lambda attr: attr in attributes)

def Public(*attributes):
    return access_control(fail_if=lambda attr: attr not in attributes)


@Public('name')  # Person = Private('age')(Person)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.age)

trace_me = True

bob = Person('Bob', 20)  # объект OnInstance
print(bob.name)  # [get: name]
bob.name = 'Tom'  # [set: name Tom]

