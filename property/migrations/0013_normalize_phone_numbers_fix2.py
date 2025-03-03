# Generated by Django 4.2.17 on 2025-01-10 22:49

from django.db import migrations
import phonenumbers
from phonenumbers import PhoneNumberFormat


def normalize_phone_numbers(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all().iterator():
        try:
            parsed_number = phonenumbers.parse(flat.owners_phonenumber, "RU")

            if not phonenumbers.is_valid_number(parsed_number):
                flat.owner_pure_phone = None
                flat.save()
                continue

            normalized_phone_number = phonenumbers.format_number(
                parsed_number, PhoneNumberFormat.E164
            )
            flat.owner_pure_phone = normalized_phone_number
            flat.save()

        except phonenumbers.phonenumberutil.NumberParseException:
            flat.owner_pure_phone = None
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone_alter_complaint_id_and_more'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
