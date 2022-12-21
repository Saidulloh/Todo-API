from django.db import models
from django.contrib.auth.models import AbstractUser 

from utils.NumberValidator import phone_validator


class User(AbstractUser):
    """
    Model for user
    """
    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='username'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[phone_validator],
        verbose_name='phone_number'
    )
    create_at = models.DateTimeField( 
        auto_now_add=True,
        verbose_name='create_at'
    )
    age = models.IntegerField(
        verbose_name='age'
    )

    def __str__(self):
        return f'{self.id} -- {self.username}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'
