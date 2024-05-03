# Generated by Django 4.2.11 on 2024-05-03 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0013_producer_movies_list_produced_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_list',
            name='produced_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produced_man', to='sample.producer'),
        ),
    ]