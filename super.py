# вызов суперкласса через явное присваивание
class C:
    def act(self):
        print('spam')

class D(C):
    def act(self):
        C.act(self)
        print('eggs')

"""
x = D()
x.act()"""


class E(C):
    def method(self):
        print(self.__class__.__bases__)
        proxy = super()
        print(proxy)
        proxy.act()

# E().method()

class A:
    def act(self): print('A')
class B:
    def act(self): print('B')

class C(A,B):
    def act(self):
        super().act()

x = C()
x.act()
