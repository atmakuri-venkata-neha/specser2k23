# Generated by Django 4.0.3 on 2023-02-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_events_event_cordinator1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='college',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
