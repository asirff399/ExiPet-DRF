# Generated by Django 5.1 on 2024-10-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_customer_address_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.CharField(default='https://i.ibb.co.com/80NSbds/dummy-profile.png', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='+880', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=10),
        ),
    ]
