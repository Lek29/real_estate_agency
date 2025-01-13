# Generated by Django 4.2.17 on 2025-01-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_alter_flat_options_alter_owner_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.AddField(
            model_name='flat',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='flats', to='property.owner', verbose_name='Собственники'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(blank=True, related_name='owned_by', to='property.flat', verbose_name='Квартиры в собственности'),
        ),
    ]
