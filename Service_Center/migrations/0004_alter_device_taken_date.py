# Generated by Django 4.0 on 2023-06-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service_Center', '0003_alter_device_service_center_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='taken_date',
            field=models.TextField(default=''),
        ),
    ]
