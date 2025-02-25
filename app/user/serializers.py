from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True) -- ANOTHER OPTION FOR WRITE/READ ONLY ---

    class Meta:
        model = Users
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_staff",  # Staff status
            
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["user_permissions", "groups", "last_login", "date_joined", "is_active", "is_superuser"]
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
