class ListInherited:

    def __attr_name(self, indent=' '*4):
        under = []
        result = f'Unders{"-"*77}\n{indent}%s\nOthers{"-"*77}\n'
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                under.append(attr)
            else:
                result += f"\t{attr}={getattr(self, attr)}\n"
        return result % ', '.join(under)

    def __str__(self):
        return f"Instance of {self.__class__.__name__}, {id(self)}:\n{self.__attr_name()}"


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)


