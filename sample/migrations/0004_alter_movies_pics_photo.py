# Generated by Django 4.2.11 on 2024-05-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_alter_movies_pics_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_pics',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]