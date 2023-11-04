from test.single import add


class A:
    def __init__(self):
        self.a_class = add()


def sub(a: int, b: int):
    return a - b


print(sub(5, 1))
