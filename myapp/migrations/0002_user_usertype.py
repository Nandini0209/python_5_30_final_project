# Generated by Django 5.0.6 on 2024-06-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Usertype',
            field=models.CharField(default='buyer', max_length=100),
        ),
    ]
