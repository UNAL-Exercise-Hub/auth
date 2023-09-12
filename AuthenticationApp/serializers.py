from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Login

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = ['UserId', 'UserEmail', 'UserPasswordHash']
        read_only_fields = ('UserId',)

    def create(self, data):
        data['UserPasswordHash'] = make_password(data['UserPasswordHash'])
        return super(LoginSerializer, self).create(data)
    
    def validate(self, data):
        if(data['UserPasswordHash'] in )