from django.db import models


class Todo(models.Model):
    """
    Model for todo list
    """
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
        verbose_name='image'
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'Todos'
