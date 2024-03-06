import numpy as np

# numpy模块主要用于数组计算，支持多种数据类型
# ndarray对象是numpy模块的基础对象，用于存放同类型的多维数组，而数据类型是由dtype对象指定

# 1:创建ndarray对象
a = np.array([1, 2, 3, 4, 5])
print("a的内容", a)
print("a的数组类型", a.dtype)
print("a的形状", a.shape)
print("数组的维度", a.ndim)
print("数组的长度", a.size)

# 2:内置的数组创建方法 ,zeros() ones()
a1 = np.ones(shape=(4, 3))
print(a1)

# 3:arange(),linspace(),logspace(),eye(),diag()函数
# 3.1创建指定数值范围的运维数组
a2 = np.arange(1, 10, 1)
a3 = np.linspace(0, 1, 10)
print(a2)
print(a3)
# 3.2创建等比数列
# 创建数值2的0-9次幂，数组的长度为10
a4 = np.logspace(0, 9, 10, base=2)
print(a4)
# 3.3 eye()用于生成对角线为1，其他元素为0的数组，diag()用于指定对角线元素，其他元素为0
a5 = np.eye(3)
a6 = np.diag([1, 2, 3, 4, 5])
print(a5)
print(a6)

