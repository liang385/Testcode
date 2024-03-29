import pandas
import pymysql
import sqlalchemy


# 通过pandas读,写excels,database,csv文件数据。

def readscsv():
    # 通过pandas.read_csv()方法读取csv文件内容
    data = pandas.read_csv(filepath_or_buffer='file/test.csv', encoding='gbk')
    print("文件内容\n", data)
    # 文件内容写入to_csv()方法,将读取的文件写入new_test.csv文件
    data.to_csv("file/new_test.csv", columns=['name', 'age'], encoding='gbk')
    data1 = pandas.read_csv(filepath_or_buffer='file/new_test.csv', encoding='gbk')
    print("new_test.csv文件内容\n", data1)


def readexcels():
    # 通过pandas.read_excel()函数读取Excel文件内容
    data = pandas.read_excel(io="file/test.xlsx", engine='openpyxl')
    print("读取的文件内容\n", data)


def readdatabase():
    # pandas数据库操作
    # 创建Mysql连接池对象
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           db='django',
                           port=3306)
    # sql查询语句
    sql = "select * from infor where id<=2;"
    sql_query_data = pandas.read_sql(sql=sql, con=conn)
    print("通过read_sql方法读取的数据库信息\n", sql_query_data)
    # 写入数据库数据
    print("*" * 30)
    # pandas提供了to_sql方法实现数据库的写入工作，通过DateFrame数据对象调用，需要SQlAlchemy模块支持
    # 使用sqlalchemy模块连接数据库
    sqlalchemy_db = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/django")
    data = {"name": ['liang'], "age": [20], "sex": ["na"]}
    # 创建DateFrame对象
    data_frame = pandas.DataFrame(data, index=None)
    sql1 = "select * from infor;"
    # 插入数据时DateFrame会自动添加index,属性
    data_frame.to_sql("infor", con=sqlalchemy_db, if_exists="append")
    # 通过read_sql()读取信息
    read_sql_data = pandas.read_sql(sql1, con=sqlalchemy_db)
    print("读取写入的信息\n", read_sql_data)


if __name__ == "__main__":
    pass
    # readexcels()
    # readdatabase()
    # readscsv()
