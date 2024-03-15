import pandas


# pandas的数据结构，Series和DataFrame,Series是一维数组，DataFrame是一种二维的表格形式的数据类型
# 创建Series对象
def runSeries():
    data = ['A', 'B', 'C']
    index = ['a', 'b', 'c']

    series = pandas.Series(data=data, index=index)
    # 单独访问，索引和元素数组
    print(series.values)
    print(series.index)
    # 获取索引对应的元素，
    print(series[['a', 'b']])
    # print(series[1])
    # 修改元素值(元素没有在Series中时可添加)
    series['d'] = 'D'
    print(series)


def runDataFrame():
    # 创建DateFrame对象需要通过字典来实现，其中每列为键，每个键对应一个数组作为值。
    data = {"A": [1, 2, 3, 4, 5],
            "B": [2, 3, 4, 5, 6],
            "C": [3, 4, 5, 6, 7],
            "D": [4, 5, 6, 7, 8]}
    index = ['a', 'b', 'c', 'd', 'e']
    # data_frame = pandas.DataFrame(data=data, index=index)
    # 如果不需要列的数据可以在创建DataFrame时指定通过columns指定
    data_frame = pandas.DataFrame(data=data, index=index, columns=["A", "B"])
    print(data_frame)


if __name__ == "__main__":
    runDataFrame()
    # runSeries()
