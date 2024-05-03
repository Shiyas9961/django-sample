# Generated by Django 4.2.11 on 2024-05-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0012_movies_list_movie_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_name', models.CharField(max_length=100)),
                ('producer_age', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movies_list',
            name='produced_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sample.producer'),
        ),
    ]
