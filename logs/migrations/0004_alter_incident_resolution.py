# Generated by Django 3.2.6 on 2021-08-06 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_remove_incident_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='resolution',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]