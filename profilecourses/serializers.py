from django.contrib.auth import authenticate, login
from rest_framework import serializers
from .models import ProfileUser


class RegisterSerializer(serializers.ModelSerializer):
    """
    Класс регистрации нового пользователя. В результате возвращен JSON Web Token
    """

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = ProfileUser
        fields = ('email', 'username', 'password', )

    def create(self, validated_data):
        return ProfileUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """
    Аутентификация существующего пользователя. В результате возвращается JSON Web Token.
    """

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError("Электронный адрес требуется для входа в систему")

        if password is None:
            raise serializers.ValidationError("Пароль требуется для входа в систему")

        user = authenticate(request=self.context.get('request'), username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Пользователя с такой электронной почтой и паролем не найдено")
        if not user.is_active:
            raise serializers.ValidationError("Этот пользователь не активный")

        return {
            'user': user
        }