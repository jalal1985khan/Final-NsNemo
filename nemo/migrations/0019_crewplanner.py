# Generated by Django 4.2 on 2023-05-18 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nemo', '0018_notifications_added_by_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrewPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew_rank', models.CharField(max_length=200, null=True)),
                ('crew_company_name', models.CharField(max_length=200, null=True)),
                ('crew_vessel', models.CharField(max_length=200, null=True)),
                ('crew_vsl_name', models.CharField(max_length=200, null=True)),
                ('crew_trading', models.CharField(max_length=200, null=True)),
                ('crew_wages', models.CharField(max_length=200, null=True)),
                ('crew_doj', models.CharField(max_length=200, null=True)),
                ('crew_immediate', models.CharField(max_length=200, null=True)),
                ('crew_other_info', models.CharField(max_length=200, null=True)),
                ('crew_status', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('crew_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]