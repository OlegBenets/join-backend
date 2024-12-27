from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    color = models.CharField(max_length=30)
    
class Task(models.Model):
    category = models.BooleanField()
    date = models.DateField()
    description = models.CharField(max_length=300)
    prio = models.CharField(max_length=360)
    status = models.CharField(max_length=360)
    title = models.CharField(max_length=100)
    asignt_to = models.IntegerField()
    sub_task = models.IntegerField()
    