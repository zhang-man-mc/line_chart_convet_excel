import functools


def factory(value=1):
    print("这是工厂函数")

    def decorate(func):
        print(f"这是装饰器函数,拿到参数{value}")

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            """包装函数"""
            r = func(*args, **kwargs)
            return r

        return wrap

    return decorate


@factory(value=4)
def add(a, b):
    """普通函数"""
    print(f"普通函数,传进来的参数为{a},{b}")


def param(a=None, *, b=1):
    print("hello")


if __name__ == "__main__":
    a = add
    print(a.__name__)
    print(a.__doc__)
    param(b=1)
