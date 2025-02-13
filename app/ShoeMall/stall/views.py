from rest_framework import viewsets
from .models import Stall
from .serializers import StallSerializer

class StallViewSet(viewsets.ModelViewSet):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


