# Generated by Django 4.0 on 2023-06-29 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service_Center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_center',
            name='devices',
            field=models.ManyToManyField(to='Service_Center.Device'),
        ),
    ]
