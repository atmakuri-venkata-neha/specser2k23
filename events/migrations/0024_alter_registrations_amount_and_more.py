# Generated by Django 4.0.3 on 2023-03-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_alter_registrations_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrations',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrations',
            name='user_phone',
            field=models.BigIntegerField(),
        ),
    ]
