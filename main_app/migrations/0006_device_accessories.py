# Generated by Django 4.2.4 on 2023-08-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_accessory'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='accessories',
            field=models.ManyToManyField(to='main_app.accessory'),
        ),
    ]