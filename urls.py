from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework import routers

#from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
     path('', views.apisList.as_view() ,name="apisList"),
     path('', views.put.as_view() ,name="put"),
    path('api_tamplate/', views.api_tamplate ,name="api_tamplate"),
    path('api_register/', views.api_register ,name="api_register"),
    ]