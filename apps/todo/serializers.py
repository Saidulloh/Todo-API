from rest_framework import serializers

from apps.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_field = 'owner'
        fields = (
            'id',
            'title',
            'description',
            'is_completed',
            'image',
            'created_at'
        )
