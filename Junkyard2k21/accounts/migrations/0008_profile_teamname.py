# Generated by Django 3.1.6 on 2021-03-23 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='teamname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.team'),
        ),
    ]
