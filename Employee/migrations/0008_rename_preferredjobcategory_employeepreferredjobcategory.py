# Generated by Django 5.0 on 2025-01-25 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_remove_employeeworkpreferences_preferred_job_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PreferredJobCategory',
            new_name='EmployeePreferredJobCategory',
        ),
    ]
