import pymongo

# 创建数据库连接对象
client = pymongo.MongoClient(
    host='localhost',
    port=27017
)

# print(client)
# 选择一个数据库
db = client['liang']
# 选择一个集合
collection = db['stu1']

# 数据操作
dict = {"name": "张三", "hometown": "四川", "age": 40, "sex": "男"}
# print(collection.insert_one(dict).inserted_id)
# 字典类型
print(collection.find_one())
print(collection.find())
