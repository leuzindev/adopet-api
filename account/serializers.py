from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups']
        extra_kwargs = {'password': {'write_only': True}}
