from rest_framework import routers
from .viewsets import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

app_name = 'library'

urlpatterns = router.urls