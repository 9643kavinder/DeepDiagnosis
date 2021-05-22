from rest_framework import serializers
from . models import UserAuth

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['name', 'email', 'phone', 'gender']

