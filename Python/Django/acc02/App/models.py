from django.db import models


# Create your models here.
class Userapp(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='张三')
    age = models.IntegerField(default=18, blank=False)
    salary = models.FloatField(max_length=6, default=5000)
    data = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True)

    # 将数据显示在admin平台Userapp数据
    def __str__(self):
        return f'{self.uid}-{self.name}-{self.age}--{self.salary}--{self.data}--{self.info}'


class Person(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, default="张三")
    age = models.IntegerField(default=20)

    def __str__(self):
        return f'{self.uid}-{self.name}-{self.age}'
