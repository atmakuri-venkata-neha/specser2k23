# Generated by Django 4.0.3 on 2023-03-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_alter_user_events_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrations',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrations',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrations',
            name='transaction_id',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrations',
            name='user_phone',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
