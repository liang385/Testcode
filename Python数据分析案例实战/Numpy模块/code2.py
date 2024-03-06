import numpy as np

# 随机生成数
# 1.rand()生成一个任意维度的数组，数组的元素取自0—1上的均匀发布
a = np.random.rand(2, 3, 2)
print(a)
print(a.shape)
print(a.ndim)
# 2.randint()生成指定范围的随机数
a1 = np.random.randint(2, 10, size=(2, 2, 3))
print(a1)
print(a1.shape)

# 3.random()生成一个0-1的浮点数的数组
c = np.random.random((2, 3))
print(c)

# 4.切片和所引
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b[0, 1:4])

# 5.改变数组的形状
# 5,1numpy.reshape(a,newshape,order='c') 其中newshape为新的shape,order表示按什么方式排列
d = np.arange(9).reshape(3, 3)
print(d)
# 5,2ravel()函数展平数组
print(d.ravel(order='F'))
# 5.3 hstack(),vstack()分别实现水平和垂直堆叠数组
# 5.4 数组分割hsplit(),vsplit(),split()
