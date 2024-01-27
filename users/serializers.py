import datetime
from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'birthday', 'password']
    
    def create(self, data):
        password = data.pop('password', None)
        user = self.Meta.model(**data)
        if user.birthday >= datetime.date.today():
            raise ValidationError('The date cannot be in the future.')
        if password is not None:
            user.set_password(password)
        user.save()
        return user