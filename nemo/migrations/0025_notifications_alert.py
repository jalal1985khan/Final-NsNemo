# Generated by Django 4.2 on 2023-05-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0024_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='alert',
            field=models.CharField(max_length=200, null=True),
        ),
    ]