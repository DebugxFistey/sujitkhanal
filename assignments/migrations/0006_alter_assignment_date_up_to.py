# Generated by Django 3.2.13 on 2023-02-22 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_alter_assignment_date_up_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date_up_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 17, 44, 58, 212098, tzinfo=utc)),
        ),
    ]
