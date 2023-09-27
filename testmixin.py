import importlib


def tester(listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'
        def ham(self): pass

    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 44

        def spam(self): pass

    instance = Sub()
    print(instance)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)  # импортируем модуль

    listerclass = getattr(modobject, classname)  # достаем класс из модуля по имени <class 'listisinstance.ListInstance'>

    tester(listerclass, sept)  # передаем класс в функцию

if __name__ == '__main__':
    testByNames('listisinstance', 'ListInstance', True)
