# Generated by Django 5.0 on 2025-01-25 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_employee_country_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeworkpreferences',
            name='preferred_job_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.jobcategories'),
        ),
    ]
