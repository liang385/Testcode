import pymysql

db_connection = pymysql.connect(
    # 1:建立与数据库的连接对象，需要指定与数据库的连接相关的属性
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="liang"
)
# 这个数据库连接对象，在使用结束后，需要调用close来释放资源
# db_connection.close()
#
# 2:获取到的是一个光标对象，数据库所有的操作都需要使用这个对象来完成 例如：DDL、DML、DQL语句
# print(db_connection)
db_cursor = db_connection.cursor()
# 3:准备执行的SQL语句
#   使用数据库操作对象，执行SQL语句 执行的返回值是一个数字，表示多少行数据受影响 (affected rows)
sql = "select * from bank_account"
db_cursor.execute(sql)

#  4:获取查询到的所有的数据
#  将查询到的每一行的数据存入一个元组，再将这些元组存入一个大的元组返回 即返回的结果是一个二维元组
datas = db_cursor.fetchall()
for data in datas:
    print(data)


# 插入数据
sql="insert into bank_account values (null,'7225113088436228',550,'niumo','nm123456','100000100010101003','2019-03-01 10:10:10','m');"
db_cursor.execute(sql)

# 提交事
db_connection.commit()
