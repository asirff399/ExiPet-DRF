# Generated by Django 5.1 on 2024-10-28 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_alter_deposite_transaction_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdraw',
            name='user',
        ),
        migrations.DeleteModel(
            name='Deposite',
        ),
        migrations.DeleteModel(
            name='Withdraw',
        ),
    ]
