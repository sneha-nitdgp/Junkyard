# Generated by Django 3.1.6 on 2021-03-23 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0009_auto_20210324_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='profile',
        ),
    ]
