from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StallViewSet

router = DefaultRouter()
router.register(r"stalls", StallViewSet, basename="stalls")

urlpatterns = [
    path("", include(router.urls)),
]
