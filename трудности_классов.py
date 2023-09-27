import sys


class X:
    a = 1


i = X()
# print(i.a)
X.a = 2
# print(i.a)
j = X()
# print(j.a)


class C:
    shared = []
    def __init__(self):
        self.perobj = []


x = C()
y = C()
x.shared.append('spam')
x.perobj.append('spam')
x.shared ='spam'
# print(x.shared, x.perobj)
# print(y.shared, y.perobj)

def generate(lablbe):
    class Spam:
        count = 1
        def method(self):
            print(f"{lablbe}={Spam.count}")
    return Spam

aclass = generate('hello')
i = aclass()  # __main__.generate.<locals>.Spam object at 0x105347210>
# print(i)
# i.method()


class Adder:
    def add(self, other):
        print('Not implemented')


class ListAdder(Adder):
    def __init__(self, *args):
        self.data = [x for x in args]

    def add(self, other, reverse=None):
        if reverse:
            return other + self.data
        return self.data + other

    def __add__(self, other):
        return self.add(other, reverse=False)

    def __radd__(self, other):
        return self.add(other, reverse=True)


l = ListAdder('5,4,2')
x = l + ['a','s']
y = [5,2] + l
"""
print(x)"""  # ['5,4,2', 'a', 's']
"""
print(y)"""  # [5, 2, '5,4,2']


class DictAdder(Adder):
    def __init__(self, **kwargs):
        self.data = {key: value for key, value in kwargs.items()}

    def add(self, other):
        return self.data | other

    def __add__(self, other):
        return self.add(other)



x = DictAdder(name='tom', age=30)
"""
print(x.data)"""  # {'name': 'tom', 'age': 30}
"""
z = x + {'job':'dev'}"""
"""
print(id(x.data), x.data)"""  # 4555993088 {'name': 'tom', 'age': 30}
"""
print(id(z), z)"""  # 4555992832 {'name': 'tom', 'age': 30, 'job': 'dev'}


class MyList:
    def __init__(self, data):
        self.data = list(data)
    def __getitem__(self, index):
        return MyList(self.data[index])
    def __mul__(self, other):
        return MyList(self.data * other)
    def __len__(self):
        return len(self.data)
    def __add__(self, other):
        return MyList(self.data + other)
    def __repr__(self):
        return repr(self.data)
    def __getattr__(self, attr):
        return getattr(self.data, attr)
    def append(self, other):
        print('append')
        self.data.append(other)


class MyListSub(MyList):
    calls = 0
    def __init__(self,data):
        self.adds = 0
        MyList.__init__(self, data)

    def __add__(self, other):
        import sys
        MyListSub.calls += 1
        self.adds += 1
        sys.stdout.write(f'Check class {MyListSub.calls}\n'
                         f'Check adds {self.adds}\n')



# l = MyListSub([1,2,3])
#
# x = l + [4]
# x = l + [4]



class Attrs:

    def __getattr__(self, item):
        return getattr(self, str('item'))

    def __setattr__(self, key, value):
        self.__dict__[str(key)] = value

    def stdout(self):
        import sys
        sys.stdout.write(str([f"{attr}={getattr(self, attr)}" for attr in self.__dict__]))

#
#
# a = Attrs()
# a.name = 'tom'
# a.stdout()


class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food):
        """вызывает метод place_order"""
        self.customer.place_order(food, self.employee)

    def result(self):
        return self.customer.print_order()


class Customer:

    def __init__(self):
        self.food = None

    def place_order(self, food, employee):
        """вызывает метод take_order"""
        self.food = employee.take_order(food)

    def print_order(self):
        return self.food.food


class Employee:
    @staticmethod
    def take_order(food_name):
        return Food(food_name)


class Food:
    def __init__(self, food):
        self.food = food


l = Lunch()
w = Lunch()
w.order('loop')
l.order('apple')


class Animal:

    def speak(self):
        pass

    def reply(self):
        self.speak()


class Mammal(Animal):
    def speak(self):
        print('ay')


class Cat(Mammal):
    def speak(self):
        print('meow')


class Dog(Mammal):
    def speak(self):
        print('gav')


class Primate(Mammal):
    def speak(self):
        print('hey')


class Hacker(Primate):
    pass





class Scene:
    def __init__(self):
        self.customer = Customer_()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        for line in self.customer, self.clerk, self.parrot:
            line.line()


class Customer_:
    def line(self):
        print('that one ex-bird')



class Clerk:
    def line(self):
        print('no it is')


class Parrot:
    def line(self):
        print(None)


Scene().action()