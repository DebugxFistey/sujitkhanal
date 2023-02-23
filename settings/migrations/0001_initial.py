# Generated by Django 3.2.13 on 2023-02-22 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('default_price', models.IntegerField()),
                ('urgent_price', models.IntegerField()),
                ('medium_price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('youtube_channel', models.CharField(max_length=255)),
                ('github_url', models.CharField(max_length=100)),
                ('facebook_url', models.CharField(max_length=100)),
                ('whatsapp', models.IntegerField()),
                ('mail', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
