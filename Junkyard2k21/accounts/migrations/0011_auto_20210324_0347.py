# Generated by Django 3.1.6 on 2021-03-23 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210324_0203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='teamleader',
            new_name='member1',
        ),
    ]