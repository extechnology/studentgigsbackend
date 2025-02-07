from django.contrib import admin

# Register your models here.

from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','city','state','country']
    search_fields = ['name','email','phone','city','state','country']
    list_filter = ['city','state','country']
    class Meta:
        model = Employee

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(FieldOfStudy)
admin.site.register(EmployeeWorkPreferences)
admin.site.register(JobCategories)
admin.site.register(EmployeeProfile)
admin.site.register(EmployeeAdditionalInformation)
admin.site.register(EmployeeEducation)

admin.site.register(EmployeeCertifications)
admin.site.register(EmployeeLanguages)
admin.site.register(EmployeeTechnicalSkills)
admin.site.register(EmployeePreferredJobCategory)
admin.site.register(EmployeeExperience)
