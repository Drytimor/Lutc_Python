"""
class ShowAttr:

    def __name_attr(self):
        return ''.join(f"\t{key}={value}\n" for key, value in self.__dict__.items())

    def __str__(self):
        return f"Class {self.__class__.__name__}, address: {id(self)}\n{self.__name_attr()}"



class Sub(ShowAttr):
    def __init__(self):
        self.name = 'Bob'
        self.age = 40

x = Sub()

print(x)"""









