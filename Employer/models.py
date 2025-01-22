from django.db import models

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
    company_name = models.CharField(max_length=255)
    company_info = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    employer_address = models.TextField()

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