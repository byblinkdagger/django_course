from django.conf.urls import url
from . import views

# lxg lxg123456
urlpatterns = [
    # 主页
    url(r'^index$', views.index, name='index'),

    # 登录
    url(r'^login/', views.login,name='login'),

    # 注册
    url(r'^register/', views.register,name='register'),

    # 登出
    url(r'^logout/', views.logout,name='logout'),

]
