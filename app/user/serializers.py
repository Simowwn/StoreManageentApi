from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True) -- ANOTHER OPTION FOR WRITE/READ ONLY ---

    class Meta:
        model = Users
        fields = ("id", "email", "first_name", "last_name", "password")
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
