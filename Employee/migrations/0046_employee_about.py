# Generated by Django 5.0 on 2025-02-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0045_employeeprofile_cover_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
