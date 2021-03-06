# Generated by Django 3.1.6 on 2021-03-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210312_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=120, verbose_name='Team Name')),
                ('teamleader', models.CharField(max_length=300)),
                ('member1_phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('member2', models.CharField(max_length=300)),
                ('member2_phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('member3', models.CharField(max_length=300)),
                ('member4', models.CharField(max_length=300)),
                ('member3_phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
            ],
        ),
    ]
