# Generated by Django 3.2.25 on 2024-05-31 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ststats', '0002_alter_run_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='player_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]