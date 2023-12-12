from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    completed = serializers.BooleanField()


    def create(self, validated_data):
        return Task.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get('id')
        print("instance",instance.id)
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.completed = validated_data.get('completed')
        instance.save()
        return instance