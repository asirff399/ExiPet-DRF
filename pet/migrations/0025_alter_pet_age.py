# Generated by Django 5.1 on 2024-10-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0024_alter_adoption_balance_after_adoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
