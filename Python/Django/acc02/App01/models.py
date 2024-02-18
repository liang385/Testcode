from django.db import models


# Create your models here.

# 一对多关系 : 多个User对应一个User_type
class User_type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}-{self.type}'


class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # 外键 :在多的一方
    user_type = models.ForeignKey(User_type, on_delete=models.CASCADE)  # 级连删除

    # models.ManyToManyField() 多对多
    # models.OneToOneField()   一对一
    def __str__(self):
        return f'{self.id}-{self.name}-{self.age}-{self.user_type}'
