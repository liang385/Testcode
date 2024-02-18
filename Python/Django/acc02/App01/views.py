from django.http import JsonResponse
from django.shortcuts import *
from App01.models import *


# Create your views here.


def adduser(request):
    for i in range(11, 20):
        User.objects.create(name=f'张{i}风', age=i,
                            user_type=User_type.objects.get(pk=i % 6 + 1))
    data = ['青铜', '白金', '铂金', '黄金', '砖石', '大师', '王者']
    # for i in data:
    #     User_type.objects.create(type=i)
    return HttpResponse("添加成功")


def delUser(request):
    # 删除数据
    # User_type.objects.filter(id=7).delete()
    User_type.objects.filter(id=6).delete()
    return HttpResponse("删除成功")


def updateUser(request):
    # 更新数据
    User_type.objects.filter(id=5).update(type="王者")
    return HttpResponse("修改成功")


def getUser(request):
    # 1:正向查询从User表查询User_type
    user = User.objects.get(id=2)
    print(user.id, user.name, user.age, user.user_type, user.user_type_id)
    # user.User_type属性值
    print(user.user_type.id, user.user_type.type)
    print("*" * 60)
    # 2:反向查询
    user_type = User_type.objects.get(type='白金')
    print(user_type.id, user_type.type)
    # user_set：内部自动生成可以让你反向查询到所有User集合 表名_set
    # 结果为查询集
    print(user_type.user_set.all())
    print("*" * 60)
    # 3:使用filter,查询user_type为白银的所有用户
    us = User.objects.filter(user_type=User_type.objects.get(type='白金'))
    print(us)
    return HttpResponse("查询成功")


def my_request(request):
    # Django中视图用来接收Web请求，并做出response
    # 视图的相应分为两类：1：json数据返回JsonResponse 2:网页形式
    # 视图参数 1：一个HttpResponse实例，2：通过url正则表达式传递过来的参数
    # request：方法和参数

    print(request)
    # <WSGIRequest: GET '/App01/my_request/'>
    # 请求方式
    print(request.method)
    # 请求路径
    print(request.path)
    # 从url传递数据 url/?name=lisi&age=45
    print(request.GET)  # <QueryDict: {}> 类字典对象
    print(request.GET.get('name'))  # 推荐使用
    print(request.POST)
    # 会话技术
    print(request.COOKIES)
    print(request.session)

    print(request.body)
    return HttpResponse("ok")


def my_Response(request):
    # 1:返回HttpResponse()
    # 2:返回模板 dict数据  前后的不分离
    # render()
    # 3:重定向
    # return redirect("/response//")
    # 返回json数据
    return JsonResponse({"date": "hello"})    # 前后端不分离返回json数据
