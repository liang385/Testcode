# 函数的使用

# 长度可变参数 *p:接收的任意多个参数并将传递的参数放在一个元组中
def demo_tuple(*p):
    print(p)


# **p:收的任意多个参数并将参数放在一个字典中
def demo_dict(**p):
    for item in p.items():
        print(item)


# 使用**p指定参数是必须指定形参值
demo_tuple(1, 2, 3)
demo_dict(x=1, y=2, z=3)

# 枚举与迭代：enumerate()函数用来枚举可迭代对象中的元素，返回包含索引和值的元组
# 用法
list = list(enumerate('abcd'))
print(list)

for index, value in enumerate(range(10, 15)):
    print((index, value), end='')
