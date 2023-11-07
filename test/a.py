import collections.abc


class A:
    def __init__(self):
        self.text = "你好"

    def __repr__(self):
        print("调用了实例")

    # def __iter__(self):
    #     return self

    def __getitem__(self, item):
        return self.text[item]

    def __next__(self):
        return


a = A()
print(a.text)
# print(iter(a))
print(isinstance(a, collections.abc.Iterable))
list
