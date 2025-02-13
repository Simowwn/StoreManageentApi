from rest_framework import serializers
from .models import Stall, Owner

class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = "__all__"

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
