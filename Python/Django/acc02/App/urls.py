from django.urls import *
from App.views import *

urlpatterns = [
    path("add/", add),
    path("del/", dell),
    path("upd/", update),
    path("get/", get),
    path("paginate/<int:page>/", paginate)
]
