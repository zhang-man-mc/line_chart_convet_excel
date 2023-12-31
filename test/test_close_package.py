"""装饰器"""
import functools
import time


def re_add(func):
    print("装饰器add运行了")

    @functools.wraps(func)
    def decorate(*args, **kwargs):
        for i in range(4):
            func()
        return None

    return decorate


def print_news(func):
    print("装饰器sub运行了")
    return func


@re_add
def add():
    print(1 + 2)


@print_news
def sub():
    print(10 - 5)


""" 高阶函数"""


def avg():
    v = [1, 2, 3]

    def cal_avg(value):
        v.append(value)
        length = len(v)
        sum_v = sum(v)
        return sum_v / length

    return cal_avg


def avg_1():
    count = 0
    sum_v = 0

    def cal_avg(value):
        nonlocal count, sum_v
        count += 1
        sum_v += value
        return sum_v / count

    return cal_avg


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(", ".join(pairs))
        arg_str = ", ".join(arg_lst)
        print("[%0.8fs]%s(%s)->%r " % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache(maxsize=128)
@clock
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    # a = avg()
    # print(a(4))
    # print(a(5))
    # print(a(6))

    # b = avg_1()
    # print(b(1))
    # print(b(2))
    # print(b(3))
    # print(b(4))

    # a = add
    # print(a.__name__)
    # print(fibonacci(30))
    print(fibonacci_1(30))
