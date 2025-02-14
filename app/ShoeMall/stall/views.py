from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Stall
from .serializers import StallSerializer

class StallViewSet(viewsets.ModelViewSet):
    queryset = Stall.objects.none()
    serializer_class = StallSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Stall.objects.all()
        return Stall.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

