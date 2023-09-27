class Methods:
    def imeth(self, x):
        print([self, x])
    @staticmethod
    def smeth(x):
        print([x])
    @classmethod
    def cmeth(cls, x):
        print([cls, x])
    @property
    def name(self):
        return f"Bob {self.__class__.__name__}"

# obj = Methods()
#
# print(obj.name)
# obj.cmeth(1)
# obj.smeth(2)

"""
obj.imeth(1)"""  # [<__main__.Methods object at 0x1014ce710>, 1]
"""
Methods.imeth(obj, 2)"""  # [<__main__.Methods object at 0x1091ba850>, 2]
"""
Methods.smeth(3)"""  # 3
"""
obj.smeth(3)"""  # 3
"""
Methods.cmeth(5)"""  # [<class '__main__.Methods'>, 5]
"""
obj.cmeth(6)"""  # [<class '__main__.Methods'>, 6]

class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    def printNumInstance():
        print(f"Number of instance {Spam.numInstance}")

    printNumInstance = staticmethod(printNumInstance)
"""
x = Spam()
y = Spam()
Spam.printNumInstance()
"""

class Sub(Spam):
    def printNumInstance():
        print('Extra staff...')
        Spam.printNumInstance()

    printNumInstance = staticmethod(printNumInstance)

class Other(Spam): pass

"""
v = Sub()
v.printNumInstance()
Sub.printNumInstance()
Spam.printNumInstance()
"""
"""
class Other(Spam): pass"""  # создание класса также увеличивает счетчик
"""
c = Other()
c.printNumInstance()"""


