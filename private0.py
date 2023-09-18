class PrivateExc(Exception): pass


class Privacy:

    def __setattr__(self, attr, value):
        if attr in self.privates:
            raise PrivateExc(attr,self)
        self.__dict__[attr] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


x = Test1()
y = Test2()
x.name = 'Bob'
"""
y.name = 'Bil'"""  # PrivateExc: ('name', <__main__.Test2 object at 0x102dfde10>)
"""
x.age = 30"""  # PrivateExc: ('age', <__main__.Test1 object at 0x10cf55ed0>)






