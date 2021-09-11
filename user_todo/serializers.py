from rest_framework import serializers

import datetime

from .models import Todo, Like


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['pk', 'title', 'body']

    def create(self, validated_data):
        todo = Todo.objects.create(
            user=self.context['request']._user,
            title=validated_data['title'],
            body=validated_data['body'],
            date_created=datetime.datetime.now()
        )

        return todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
