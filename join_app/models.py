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
    phone = models.IntegerField()
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name} ({self.pk})"
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=30, choices=CATEGORY, default='user_story')
    date = models.DateField()
    prio = models.CharField(max_length=30, choices=PRIO, default='medium')
    status = models.CharField(max_length=30, choices=STATUS, default='todo')
    asignt_to = models.ManyToManyField(Contact, related_name="tasks")

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=255)
    checked = models.BooleanField()
    task = models.ForeignKey(Task, related_name="subTasks", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    