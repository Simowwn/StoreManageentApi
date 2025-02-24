from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    # http_method_names = ["post", "put"]


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")

        for i in first_name:
            if i.isdigit():
                return Response(
                    {"message": "First name should not contain digits."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        for i in last_name:
            if i.isdigit():
                return Response(
                    {"message": "Last name should not contain digits."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if len(password) < 8:
            return Response(
                {"message": "Password should be at least 8 characters long."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        email = validated_data.get("email")
        password = validated_data.get("password")

        user = Users(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        return Response(
            {"id": user.id, "message": f"{user.email} registered successfully."},
            status=status.HTTP_201_CREATED,
        )


class LoginView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        email = validated_data["email"]
        
        try:
            existing_user = Users.objects.get(email=email)

            refresh = RefreshToken.for_user(existing_user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {
                        "id": str(existing_user.id),
                        "email": existing_user.email,
                        "first_name": existing_user.first_name,
                        "last_name": existing_user.last_name,
                        "is_staff": existing_user.is_staff,
                    },
                }
            )
        except Users.DoesNotExist:
            return Response({"message": f"Account {email} does not exists yet."}, status=status.HTTP_200_OK)

