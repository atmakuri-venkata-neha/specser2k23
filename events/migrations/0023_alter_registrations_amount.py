# Generated by Django 4.0.3 on 2023-03-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_registrations_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrations',
            name='amount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
