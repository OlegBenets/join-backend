from django.db import models

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
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField(max_length=12)
    color = models.CharField(max_length=30)
    
class Task(models.Model):
    category = models.CharField(max_length=30, choices=CATEGORY)
    date = models.DateField()
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=30, choices=PRIO)
    category = models.CharField(max_length=30, choices=STATUS)
    title = models.CharField(max_length=255)
    asignt_to = models.ForeignKey(Contact, on_delete=models.CASCADE)


class SubTask(models.Model):
    title = models.CharField(max_length=255)
    checked = models.BooleanField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    