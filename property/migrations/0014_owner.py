# Generated by Django 4.2.17 on 2025-01-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_normalize_phone_numbers_fix2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumbers', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(related_name='owners', to='property.flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]