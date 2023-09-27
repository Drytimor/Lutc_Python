class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    @classmethod
    def printNumInstance(cls):
        print(f"Number of instance {cls.numInstance, cls}")


class Sub(Spam):
    @classmethod
    def printNumInstance(cls):
        print('Extra staff...', cls)
        Spam.printNumInstance()


class Other(Spam): pass
"""
a, b = Spam(), Spam()
a.printNumInstance()"""

a = Sub()
y = Spam()
# a.printNumInstance()
# Sub.printNumInstance()
z = Other()
# a.printNumInstance()
# y.printNumInstance()
# z.printNumInstance()


class Spam_:
    numInstance = 0
    @classmethod
    def count(cls):
        cls.numInstance += 1
    def __init__(self):
        self.count()


class Sub_(Spam_):
    numInstance = 0
    def __init__(self):
        Spam_.__init__(self)

class Other_(Spam_):
    numInstance = 0

x = Spam_()
y1, y2 = Sub_(), Sub_()
z1, z2, z3 = Other_(), Other_(), Other_()
"""
print(x.numInstance) 
print(y1.numInstance)
print(z1.numInstance)"""


