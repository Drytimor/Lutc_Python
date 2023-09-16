class AttrDisplay:
    """Отображает принадлежность к классу
    и атрибуты экземпляра данного класса"""
    def __gather_attrs(self):
        attrs = [f"{key}={value}" for key, value in sorted(self.__dict__.items())]

        return ', '.join(attrs)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__gather_attrs()}"





if __name__ == '__main__':
    class TopClass(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopClass.count
            self.attr2 = TopClass.count + 1
            TopClass.count += 2

    class SubClass(TopClass):
        pass

    x, y = TopClass(), SubClass()
    print(x)
    print(y)

