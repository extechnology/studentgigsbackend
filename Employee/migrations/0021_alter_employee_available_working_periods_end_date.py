# Generated by Django 5.0 on 2025-01-30 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0020_alter_employee_available_working_periods_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='available_working_periods_end_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 1, 30), null=True),
        ),
    ]
