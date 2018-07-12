from django.test import TestCase
import hashlib

# Create your tests here.

# f = open("test.text", "r", encoding="utf-8")
# data = ""
# while True:
#     data += f.read(512)
#     if not f.read(512):
#         break
#
# f.close()
# print(data)

# pwd = b'l123456'
# md = hashlib.md5()
# md.update(pwd)
# secret = md.hexdigest()
# print(secret)

# from datetime import date,time
#
# print(date.max)
# print(date.min)
# today = date.today()
# print(today)
# print(today.isoweekday())
#
# print("--------------------------")
#
# import time
# print(time.ctime())
# print(time.strftime("%H:%M:%S"))


# import os
# # f = open("test.text", "r", encoding="utf-8")
# # filename = './test.txt'
# my_path=os.path.dirname(__file__)
# print(my_path)

# import os
#
# content_path = 'E:\\py_demos\\cloud'
# for f in os.listdir(content_path):
#
#     # 拼接文件完整路径
#     file_fullpath = os.path.join(content_path, f)
#
#     # 判断是否是文件
#     if os.path.isfile(file_fullpath):
#         print('loading {}'.format(file_fullpath))
#         print(f)


# import time
#
# class Timeit(object):
#     def __init__(self, func):
#         self._wrapped = func
#
#     def __call__(self, *args, **kws):
#         start_time = time.time()
#         result = self._wrapped(*args, **kws)
#         print("elapsed time is %s " % (time.time() - start_time))
#         return result
#
#
# @Timeit
# def func():
#     time.sleep(1)
#     return "invoking function func"
#
#
# if __name__ == '__main__':
#     func()  # output: elapsed time is 1.00044410133


#多继承的顺序问题： 深度第一，由左至右
# 此例的执行顺序 ：   Init (val = 5)  -->  Add2(val = 5 + 2) --> Mul5(val = 7 * 5) --> Incr(val = 35 + 1)
# class Init(object):
#     def __init__(self, value):
#         self.val = value
#
#
# class Add2(Init):
#     def __init__(self, val):
#         super(Add2, self).__init__(val)
#         # Init.__init__(self,val)
#         self.val += 2
#
#
# class Mul5(Init):
#     def __init__(self, val):
#         super(Mul5, self).__init__(val)
#         self.val *= 5
#
#
# class Pro(Mul5, Add2):
#     pass
#
#
# class Incr(Pro):
#     csup = super(Pro)
#
#     def __init__(self, val):
#         self.csup.__init__(val)
#         self.val += 1
#
#
# p = Incr(5)
# print(p.val)
import os
import sys

#
# user = User(name = 'jack')
# user.save()

import django
django.setup()

from .models import User
from .serializers import UserSerializer

data = User.objects.all()
ser_data = UserSerializer(data)
print(type(ser_data.data))
print(ser_data.data)
