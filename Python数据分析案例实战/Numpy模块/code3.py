import numpy as np
from numpy import matlib

# numpy模块中的函数的应用

# 1.三角函数
a = np.array([0, 30, 60, 90])
print("six值", np.sin(a * np.pi / 180))
print('cos值', np.cos(a * np.pi / 180))
print('tan值', np.tan(a * np.pi / 180))

# 2.算术函数主要是直接针对数组，数组的形状shape需要符合数组广播的规则。
a = np.random.random(6)
b = np.random.random(6)
print('a+b', np.add(a, b))
print('a*b', np.multiply(a, b))
print('1/a', np.reciprocal(a))

# 3.统计函数
# 3.1amax()获取数组中的最大值，axis=0时通过列的方式进行获取，axis=1通过行的方式进行获取
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('原数组c:\n', c)
print('行的方式获取\n', np.amax(c, axis=1))
# 3.2 ptp()计算数组元素的最大值和最小值的差，sum()计算数组元素的所有元素之和 axis参数和之前一致
print('以行的方式计算数组c元素的差\n', np.ptp(c, axis=1))

# 4.矩阵函数
# numpy模块通过了一个matlib子模块，模块中的函数返回值是一个矩阵
# 随机数矩阵,matlib.ones()和matlib.zeros分别用1，0填充位置
d = matlib.empty(shape=(3, 3), dtype='int32')
print('矩阵d\n', d)
# 创建和将数组转化成矩阵
print('将数组转化为矩阵\n', np.mat(c))
print('创建矩阵\n', np.mat("123,345;345,232"))

# 广播机制不同shape的数组算术运算时需要符合计算的条件
