import jwt
from django.db import models
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from profilecourses.manager import ProfileUserManager


class ProfileUser(AbstractBaseUser, PermissionsMixin):
    """
    Пользовательский класс.
    """
    username = models.CharField(db_index=True, max_length=255, unique=True, verbose_name="Логин")

    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False,
                              verbose_name="Электронная почта")
    is_staff = models.BooleanField(default=False, verbose_name="Права доступа")
    is_active = models.BooleanField(default=True, verbose_name="Статусактивности")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    rated = models.BooleanField(default=False, editable=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username', )

    objects = ProfileUserManager()

    def __str__(self):
        """
        Возвращение строкового представления ProfileUser
        """

        return self.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        db_table = 'profile'
        ordering = ('-created_at', '-updated_at',)

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.username

    def has_perm(self, perm, obj=None):
        # получение прав для входа в админ панель
        return True

    def has_module_perms(self, app_label):
        # получение прав для входа в админ панель
        return True

