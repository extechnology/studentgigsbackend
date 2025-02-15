from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from Employee.models import Employee

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
    # employer_address = models.TextField(null=True, blank=True)
    street_address = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    postal_code = models.CharField(max_length=10,null=True, blank=True)
    country = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class OnlineJobInformation(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE,related_name='online_job_information',verbose_name='Company',blank=True)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    category = models.CharField(max_length=255)
    age_requirement_min = models.PositiveIntegerField()
    age_requirement_max = models.PositiveIntegerField()
    preferred_academic_courses = models.TextField()
    pay_structure = models.CharField(max_length=255)
    salary_type = models.CharField(max_length=255,null=True, blank=True)
    job_location = models.CharField(max_length=255,null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    job_type = models.CharField(max_length=255,default='online')
    
    def __str__(self):
        return f"{self.company.company_name} - {self.job_title}"

class OfflineJobInformation(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE,related_name='offline_job_information',verbose_name='Company',blank=True)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    category = models.CharField(max_length=255,null=True, blank=True)
    age_requirement_min = models.PositiveIntegerField()
    age_requirement_max = models.PositiveIntegerField()
    preferred_academic_courses = models.TextField()
    pay_structure = models.CharField(max_length=255)
    job_location_map = models.URLField()
    street_address = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    postal_code = models.CharField(max_length=10,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    job_type = models.CharField(max_length=255,default='offline')
    
    
    def __str__(self):
        return self.job_title
    

class EmployerSlider(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    

    def __str__(self):
        return self.title


class EmployerJobApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='job_applications',verbose_name='Employee',blank=True)
    online_job = models.ForeignKey(OnlineJobInformation, on_delete=models.CASCADE,related_name='job_applications',verbose_name='Online Job',blank=True)
    offline_job = models.ForeignKey(OfflineJobInformation, on_delete=models.CASCADE,related_name='job_applications',verbose_name='Offline Job',blank=True)
    date_applied = models.DateField(auto_now_add=True,null=True, blank=True)
    resume = models.FileField(upload_to='job-application-resumes/',null=True, blank=True)
    
    def __str__(self):
        return f"{self.employee.name} - {self.online_job.job_title}"
    