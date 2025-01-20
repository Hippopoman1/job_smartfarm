
from django.urls import path 
from .views import *
urlpatterns = [
    path('home',home,name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', index,name='index'),
    path('dashboard/',dashboard,name='dashboard'),
    path('get_weather/', get_weather, name='get_weather'),  # API สำหรับดึงข้อมูลสภาพอากาศ
    path('weather/', lambda request: render(request, 'get_weather.html'), name='weather'),  # หน้า HTML
]
  
