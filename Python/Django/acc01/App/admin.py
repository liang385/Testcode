from django.contrib import admin

# Register your models here.
# 导入App.models
from App.models import *
# 后台管理系统的使用
# 1：在这里注册对应的模型
# 2：创建超级管理员 python manage.py createsuperuser
# 用户名admin 密码admin
# 3:重要作用修改数据库信息
admin.site.register(Appuser)
