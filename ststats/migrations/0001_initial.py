# Generated by Django 3.2.25 on 2024-05-30 21:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
