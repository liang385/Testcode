from django.shortcuts import *
from user.models import *


# Create your views here.
# 首页
def index(request):
    # 获取cookie userid默认值为0
    # userid = request.COOKIES.get("userid", 0)
    # 获取session
    userid = request.session.get("userid")
    # 结果为一个查询集需要遍历
    users = User.objects.filter(id=userid)
    # 获取当前登录对象
    user = users.first()
    return render(request, "index.html", {"user": user})


# 注册
def register(request):
    # 接收前端来的数据
    if request.method == 'GET':
        return render(request, "register.html")
    elif request.method == "POST":
        uname = request.POST.get("username")
        passwd = request.POST.get("password")
        email = request.POST.get("email")
        # print(uname, passwd, email)

        # 先判断用户是否已经存在
        users = User.objects.filter(username=uname)
        if users.exists():
            return HttpResponse("用户已经存在")

        # 实现注册功能
        try:
            user = User()
            user.username = uname
            user.password = passwd
            user.email = email
            user.save()
        except:
            return HttpResponse("注册失败")
        # 返回index页面
        return HttpResponseRedirect('/user/index')


# 登录
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        # 接收前端来的数据
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username, password=password)
        # print(users.first())
        if users.exists():
            # 获取当前登录对象
            user = users.first()
            # 设置cookie
            # 注意cookie存储在游览器，不可以跨域，跨游览器，存储的大小为字符串，不能为中文
            # 登录后跳转回首页
            response = redirect("/user/index")
            # 设置cookie  max_age过期时间 单位秒
            # response.set_cookie("userid", user.id, max_age=7 * 24 * 3600)

            # 设置session,session基于cookie,存储在服务员端
            request.session['userid'] = user.id
            # 设置过期时间
            request.session.set_expiry(7 * 24 * 3600)
            return response


# 注销
def delete_user(request):
    # 删除session
    session_key = request.session.session_key
    request.session.delete(session_key)

    return HttpResponse("注销成功")
