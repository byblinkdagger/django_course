from django.conf.urls import url, include
from . import views

# lxg lxg123456
urlpatterns = [
    # 主页
    url(r'^index/', views.index, name='index'),

    # 登录
    url(r'^login/', views.login, name='login'),

    # 注册
    url(r'^register/', views.register, name='register'),

    # 登出
    url(r'^logout/', views.logout, name='logout'),

    # 验证码
    url(r'^captcha', include('captcha.urls')),

    # 获取用户数据
    url(r'^user/data$', views.getUserData),

    # rest-framework
    url(r'^rest/data$', views.getlist),

    url(r'^rest/user$', views.getUser),

]
