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


class JobGeneralInfo(models.Model):
    employer_name = models.CharField(max_length=255)
    job_description = models.TextField()
    logo = models.ImageField(upload_to='employer_logos/', null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    employer_address = models.TextField()

    def __str__(self):
        return self.employer_name

