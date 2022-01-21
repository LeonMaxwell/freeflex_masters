from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer


class RegisterAPIView(APIView):
    # Регистрация пользователя в системе

    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'token': serializer.data.get('token', None),},
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    # Авторизация пользователя в системе

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(f"{user.username} успешно вошел в систему", status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    """ Выход пользователя из системы """
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)