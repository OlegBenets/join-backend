# Generated by Django 5.1.4 on 2024-12-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField(max_length=30)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.BooleanField()),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('prio', models.CharField(max_length=360)),
                ('status', models.CharField(max_length=360)),
                ('title', models.CharField(max_length=100)),
                ('asignt_to', models.IntegerField()),
                ('sub_task', models.IntegerField()),
            ],
        ),
    ]
