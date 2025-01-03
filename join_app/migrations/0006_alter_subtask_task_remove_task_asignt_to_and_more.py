# Generated by Django 5.1.4 on 2025-01-03 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0005_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subTasks', to='join_app.task'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='asignt_to',
        ),
        migrations.AddField(
            model_name='task',
            name='asignt_to',
            field=models.ManyToManyField(related_name='tasks', to='join_app.contact'),
        ),
    ]