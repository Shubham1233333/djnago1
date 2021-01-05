from django.contrib import admin
from django.urls import path
from costomer import views
urlpatterns = [
    path('register/',views.register ,name='register'),
    path('signin/',views.signin ,name="signin"),
    path('logout/',views.logout_view ,name="logout"),
    path('buy/',views.buy ,name="buy"),
    path('orders/',views.orders ,name="orders"),
    
    #path('pd',views.pd ,name="pd"),
]

