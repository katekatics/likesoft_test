from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """Получение списка книг"""
    def list(self, request, *args, **kwargs) -> Response:
        serializer = super(BookViewSet, self).list(request)
        return Response({'books': serializer.data})

    """Получение детальной информации о книге"""
    def retrieve(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

    """Добавление новой книги"""
    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """Обновление информации о книге"""
    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializer.data)

    """Удаление книги"""
    def destroy(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)
