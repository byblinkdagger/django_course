from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse,HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    pass
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("index")