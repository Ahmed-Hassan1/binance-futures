from django.urls import path
from .views import *

urlpatterns = [
    path('',homePage,name="home"),
    path('table/',table,name="table"),
    path('table_1/',table_1,name="table_1"),
    path('table_5/',table_5,name="table_5"),
    path('table_15/',table_15,name="table_15"),
    path('table_30/',table_30,name="table_30"),
]