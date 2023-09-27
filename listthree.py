class ListTree:

    def __attr_name(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += f'{spaces}{attr}\n'
            else:
                result += f'{spaces}{attr}={getattr(self, attr)}\n'
        return result

    def __list_class(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return (f"{dots}"
                    f"<Class {aClass.__name__}: "
                    f"address {id(self)}: (see above)>\n")
        else:
            self.__visited[aClass] = True
            here = self.__attr_name(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__list_class(super, indent+4)
            return (f"{dots}"
                    f"<Class {aClass.__name__}, "
                    f"address {id(aClass)}: \n {here} {above} {dots}>\n")

    def __str__(self):
        self.__visited = {}
        here = self.__attr_name(self, 0)
        above = self.__list_class(self.__class__, 4)
        return (f"<Instance of {self.__class__.__name__},"
                f"address {id(self)}:\n{here} {above}>\n")

import testmixin
print(testmixin.tester(ListTree))