# Generated by Django 3.2.6 on 2021-08-06 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0009_systemapp_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemapp',
            name='uuid',
        ),
    ]