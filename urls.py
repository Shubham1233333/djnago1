from django.contrib import admin
from django.urls import path
from products import views
urlpatterns = [
path('',views.home ,name="home"),
 path('add/',views.add ,name="add"),
 path('cart/',views.cart ,name="cart"),
  path('query/',views.query ,name="query"),
 #
 # 
 #
]#
