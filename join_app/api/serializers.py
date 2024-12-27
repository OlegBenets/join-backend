from rest_framework import serializers
from join_app.models import Contact, Task

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    phone = serializers.IntegerField()
    color = serializers.CharField(max_length=30)
    
    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
    

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.BooleanField()
    date = serializers.DateField()
    description = serializers.CharField(max_length=300)
    prio = serializers.CharField(max_length=360)
    status = serializers.CharField(max_length=360)
    title = serializers.CharField(max_length=100)
    asignt_to = serializers.IntegerField()
    sub_task = serializers.IntegerField()
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    