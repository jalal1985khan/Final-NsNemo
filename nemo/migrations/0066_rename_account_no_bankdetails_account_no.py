# Generated by Django 4.2 on 2023-06-08 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0065_bankdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankdetails',
            old_name='Account_no',
            new_name='account_no',
        ),
    ]