# Generated by Django 3.1.6 on 2021-03-23 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0010_remove_response_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='user',
            new_name='teamname',
        ),
    ]
