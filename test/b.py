from test.a import A
from test.single import add, get, reset

import requests


class B:
    def __init__(self):
        self.b_class = A()
        self.b = self.b_class.a_class

    def output(self):
        print(get())

    def test(self, a, b, c, d, e, f, g, h, i, j, k, l):
        pass


b = B()
b.output()
print(b.b)
