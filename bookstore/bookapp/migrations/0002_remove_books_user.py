# Generated by Django 4.0.6 on 2022-09-22 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='user',
        ),
    ]
