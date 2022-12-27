from django.db import models

from apps.users.models import User


class Todo(models.Model):
    """
    Model for todo list
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
        verbose_name='owner',
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='title'
    )
    description = models.TextField(
        verbose_name='description'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='is comleted'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )
    image = models.ImageField(
        upload_to='todo_images/',
        verbose_name='image',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'Todos'
