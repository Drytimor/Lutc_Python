class Operations:
    def __getattr__(self, name):  # перехватывает только неопределенные атрибуты экземпляра
        if name == 'age':
            return f"getattr: {40}"
        raise AttributeError(name)

    def __setattr__(self, name, value):
        print(f"setattr: {name} {value}")
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value


class Properties:
    def getage(self):
        return f"getage: {40}"

    def setage(self, value):
        print(f"set age: {value}")
        self._age = value

    age = property(getage, setage, None)

"""
x = Properties()
x.age = 43
print(x.age)
x.name = 'bob'
print(x.name)
print('-'*25)

y = Operations()
y.age = 43
print(y.age)
y.name = 'tom'
print(y.name)
"""

class AgeDesc:
    def __get__(self, instance, owner): return f"get {40}"
    def __set__(self, instance, value):
        print(f"set")
        instance._age = value

class Descriptors:
    age = AgeDesc()
"""
x = Descriptors()
print(x.age)
x.age = 45
print(x._age)"""
