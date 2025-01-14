from rest_framework import serializers
from join_app.models import Contact, Task, SubTask

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", 'name', 'email', 'phone', 'color']
        
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'checked']

class TaskSerializer(serializers.ModelSerializer):
    sub_tasks = SubTaskSerializer(many=True)
    asignt_to = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'date', 'prio', 'status', 'asignt_to', 'sub_tasks']
        
