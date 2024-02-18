# 正则表达式使用方法
import re

# 1:普通字符：字母，数字，汉字，下划线
# 2：多元字符：.:匹配除换行符'/n'以外的所有字符 [^]:表示不匹配，-：定义[]里的字符区间[a-z]
# 3:转义字符：以'/'的方式
# 4：预定义匹配字符集：\d:匹配0-9任意一个数字 \w:匹配一个任意数字，下划线，字母
# \s:匹配 空格，制表符，换页符，等空白字符的任意一个 大写表示相反 如\w [^/w]
# 5:重复匹配 {n}, {n,m},{m,} ?:匹配表达式0或1次 +:匹配表达式{1，} *：匹配表达式{0，}
# 6：位置字符: ^字符串开始的地方匹配  ￥结束的地方开始匹配

# 语法
# search(pattern ,string,flags)方法 其中flags表示：标注位，默认为0
# span():表示以元组的方式返回范围 group:以str返回search的元素
a = "function"
print(re.search('tion', a).span())
print(re.search('tion', a).group())

# match()方法：从字符开始的位置匹配一个模式，匹配成功则返回匹配信息,
str1 = 'www.pt press.com'
print(re.match('^w{0,3}.p',str1))

# findall()在整个字符串中查找匹配模式，返回所有匹配的信息，
# 不能使用span()和，group()方法，返回结果是列表

b=a*2
print(re.findall('tion',b))

