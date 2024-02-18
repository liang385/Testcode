# 文件的基本操作关闭，打开，读写
# 文件的创建和打开
# 使用方法open(name,mode,encoding)返回一个文件对象
# mode参数：a追加 w写 r读
# 打开文件
f = open('demo.txt', 'r', encoding="UTF_8")
# 文件对象.read(size)  size指定读取文件的字符个数
# read()方法打开文件的前提是指定打开模式我 r(只读),或r+(读写)
print(f.read(3))

# 注意文件的读取指针会随着读取函数的读取行为移动
string = f.readline()  # 一次读取一行内容
print(string)

# 读取文件的全部行，封装到列表中
list1 = f.readlines()
print(list1)
f.close()
# 文件的写入
with open("demo.txt", 'a', encoding="UTF_8") as f1:
    string1 = "查询是的"
    f1.write(string1)

# 内容刷新
f1.flush()  # 将内容写入文件
f1.close()  # 解除文件的占用
