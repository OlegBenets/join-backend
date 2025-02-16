# Generated by Django 5.1.4 on 2025-02-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0011_remove_task_subtasks_subtask'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='asignt_to',
            new_name='asigned_to',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
