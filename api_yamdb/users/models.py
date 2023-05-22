from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLE_USER = "user"
    USER_ROLE_MODERATOR = "moderator"
    USER_ROLE_ADMIN = "admin"

    Roles = (
        ('Anonym', 'Аноним'),
        ('user', 'Аутентифицированный пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор'),
        ('superuser', 'Суперюзер'),
    )

    first_name = models.CharField(('first name'), max_length=150, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        choices=Roles,
        max_length=30,
        default='user'
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=254,
        unique=True,
    )

    @property
    def is_user(self):
        return self.role == self.USER_ROLE_USER

    @property
    def is_moderator(self):
        return self.role == self.USER_ROLE_MODERATOR

    @property
    def is_admin(self):
        return self.role == self.USER_ROLE_ADMIN

    class Meta:
        ordering = ['id']
