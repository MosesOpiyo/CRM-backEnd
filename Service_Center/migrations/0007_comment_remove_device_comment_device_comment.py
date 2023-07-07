# Generated by Django 4.0 on 2023-07-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service_Center', '0006_service_center'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='comment',
        ),
        migrations.AddField(
            model_name='device',
            name='comment',
            field=models.ManyToManyField(to='Service_Center.Comment'),
        ),
    ]
