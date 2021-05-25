from rest_framework import serializers
from . models import *

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['name', 'email', 'phone', 'gender']

