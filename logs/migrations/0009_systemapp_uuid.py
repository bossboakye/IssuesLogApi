# Generated by Django 3.2.6 on 2021-08-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0008_auto_20210806_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemapp',
            name='uuid',
            field=models.TextField(default=True),
        ),
    ]
