# Generated by Django 2.2.24 on 2025-01-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_update_new_building_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, default=None, verbose_name='Новостройка'),
        ),
    ]
