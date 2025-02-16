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
    sub_tasks = SubTaskSerializer(many=True, required=False) 
    assigned_to = ContactSerializer(many=True, read_only=True, required=False)  
    assigned_to_ids = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True, write_only=True, required=False)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "category", "date", "prio", "status", "assigned_to", "assigned_to_ids", "sub_tasks"]

    def create(self, validated_data):
        sub_tasks_data = validated_data.pop("sub_tasks", [])
        assigned_contacts = validated_data.pop("assigned_to_ids", [])

        task = Task.objects.create(**validated_data)
        task.assigned_to.set(assigned_contacts)

        for sub_task_data in sub_tasks_data:
            SubTask.objects.create(task=task, **sub_task_data)

        return task

    def update(self, instance, validated_data):
        sub_tasks_data = validated_data.pop("sub_tasks", [])
        assigned_contacts = validated_data.pop("assigned_to_ids", [])

        instance = super().update(instance, validated_data)
        instance.assigned_to.set(assigned_contacts) 
        
        instance.sub_tasks.all().delete()  
        for sub_task_data in sub_tasks_data:
            SubTask.objects.create(task=instance, **sub_task_data)

        return instance