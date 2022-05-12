from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, PostViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'likes', LikeViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls))
]
