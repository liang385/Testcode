from django.urls import *
from App.views import *

# 使用子路由url,一个应用对应一个子url


urlpatterns = [
    path("index/", index),
    path("index01/", index01),
    # 用户详情传递一个参数
    path('index02/<int:uid>/', index02, name="index02"),

    path('index03/', index03)
]
