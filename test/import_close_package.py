# import test_close_package

# from test.test_close_package import ClosePackage
a = [1, 2, 3, 4, 5]


def best(oder):
    return max((item) for item in oder)


def test_if(value):
    return value if value > 2 else 1


print(best(a))
print(test_if(12))
