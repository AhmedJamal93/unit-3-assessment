# Generated by Django 3.1 on 2020-09-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.IntegerField(blank=True),
        ),
    ]
