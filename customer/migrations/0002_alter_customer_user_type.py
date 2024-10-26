# Generated by Django 5.1 on 2024-08-13 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Customer', 'Customer'), ('Member', 'Member')], default='Customer', max_length=10),
        ),
    ]
