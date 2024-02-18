from django.urls import *
from user.views import *

urlpatterns = [
    path("index/", index, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("delete/", delete_user, name="delete"),

]
