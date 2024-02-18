from django.urls import *
from App01.views import *

urlpatterns = [
    path("adduser/", adduser),
    path("deluser/", delUser),
    path("upduser/", updateUser),
    path("getuser/", getUser),
    path("request/", my_request),
    path("response/", my_Response)
]
