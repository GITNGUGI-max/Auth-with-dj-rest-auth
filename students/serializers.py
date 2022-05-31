from dataclasses import field
from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'classroom' ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ['url', 'id', 'username', 'email', 'password']

