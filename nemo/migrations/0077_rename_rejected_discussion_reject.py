# Generated by Django 4.2 on 2023-06-20 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0076_remove_discussion_status_discussion_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='rejected',
            new_name='reject',
        ),
    ]
