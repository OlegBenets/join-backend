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
        
    def get_checked(self, obj):
        return "checked" if obj.checked == "checked" else "unchecked"

    def to_internal_value(self, data):
        if isinstance(data.get("checked"), bool):
            data["checked"] = "checked" if data["checked"] else "unchecked"
        elif data.get("checked") in ["True", "False"]: 
            data["checked"] = "checked" if data["checked"] == "True" else "unchecked"
        
        return super().to_internal_value(data)

class TaskSerializer(serializers.ModelSerializer):
    sub_tasks = SubTaskSerializer(many=True, required=False) 
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)  # Direkt als Liste von IDs

    class Meta:
        model = Task
        fields = ["id", "title", "description", "category", "date", "prio", "status", "assigned_to", "sub_tasks"]

    def create(self, validated_data):
        sub_tasks_data = validated_data.pop("sub_tasks", [])
        assigned_contacts = validated_data.pop("assigned_to", [])  # IDs werden direkt erwartet

        task = Task.objects.create(**validated_data)
        task.assigned_to.set(assigned_contacts)

        for sub_task_data in sub_tasks_data:
            SubTask.objects.create(task=task, **sub_task_data)

        return task

    def update(self, instance, validated_data):
        sub_tasks_data = validated_data.pop("sub_tasks", [])
        assigned_contacts = validated_data.pop("assigned_to", [])  

        instance = super().update(instance, validated_data)
        instance.assigned_to.set(assigned_contacts)  

        instance.sub_tasks.all().delete()
        for sub_task_data in sub_tasks_data:
            SubTask.objects.create(task=instance, **sub_task_data)

        return instance