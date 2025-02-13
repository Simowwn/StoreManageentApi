from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not password:
            return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)

        user = Users(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()

        return Response({"id": user.id, "email": user.email}, status=status.HTTP_201_CREATED)


