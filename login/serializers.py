from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 等价于  fields = "__all__"   用于控制解析哪些字段
        fields = ('name', 'password', 'email', 'sex', 'c_time')
