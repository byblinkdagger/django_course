from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from .models import User
from .forms import UserForm, RegisterForm
import hashlib
from django.core import serializers


# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect("index")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    # 设置session过期时间 120秒
                    request.session.set_expiry(120)
                    return redirect('index')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())
                new_user = User()
                new_user.name = username
                # new_user.password = hash_code(password1)
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("index")
    request.session.flush()
    return redirect("index")


# @require_GET
def getUserData(request):
    from .entity import baseRes
    userdata = list(User.objects.all().values())
    return JsonResponse({"code": 0,
                         "content": list(userdata),
                         "msg": "success"}, safe=False)


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['GET'])
def getlist(request, format=None):
    if request.method == 'GET':
        user = User.objects.all().distinct()
        serializer = UserSerializer(user, many=True)
        # return Response(serializer.data)
        #
        # # http: // 127.0.0.1:8000 / getlist?limit = 20
        # # http: // 127.0.0.1:8000 / getlist?limit = 20 & offset = 20
        # # http: // 127.0.0.1:8000 / getlist?limit = 20 & offset = 40
        # # 根据url参数 获取分页数据
        # obj = StandardResultSetPagination()
        # page_list = obj.paginate_queryset(meizis, request)
        # # 对数据序列化 普通序列化 显示的只是数据
        # ser = ListSerialize(instance=page_list, many=True)  # 多个many=True # instance：把对象序列化

        response = serializer.data
        # return JsonResponse({"code":0,
        #                  "content":response,
        #                  "msg":"success"},safe=False)

        print(type(serializer.data))
        print(serializer.data)

        return Response({"code": 0,
                         "content": response,
                         "msg": "success",
                         }, status=status.HTTP_200_OK)


@api_view(['POST'])
def getUser(request, format=None):
    if request.method == 'POST':
        # 获取token,
        # 用于获取header的信息
        # 注意的是header
        # key必须增加前缀HTTP，同时大写，例如你的key为username，那么应该写成：request.META.get("HTTP_USERNAME")
        # 另外就是当你的header
        # key中带有中横线，那么自动会被转成下划线，例如my - user的写成： request.META.get("HTTP_MY_USER")
        token = request.META.get("HTTP_TOKEN")
        if not token:
            return Response({"code": -1,
                             "msg": "缺少Token !",
                             }, status=status.HTTP_200_OK)
        try:
            name = request.POST['name']
        except:
            return Response({"code": -1,
                             "msg": "缺少参数name",
                             }, status=status.HTTP_200_OK)

        user = User.objects.all().filter(name=name)

        if user:
            serializer = UserSerializer(user, many=True)
            response = serializer.data
            return Response({"code": 0,
                         "content": response,
                         "msg": "success",
                         }, status=status.HTTP_200_OK)
        else:
            return Response({"code": -1,
                         "msg": "查无此人",
                         }, status=status.HTTP_200_OK)
