# Generated by Django 4.0 on 2023-06-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service_Center', '0002_alter_service_center_devices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='service_center_feedback',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Service_Feedback',
        ),
    ]
