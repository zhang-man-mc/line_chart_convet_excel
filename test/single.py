class Single:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def set(self, value):
        self.a = value

    def get(self):
        return self.a, self.b


_sing = Single(2, 3)

add = _sing.add
reset = _sing.set
get = _sing.get
