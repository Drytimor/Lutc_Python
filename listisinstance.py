class ListInstance:
    def __attr_name(self):
        return ''.join(f"\t{key}={value}\n" for key, value in self.__dict__.items())

    def __str__(self):
        return f"Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attr_name()}"



class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'Food'

x = Spam()  # Instance of Spam, address 4344539088:
                        # data1=Food


class Super:
    def __init__(self, data5, data1='spam'):
        self.data1 = data1
        self.data5 = data5
    def spam(self): pass


class Sub(Super, ListInstance):
    def __init__(self, data2='eggs', data3=42):
        Super.__init__(self, data5=None)
        self.data2 = data2
        self.data3 = data3
    def ham(self): pass


x = Sub()




