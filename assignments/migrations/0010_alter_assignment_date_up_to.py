# Generated by Django 3.2.13 on 2023-02-22 18:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0009_alter_assignment_date_up_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date_up_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 18, 13, 10, 546263, tzinfo=utc)),
        ),
    ]
