from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class JobCategories(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photos/',null=True, blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/',null=True, blank=True)
    job_title = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    preferred_work_location = models.CharField(max_length=100,null=True, blank=True)
    available_work_hours = models.PositiveIntegerField(null=True, blank=True)
    available_working_periods_start_date = models.DateField(null=True, blank=True)
    available_working_periods_end_date = models.DateField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)   
    

    def __str__(self):
        return f'{self.name} - {self.email}'

class EmployeeLanguages(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='languages',verbose_name='Employee')
    language = models.CharField(max_length=100)
    LEVELS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
        ('Native', 'Native')
        )
    level = models.CharField(max_length=20, choices=LEVELS)

class EmployeeTechnicalSkills(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='technical_skills',verbose_name='Employee')
    skill = models.CharField(max_length=100)
    LEVELS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    )
    level = models.CharField(max_length=20, choices=LEVELS)
    description = models.TextField(null=True, blank=True)
    

class EmployeeSoftSkills(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='soft_skills',verbose_name='Employee')
    skill = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class EmployeeEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='educations',verbose_name=Employee)
    current_academic_year = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=100)
    name_of_institution = models.CharField(max_length=200)
    expected_graduation_year = models.CharField(max_length=50)
    
class EmployeeEducationAchievements(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='education_achievements',verbose_name=Employee)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
class EmployeeCertifications(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='certifications',verbose_name=Employee)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='certifications/',null=True, blank=True)
    

class EmployeeWorkPreferences(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='work_preferences',verbose_name=Employee)
    JOB_TYPES = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Both', 'Both')
    )
    interested_job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    # preferred_job_category = models.ForeignKey(JobCategories, on_delete=models.CASCADE, null=True, blank=True)
    expected_salary_range = models.CharField(max_length=100)
    AVAILABILITY_CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Weekend', 'Weekend'),
        ('Flexible', 'Flexible'),
    )
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    TRANSPORT_CHOICES = (
        ('Own vehicle', 'Own vehicle'),
        ('Public transport', 'Public transport'),
        ('Both', 'Both'),
        ('None', 'None')
    )
    transportation_availability = models.CharField(max_length=20, choices=TRANSPORT_CHOICES)

class EmployeePreferredJobCategory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='preferred_job_categories',verbose_name=Employee)
    preferred_job_category = models.CharField(max_length=200)
    
    
class EmployeeExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='experiences',verbose_name=Employee)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
class EmployeeAdditionalInformation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='additional_information',verbose_name=Employee)
    hobbies_or_interests = models.TextField(null=True, blank=True)
    RELOCATE_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    willing_to_relocate = models.CharField(max_length=20, choices=RELOCATE_CHOICES)
    reference_or_testimonials = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/',null=True, blank=True)
    
    
    
