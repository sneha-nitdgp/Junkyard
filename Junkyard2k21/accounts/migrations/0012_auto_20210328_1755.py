# Generated by Django 3.1.7 on 2021-03-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210324_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(max_length=120),
        ),
    ]
