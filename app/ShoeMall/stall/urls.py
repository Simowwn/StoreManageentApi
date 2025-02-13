from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StallViewSet, OwnerViewSet

router = DefaultRouter()
router.register(r'stalls', StallViewSet)
router.register(r'owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
