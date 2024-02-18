from django.db import models


# 导入模板
# Create your models here.


# 用户类需要继承models.Model类
# Models<==>表结构
# Class属性<==>表字段
# 对象<==>表的一行记录
class Appuser(models.Model):
    # 将自动创建主键
    name = models.CharField(max_length=10)  # Sql :  name varchar(10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

    # 将数据显示在admin平台Appuser数据
    def __str__(self):
        return f'{self.name}-{self.age}-{self.sex}'
# 3：数据迁移:将模型Model映射到数据库的过程
# python ./manage.py makemigrations 生成迁移文件
# python ./manage.py migrate  执行迁移数据库创建表
