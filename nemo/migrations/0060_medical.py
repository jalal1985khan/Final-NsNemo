# Generated by Django 4.2 on 2023-06-05 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0059_alter_crewplanner_crew_vessel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
                ('expiry_date', models.CharField(max_length=200, null=True)),
                ('done_by', models.CharField(choices=[('OFFICE', 'OFFICE'), ('AGENT', 'AGENT'), ('SELF', 'SELF')], max_length=200, null=True)),
                ('status', models.CharField(choices=[('FIT', 'FIT'), ('UNFIT', 'UNFIT')], max_length=200, null=True)),
                ('amount', models.CharField(max_length=200, null=True)),
                ('upload', models.FileField(blank=True, null=True, upload_to='medicals')),
                ('hospital_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nemo.hospital')),
            ],
        ),
    ]
