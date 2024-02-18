// 聚合(aggregate)是基于数据处理的聚合管道，每个文档通过一个由多个阶段（stage）组成的管道，
// 可以对每个阶段的管道进行分组、过滤等功能，然后经过一系列的处理，输出相应的结果。
// 语法格式：db.集合名称.aggregate({管道:{表达式}})

// $group： 将集合中的文档分组，可用于统计结果 ,_id表示分组的依据，使用某个字段的格式为’$字段’
db.stu1.aggregate({
    $group:{
		_id:"$sex"}})
//统计男生、女生分别的总人数
db.stu1.aggregate(
	{$group:
		{
		_id:"$sex",
		count:{$sum:1}
		}
	}
)
db.stu1.aggregate(
	{$group:
		{
		_id:"$sex",
		count:{$sum:1},
		avg_age:{$avg:"$age"}
		}
	}
)
db.stu1.aggregate(
	{$group:
		{
		_id:"$hometown",
		avg_age:{$avg:"$age"},
		count:{$sum:1}
		}
	}
)

// $match： 过滤数据， 只输出符合条件的⽂档
// 查询年龄大于等于18的男生、女生人数
db.stu.aggregate(
	{$match:{age:{$gte:18}}},
	{$group:{_id:'$sex',count:{$sum:1}}}
)



// $project： 修改输入文档的结构，如重命名、增加、删除字段、创建计算结果；简单来说就是修改输入输出的值
db.stu1.aggregate({$project:{_id:0, name:1, age:1}})



// $sort： 将输⼊⽂档排序后输出

// $limit： 限制聚合管道返回的⽂档数

// $skip： 跳过指定数量的⽂档， 并返回余下的⽂档

// $unwind： 将数组类型的字段进⾏拆
use liang
db.createCollection("stu1");
db.stu1.insertMany([
    {name: "张飞", hometown: "蜀国", age: 30, sex: "男"},
    {name: "关羽", hometown: "蜀国", age: 40, sex: "男"},
    {name: "刘备", hometown: "蜀国", age: 50, sex: "男"},
    {name: "曹操", hometown: "魏国", age: 45, sex: "男"},
    {name: "司马懿", hometown: "魏国", age: 45, sex: "男"},
    {name: "孙权", hometown: "吴国", age: 50, sex: "男"},
    {name: "貂蝉", hometown: "未知", age: 18, sex: "女"},
    {name: "西施", hometown: "越国", age: 18, sex: "女"},
    {name: "王昭君", hometown: "西汉", age: 18, sex: "女"},
    {name: "杨玉环", hometown: "唐朝", age: 18, sex: "女"}
]);


