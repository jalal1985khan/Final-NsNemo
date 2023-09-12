# Generated by Django 4.2 on 2023-06-20 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nemo', '0072_contract_sign_off_port_alter_contract_sign_on_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('reason', models.CharField(blank=True, max_length=200, null=True)),
                ('reminder_check', models.CharField(blank=True, max_length=200, null=True)),
                ('comment_check', models.CharField(blank=True, max_length=200, null=True)),
                ('reference_check', models.CharField(blank=True, max_length=200, null=True)),
                ('special_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('refernce', models.CharField(blank=True, max_length=200, null=True)),
                ('refernce_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nemo.candidate')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nemo.company')),
            ],
        ),
    ]
