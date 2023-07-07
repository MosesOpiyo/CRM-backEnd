# Generated by Django 4.0 on 2023-06-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(default='')),
                ('supplier', models.TextField(default='')),
                ('imei', models.BigIntegerField(default=0)),
                ('picked_at_shop', models.BooleanField(default=False)),
                ('delivered_to_client_by', models.TextField(default='')),
                ('client_name', models.TextField(default='')),
                ('client_phone_number', models.IntegerField(default=0)),
                ('client_email', models.EmailField(default='', max_length=254)),
                ('client_location', models.TextField(default='')),
                ('client_pin', models.TextField(default='')),
                ('sold_by', models.TextField(default='')),
                ('status', models.TextField(default='')),
                ('warranty_status', models.TextField(default='')),
                ('cash', models.IntegerField(default=0)),
                ('mpesa', models.IntegerField(default=0)),
                ('invoiced_amount', models.IntegerField(default=0)),
                ('expense_name', models.TextField(default='')),
                ('expense_amount', models.IntegerField(default=0)),
            ],
        ),
    ]
