# Generated by Django 4.1.13 on 2024-01-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(default='75 Days Hard Challenges', max_length=128),
        ),
    ]
