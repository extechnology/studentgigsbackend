# Generated by Django 5.0 on 2025-02-11 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0003_remove_offlinejobinformation_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_info', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('employer_address', models.TextField()),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfflineJobInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('work_address', models.TextField()),
                ('age_requirement_min', models.PositiveIntegerField()),
                ('age_requirement_max', models.PositiveIntegerField()),
                ('preferred_academic_courses', models.TextField()),
                ('pay_structure', models.CharField(max_length=255)),
                ('job_location', models.CharField(max_length=255)),
                ('job_location_map', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.offlinetalentcategories')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.companyinfo')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineJobInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('age_requirement_min', models.PositiveIntegerField()),
                ('age_requirement_max', models.PositiveIntegerField()),
                ('preferred_academic_courses', models.TextField()),
                ('pay_structure', models.CharField(max_length=255)),
                ('job_location', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.onlinetalentcategories')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.companyinfo')),
            ],
        ),
    ]
