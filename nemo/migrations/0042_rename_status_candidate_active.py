# Generated by Django 4.2 on 2023-06-02 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0041_rename_group_candidate_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='status',
            new_name='active',
        ),
    ]
