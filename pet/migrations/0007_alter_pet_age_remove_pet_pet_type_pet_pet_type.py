# Generated by Django 5.1 on 2024-08-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_pet_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.RemoveField(
            model_name='pet',
            name='pet_type',
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_type',
            field=models.ManyToManyField(to='pet.pettype'),
        ),
    ]
