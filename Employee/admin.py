from django.contrib import admin

# Register your models here.

from .models import *

class LanguageInline(admin.StackedInline):
    model = EmployeeLanguages
    extra = 1
class TechnicalSkillInline(admin.StackedInline):
    model = EmployeeTechnicalSkills
    extra = 1
class SoftSkillInline(admin.StackedInline):
    model = EmployeeSoftSkills
    extra = 1
class EducationInline(admin.StackedInline):
    model = EmployeeEducation
    extra = 1
class AchievementInline(admin.StackedInline):
    model = EmployeeEducationAchievements
    extra = 1

class CertificationInline(admin.StackedInline):
    model = EmployeeCertifications
    extra = 1

class WorkPreferenceInline(admin.StackedInline):
    model = EmployeeWorkPreferences
    extra = 1

class ExperienceInline(admin.StackedInline):
    model = EmployeeExperience
    extra = 1
class preferredJobCategoryInline(admin.StackedInline):
    model = EmployeePreferredJobCategory
    extra = 1

class ExperienceInline(admin.StackedInline):
    model = EmployeeExperience
    extra = 1

class AdditionalInfoInline(admin.StackedInline):
    model = EmployeeAdditionalInformation
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [LanguageInline,TechnicalSkillInline,SoftSkillInline,EducationInline,AchievementInline,CertificationInline,WorkPreferenceInline,ExperienceInline,preferredJobCategoryInline,ExperienceInline,AdditionalInfoInline]
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