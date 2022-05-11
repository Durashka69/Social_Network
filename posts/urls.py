from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls))
]
