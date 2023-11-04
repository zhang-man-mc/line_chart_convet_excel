"""装饰器"""


def re_add(func):
    print("装饰器add运行了")

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


if __name__ == "__main__":
    # a = avg()
    # print(a(4))
    # print(a(5))
    # print(a(6))

    b = avg_1()
    print(b(1))
    print(b(2))
    print(b(3))
    print(b(4))
