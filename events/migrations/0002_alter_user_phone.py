# Generated by Django 4.0.3 on 2023-02-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=None, unique=True),
        ),
    ]
