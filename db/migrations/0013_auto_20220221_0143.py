# Generated by Django 3.2.9 on 2022-02-21 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dibels_test', '0012_queuedmazequestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mazetest',
            name='queuedGeneratedWord1',
        ),
        migrations.RemoveField(
            model_name='mazetest',
            name='queuedGeneratedWord2',
        ),
        migrations.RemoveField(
            model_name='mazetest',
            name='queuedSentenceId',
        ),
        migrations.RemoveField(
            model_name='mazetest',
            name='queuedWordSelection',
        ),
    ]