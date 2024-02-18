from django.shortcuts import *
from App.models import *
from django.core.paginator import *


# Create your views here.
# 增加
def add(request):
    # 方式一：创建对象实例通过p.save()保存
    # p = Person()
    # p.name = 'dff'
    # p.age = 99
    # p.save()
    try:
        # 方法二:创建对象并初始化
        # P = Person(name="王东方", age=78)
        # P.save()
        # 方法三：使用create方法可以防止重复
        # Person.objects.create(name="sdd", age=98)
        # 方法四
        # Person.objects.get_or_create(name="sdfsf", age=65)
        for i in range(1, 100):
            Person.objects.create(name=f'王{i}发', age=i)
    except Exception as e:
        return HttpResponse("添加失败")
    return HttpResponse("添加成功")


def dell(request):
    # 1:删除所有数据
    # Person.objects.all().delete()
    # 2:删除指定数据
    # Person.objects.filter(uid=23).delete()
    # 3:使用对象模型删除数据
    P = Person.objects.get(id=1)
    P.delete()
    return HttpResponse("删除成功")


def update(request):
    # 模型没有定义update方法，直接给字段赋值,调用save()方法实现update
    P = Person.objects.get(uid=24)
    P.name = "rfgsds"
    P.save()
    return HttpResponse("修改成功")


def get(request):
    # 查询
    p = Person.objects.all().values("name")
    print(p)
    # 传递的数据为字典类型
    return render(request, "get.html", {"p": p})


def paginate(request, page=1):
    # 分页功能
    per_page = 10
    datas = Person.objects.all()
    paginator = Paginator(datas, per_page)
    # 获取page页的数据
    persons = paginator.page(page)
    # 获取遍历范围，可以遍历
    page_range = paginator.page_range
    # 传递的参数为字典dict
    date = {"persons": persons, "page_range": page_range}
    return render(request, "paginate.html", date)
