from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .viewsets import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

app_name = 'library'

urlpatterns = [
    path('api', include(router.urls), name='api'),
]
