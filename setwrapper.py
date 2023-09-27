class Set(list):
    def __init__(self, value=[]):
        list.__init__(self)
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = [x for x in self.data if x in other]
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)
    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key]  # self[i], self[i:j]
    def __and__(self, other): return self.intersect(other)  # self & other
    def __or__(self, other): return self.union(other)  # self | other
    def __repr__(self): return f"Set: {repr(self.data)}"  # print(self)...
    def __iter__(self): return iter(self.data)  # for x in self...

"""
x = Set([1,2,3,4])
print(x.data)
y = x & (6,3,9,5)
c = x | (9,0,8)
print(y)
print(c)
for x in c:
    print(x)
    """
