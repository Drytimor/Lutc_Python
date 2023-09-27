class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1

    @staticmethod
    def printNumInstance():
        print(f"Number of instance {Spam.numInstance}")



class Sub(Spam):
    @staticmethod
    def printNumInstance():
        print('Extra staff...')
        Spam.printNumInstance()


class Other(Spam): pass

a = Sub()
b = Sub()
c = Other()
a.printNumInstance()
b.printNumInstance()
c.printNumInstance()
