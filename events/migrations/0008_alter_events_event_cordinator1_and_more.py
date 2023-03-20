# Generated by Django 4.0.3 on 2023-02-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_events_event_cordinator1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_cordinator1',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_cordinator2',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_cordinator3',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_cordinator4',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_prize_money',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_runner_prize_money',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='team_size',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
