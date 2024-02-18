class Demomethod(object):  # 继承object类
    # 私有属性方法用__开头
    __hair = 'black'  # 定义类变量

    # 定义魔术方法init创建一个对象是默认被调用 self表示类的实例
    def __init__(self, name, age):
        # 创建类的实例属性创建类实例时需要传递参数
        self.name = name
        self.age = age

    def show(self):
        # f-String格式化
        print(f'姓名：{self.name} 年龄: {self.age} ')


#
a = Demomethod('张三', 20)
print(a.name)
a.show()
