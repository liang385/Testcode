from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import *
from App.models import *


# 导入models模板

# Create your views here.
#


def index(request):
    # render渲染模板一个html文件作为response
    # 主页
    return render(request, 'js.html')


def index01(request):
    # 模型操作获取用户信息
    Appusers = Appuser.objects.all()
    return render(request, 'user.html', {"users": Appusers})


def index02(requset, uid):
    # 用户详情传递一个参数
    users = Appuser.objects.get(pk=uid)
    return render(requset, "Usertail.html", {"users": users})


def index03(request):
    # DjangoTemplate语言
    data = {
        'name': "zhangsan",
        "age": 45,
        "province": ["广东", "深圳", "河北"],
        "stars": [["张三丰", "雷军", "杨幂"],
                  ["李四", "马化腾", "迪丽热巴"],
                  ["吴亦凡", "雷军", "刘强东"]
                  ]
    }
    return render(request, 'DjanTem.html', data)


def liang(request):
    # 反向解析使用路径别名替代URL路径
    return redirect('/App/index/')
