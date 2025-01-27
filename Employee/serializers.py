from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from Employer.models import OnlineTalentCategories,OfflineTalentCategories

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email','username', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class EmployeeLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLanguages
        fields = '__all__'


class EmployeeTechnicalSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTechnicalSkills
        fields = '__all__'


class EmployeeSoftSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSoftSkills
        fields = '__all__'  
        
class EmployeeEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEducation
        fields = '__all__'
        

class EmployeeEducationAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEducationAchievements
        fields = '__all__'
        

class EmployeeCertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCertifications
        fields = '__all__'

class EmployeeWorkPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkPreferences
        fields = '__all__'

class EmployeePreferredJobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePreferredJobCategory
        fields = '__all__'

class EmployeeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeExperience
        fields = '__all__'
     
class EmployeeAdditionalInformationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EmployeeAdditionalInformation
        fields = '__all__'   


class EmployeeSerializer(serializers.ModelSerializer):
    languages = EmployeeLanguagesSerializer(many=True)
    technical_skills = EmployeeTechnicalSkillsSerializer(many=True)
    soft_skills = EmployeeSoftSkillsSerializer(many=True)
    educations= EmployeeEducationSerializer(many=True)
    education_achievements = EmployeeEducationAchievementsSerializer(many=True)
    certifications = EmployeeCertificationsSerializer(many=True)
    work_preferences = EmployeeWorkPreferencesSerializer(many=True)
    experiences = EmployeeExperienceSerializer(many=True)
    additional_information = EmployeeAdditionalInformationSerializer(many=True)
    preferred_job_categories = EmployeePreferredJobCategorySerializer(many=True)
    online_talent_categories = serializers.SerializerMethodField()
    offline_job_categories = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = '__all__'
    
    def get_online_talent_categories(self, obj):
        return OnlineTalentCategories.objects.all().values_list('category', flat=True)

    def get_offline_job_categories(self, obj):
        return OfflineTalentCategories.objects.all().values_list('category', 'vehicle_option',flat=False)

