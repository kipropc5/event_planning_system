# Generated by Django 5.0.2 on 2024-11-22 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_alter_event_end_time_alter_event_event_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='event_name',
            new_name='participant_event_name',
        ),
    ]
