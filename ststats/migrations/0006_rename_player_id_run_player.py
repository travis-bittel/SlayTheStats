# Generated by Django 3.2.25 on 2024-05-31 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ststats', '0005_rename_player_run_player_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='player_id',
            new_name='player',
        ),
    ]