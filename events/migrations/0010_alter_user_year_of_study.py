# Generated by Django 4.0.3 on 2023-02-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_user_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year_of_study',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
