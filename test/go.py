# 生成器示例
def my_generator():
    data = range(1000000)  # 生成一个包含100万个元素的范围
    for num in data:
        yield num**2


# 使用生成器
result = my_generator()  # 返回一个生成器对象
# print(next(result))  # 打印第一个平方数，此时只生成了一个值
# print(next(result))  # 打印第二个平方数，只生成一个新的平方数，不占用额外的内存空间
# print(next(result))  # 打印第二个平方数，只生成一个新的平方数，不占用额外的内存空间
# print(next(result))  # 打印第二个平方数，只生成一个新的平方数，不占用额外的内存空间


def my_iterator():
    data = range(1000000)  # 生成一个包含100万个元素的范围
    return (num**2 for num in data)


# 使用迭代器
result = my_iterator()  # 返回一个迭代器对象
print(next(result))  # 打印第一个平方数，此时会生成并占用所有的平方数
print(next(result))  # 打印第二个平方数，平方数已经生成并占用了大量内存空间
print(next(result))  # 打印第二个平方数，平方数已经生成并占用了大量内存空间
