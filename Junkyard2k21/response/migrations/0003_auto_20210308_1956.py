# Generated by Django 3.1.6 on 2021-03-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0002_auto_20210308_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]