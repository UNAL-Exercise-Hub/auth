from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import environ

from .models import Login

env = environ.Env()
environ.Env.read_env()

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ['UserId', 'UserEmail', 'UserPasswordHash']
        read_only_fields = ('UserId',)

    def create(self, data):
        data['UserPasswordHash'] = make_password(data['UserPasswordHash'], salt=env("SALT_JWT"))
        return super(LoginSerializer, self).create(data)

