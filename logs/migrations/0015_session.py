# Generated by Django 3.2.6 on 2021-08-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0014_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('payload', models.JSONField(max_length=100)),
            ],
        ),
    ]