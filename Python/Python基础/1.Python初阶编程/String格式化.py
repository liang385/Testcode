import time


def run():
    # 字符串的格式化
    # 1:%
    print('%.3f' % 20)
    # 2:format格式化
    print('{}{}'.format('hello', 'world'))
    strl =5000.000
    print("所得利息：", format(strl, '.2f'))


if __name__ == "__main__":
    run()
