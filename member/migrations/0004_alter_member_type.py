# Generated by Django 5.1 on 2024-10-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='type',
            field=models.CharField(choices=[('PET SITTER', 'PET SITTER'), ('PET GROMMER', 'PET GROMMER'), ('PET DOCTOR', 'PET DOCTOR'), ('PET MANAGER', 'PET MANAGER')], max_length=30),
        ),
    ]