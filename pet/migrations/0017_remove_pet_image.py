# Generated by Django 5.1 on 2024-08-23 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0016_pet_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image',
        ),
    ]
