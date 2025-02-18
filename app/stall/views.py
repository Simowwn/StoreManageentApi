from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Stall
from .serializers import StallSerializer
from rest_framework.response import Response
from rest_framework import status


class StallViewSet(viewsets.ModelViewSet):
    serializer_class = StallSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Stall.objects.all()
        return Stall.objects.filter(owner=self.request.user)

    def create(self, request):
        data = request.data
        user = request.user

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        brand = validated_data.get("brand")

        existing_brand = Stall.objects.filter(brand__iexact=brand)

        if existing_brand:
            return Response(
                {"message": "A stall with the same brand already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        validated_data["owner"] = user

        created_stall = Stall.objects.create(**validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
