# Generated by Django 3.2.6 on 2021-08-06 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20210806_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='name',
        ),
    ]
