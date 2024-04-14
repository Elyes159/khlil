from rest_framework import serializers

from api_wordpress.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    dueDate = serializers.DateField(source='due_date')

    class Meta:
        model = Todo
        exclude = ['due_date']


