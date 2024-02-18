use liang
db.stu.insertMany([{"name":"张三","age":45,"gender":"man"},
{"name":"张三风","age":45,"gender":"woman"},
{"name":"李氏","age":75,"gender":"man"},
{"name":"王五","age":55,"gender":"woman"},])
db.stu.find()
// 查询条件为{}表示修改所有数据
db.stu.update({},{$set:{age:1}},{multi:true})
db.stu.remove({}, {justOne:false})
// 自定义查询
db.stu.find({
$where:function(){
    return this.age>45 ;
}
})
// $or and逻辑
db.stu.find({$or:[{age:45},{gender:"man"}]})
db.stu.find({age:45,gender:"man"})
// 投影{条件}，{字段1:1,,,} 1：表示显示 _Id 默认显示
db.stu.find({age:{$gt:45}},{_id:0,name:1,age:1,})
// 排序().sort({key:1....}) 1升序 -1降序
db.stu.find({}).sort({age:-1})
