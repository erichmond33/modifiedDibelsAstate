# Generated by Django 4.0.3 on 2022-03-26 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dibels_test', '0020_alter_queuedmazequestion_font'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuedmazequestion',
            name='font',
            field=models.ForeignKey(default=160, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font'),
        ),
    ]
