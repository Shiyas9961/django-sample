# Generated by Django 4.2.11 on 2024-05-02 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0005_movies_list_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies_list',
            name='photo',
        ),
    ]
