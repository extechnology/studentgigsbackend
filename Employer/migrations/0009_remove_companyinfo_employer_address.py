# Generated by Django 5.0 on 2025-02-12 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0008_alter_companyinfo_employer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='employer_address',
        ),
    ]
