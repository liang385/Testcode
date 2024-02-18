//1： 创建数据库
use liang;
//2： 查看当前数据库
db;
//3：删除当前数据库db.dropDatabase()
//4： 创建，删除，显示集合 
// 参数 options :指定有关内存大小及其index的选项,name为字符串
db.createCollection("stu");
db.stu.drop()
show db.collections
// 插入文档:存储的数据结构和Json数据一样，为二进制的Bson格式,会自动添加一个主键_id
// 方法1
db.stu.insertOne({"_id":1,"name":"张三","age":38,"gender":"man",});
// 方法2 :创建数组，将数据放入数组中一次性插入
db.stu.insertMany([
{"_id":2,"name":"张三风","age":38,"gender":"man",},
{"_id":3,"name":"李四","age":55,"gender":"woman",},
{"_id":4,"name":"张人","age":89,"gender":"man",},
{"_id":5,"name":"沃达丰","age":79,"gender":"woman",},
{"_id":6,"name":"东莞市","age":999,"gender":"man",},])

// 自动添加一个字段
db.stu.insert({"idcare":"564"})

// 查询文档 pretty()格式化输出
db.stu.find().pretty()
// 修改：save()文档——id存在则修改，不存在则添加,没有的字段设置为null
db.stu.save({"_id":1,"name":"李四"})
db.stu.update({"name":"李四"},{"name":"修改后的数据"})
// 修改全部匹配的数据multi="true"需要配合$set使用
db.stu.update({"name":"李四"},{$set:{"name":"修改的数据"}},{multi:"true"})
//  删除数据JustOne:为1 or true删除一条记录，为false则都删除
db.stu.remove({gender:"woman"},{justOne:false})
db.stu.remove({})
// 查询数据 db.stu.find({条件文档}) 
db.stu.findOne({age:38})
db.stu.find({age:38})
// 运算符 $lt $lte（less than equal） $gt $gte （greater than） $ne 不＝
db.stu.find({age:{$ne:38}})
db.stu.find({age:{$gte:38}})
// 范围运算符 $in $nin [40,80]为数值不是范围
db.stu.find({age:{$nin:[40,80]}})
// 逻辑运算符 $or
db.stu.find({$or:[{name:"张三"},{gender:"man"}]})
db.stu.find({name:"张三",gender:"man"})
// 模糊查询，正则表达式 使用 // 或 $regex
// 以张开头
db.stu.find({name:/^张/})
db.stu.find({name:{$regex:"^张"}})
// limit:读取指定数量的文档
// skip:跳过指定数量的文档
// 查询前3条记录
db.stu.find().limit(3)
// 查询除前两条记录
db.stu.find().skip(2)
// 查询前五条记录的后两条记录
db.stu.find().limit(5).skip(3)
