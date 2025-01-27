from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee

@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:  # Only create an Employee profile for new User objects
        Employee.objects.create(user=instance, email=instance.email, name=instance.username)
