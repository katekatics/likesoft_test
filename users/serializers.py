from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
