from django.contrib.auth.models import BaseUserManager


class ProfileUserManager(BaseUserManager):

    """
    Собственный класс Manager. Используется при создании пользователей.
    """

    def _create_user(self, username, email, password=None, **extra_fields):

        if not username:
            raise ValueError("Для регистрации профиля требуется указать логин")
        if not email:
            raise ValueError("Для регистрации профиля нужна почта для его подтверждения")
        if not password:
            raise ValueError("Для защиты профиля он должен иметь пароль")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
