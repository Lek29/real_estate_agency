# Generated by Django 4.2.17 on 2025-01-12 08:52

from django.db import migrations


def transfer_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            defaults={
                'phonenumbers': flat.owners_phonenumber,
                'pure_phone': flat.owner_pure_phone,
            }
        )
        
        owner.flat.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20250112_0605'),
    ]

    operations = [
        migrations.RunPython(transfer_owners),
    ]
