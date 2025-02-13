from rest_framework import viewsets
from .models import Stall, Owner
from .serializers import StallSerializer, OwnerSerializer

class StallViewSet(viewsets.ModelViewSet):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
