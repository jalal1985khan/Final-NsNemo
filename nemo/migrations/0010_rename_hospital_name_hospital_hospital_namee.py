# Generated by Django 4.2 on 2023-05-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0009_alter_hospital_hospital_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='hospital_name',
            new_name='hospital_namee',
        ),
    ]
