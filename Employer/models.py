from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Talent Categories


class OnlineTalentCategories(models.Model):
    category = models.CharField(max_length=150)
    

    def __str__(self):
        return self.category
    

class OfflineTalentCategories(models.Model):
    category = models.CharField(max_length=150)
    VEHICLE_OPTIONS = (
        ('with vehicle', 'with vehicle'),
        ('without vehicle', 'without vehicle'),
    )
    vehicle_option = models.CharField(max_length=20, choices=VEHICLE_OPTIONS,default='without vehicle')
    
    def __str__(self):
        return self.category


class CompanyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255,null=True, blank=True)
    company_info = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    employer_address = models.TextField()
    street_address = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    postal_code = models.CharField(max_length=10,null=True, blank=True)
    country = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class OnlineJobInformation(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    category = models.ForeignKey(OnlineTalentCategories, on_delete=models.CASCADE)
    age_requirement_min = models.PositiveIntegerField()
    age_requirement_max = models.PositiveIntegerField()
    preferred_academic_courses = models.TextField()
    pay_structure = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.job_title


class OfflineJobInformation(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    category = models.ForeignKey(OfflineTalentCategories, on_delete=models.CASCADE)
    work_address = models.TextField()
    age_requirement_min = models.PositiveIntegerField()
    age_requirement_max = models.PositiveIntegerField()
    preferred_academic_courses = models.TextField()
    pay_structure = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    job_location_map = models.URLField()
    
    def __str__(self):
        return self.job_title