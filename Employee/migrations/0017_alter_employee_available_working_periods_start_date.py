# Generated by Django 5.0 on 2025-01-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0016_delete_employeepersonalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='available_working_periods_start_date',
            field=models.DateField(blank=True, default='yyyy-mm-dd', null=True),
        ),
    ]
