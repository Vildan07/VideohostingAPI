from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, VideoViewSet, FileViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('video', VideoViewSet)
router.register('file', FileViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
