# Generated by Django 3.2.9 on 2022-01-19 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dibels_test', '0003_auto_20220114_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mazetest',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
