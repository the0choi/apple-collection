# Generated by Django 4.2.4 on 2023-08-14 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='latest_model',
        ),
        migrations.AddField(
            model_name='device',
            name='colours',
            field=models.CharField(default='white', max_length=100),
            preserve_default=False,
        ),
    ]
