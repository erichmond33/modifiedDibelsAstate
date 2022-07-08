# Generated by Django 4.0.3 on 2022-03-26 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dibels_test', '0021_alter_queuedmazequestion_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagequestionattempt',
            name='font',
            field=models.ForeignKey(default=230, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font'),
        ),
        migrations.CreateModel(
            name='queuedImageQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queuedImageSelection', models.CharField(default='null', max_length=50)),
                ('queuedGeneratedWord1', models.CharField(blank=True, max_length=50)),
                ('queuedGeneratedWord2', models.CharField(blank=True, max_length=50)),
                ('font', models.ForeignKey(default=160, on_delete=django.db.models.deletion.CASCADE, to='dibels_test.font')),
                ('testId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dibels_test.imagetest')),
            ],
        ),
    ]
