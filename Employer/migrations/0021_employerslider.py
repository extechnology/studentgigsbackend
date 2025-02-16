# Generated by Django 5.0 on 2025-02-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0020_offlinejobinformation_job_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider_images/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
