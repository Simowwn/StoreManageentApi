from rest_framework import serializers
from .models import Stall


class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = "__all__"
        read_only_fields = ["owner"]
        depth = 1
