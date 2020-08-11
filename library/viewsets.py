import django_filters.rest_framework
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from .filters import BookFilter


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = BookFilter
