# Generated by Django 5.0 on 2025-02-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0022_remove_offlinejobinformation_posted_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offlinejobinformation',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='onlinejobinformation',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
