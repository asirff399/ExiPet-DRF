# Generated by Django 5.1 on 2024-08-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0009_remove_pet_pet_type_pet_pet_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.ManyToManyField(to='pet.pettype'),
        ),
    ]
