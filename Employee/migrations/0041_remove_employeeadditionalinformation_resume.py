# Generated by Django 5.0 on 2025-02-06 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0040_remove_employeeexperience_exp_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeadditionalinformation',
            name='resume',
        ),
    ]
