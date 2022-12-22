from django.contrib import admin

from apps.todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Todo, TodoAdmin)
