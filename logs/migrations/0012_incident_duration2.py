# Generated by Django 3.2.6 on 2021-08-06 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0011_incident_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='duration2',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
