# Generated by Django 3.2.13 on 2023-02-22 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_assignment_date_up_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Working On', 'Working On'), ('Delivered', 'Delivered')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='date_up_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 16, 46, 47, 130045, tzinfo=utc)),
        ),
    ]
