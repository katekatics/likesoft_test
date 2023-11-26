from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .tasks import send_hello_email_task


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """Создание нового пользователя"""
    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_hello_email_task.delay(serializer.data['email'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
