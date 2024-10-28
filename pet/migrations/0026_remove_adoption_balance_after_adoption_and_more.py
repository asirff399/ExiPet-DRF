# Generated by Django 5.1 on 2024-10-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0025_alter_pet_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoption',
            name='balance_after_adoption',
        ),
        migrations.AddField(
            model_name='adoption',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='pet_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]