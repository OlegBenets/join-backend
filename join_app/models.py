from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("user_story", "User Story"),
    ("technical_task", "Technical Task")
)

PRIO = (
    ("urgent", "Urgent"),
    ("medium", "Medium"),
    ("low", "Low"),
)

STATUS = (
    ('todo', 'Todo'),
    ('in_progress', 'In progress'),
    ('await_feedback', 'Await feedback'),
    ('done', 'Done'),
)

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contacts', null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=8)
    
    def __str__(self):
        return f"{self.name} ({self.pk})"
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=30, choices=CATEGORY, default='user_story')
    date = models.DateField()
    prio = models.CharField(max_length=30, choices=PRIO, default='medium')
    status = models.CharField(max_length=30, choices=STATUS, default='todo')
    assigned_to = models.ManyToManyField(Contact, related_name="tasks")

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name="sub_tasks", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    