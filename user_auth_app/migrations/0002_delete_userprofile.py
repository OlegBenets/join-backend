# Generated by Django 5.1.4 on 2025-01-14 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0009_alter_contact_color_alter_contact_phone_and_more'),
        ('user_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
