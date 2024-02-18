"""
python序列分类  有序：字符串 元组，列表  无序：集合，字典
不可变序列：字符串，元组  可变序列：列表，集合，字典
"""

# 1：转义字符\n
str1 = "python\npython"
print(str1)
# 2: 字符串的格式化“% ，format,f-String"
# %十六进制输出
print('%x' % 20)
# f-Strings格式化
# 结构F(f)+str,字符串中想替代的位置用{}占位符，可以直接识别字符串后边写写入的替换内容
name = 'liang'
age = '18'
msg = F'姓名:{name},年龄：{age}'
print(msg)
# 它可以加任意表达式
print(f'计算结果：{3 * 21}')
print(f'全部大写：{name.upper()}')
print(type('%.2f' % 314.9256))
#str="asdffda".pop()
print(str)
