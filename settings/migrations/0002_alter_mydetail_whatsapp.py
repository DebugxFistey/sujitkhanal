# Generated by Django 3.2.13 on 2023-02-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydetail',
            name='whatsapp',
            field=models.CharField(default='+9779842765535', max_length=100),
        ),
    ]
