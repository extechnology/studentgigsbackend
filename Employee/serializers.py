from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from Employer.models import OnlineTalentCategories,OfflineTalentCategories
import requests
from django.core.files.base import ContentFile

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
        
    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return EmployeeLanguages.objects.create(**validated_data, employee=employee)


class EmployeeTechnicalSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTechnicalSkills
        fields = '__all__'

    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return EmployeeTechnicalSkills.objects.create(**validated_data, employee=employee)

class EmployeeSoftSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSoftSkills
        fields = '__all__'  
        
    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return EmployeeSoftSkills.objects.create(**validated_data, employee=employee)
    
    
class FieldOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = '__all__'
        
class EmployeeEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEducation
        fields = '__all__'
  
    def create(self, validated_data):
        field_of_studies_data = validated_data.pop('field_of_study')
        
        employee = Employee.objects.get(user=self.context['request'].user)
        
        data = EmployeeEducation.objects.create(**validated_data, field_of_study=field_of_studies_data,employee=employee)
        if FieldOfStudy.objects.filter(name=field_of_studies_data).exists():
            field_of_study_instance = FieldOfStudy.objects.get(name=field_of_studies_data)
        else :
            field_of_study_instance = FieldOfStudy.objects.create(name=field_of_studies_data)
            
        return data

    def update(self, instance, validated_data):
        field_of_studies_data = validated_data.pop('field_of_study')
        instance.field_of_study = field_of_studies_data
        instance.save()
        return instance
    
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
    
    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return EmployeePreferredJobCategory.objects.create(**validated_data, employee=employee)
    
    def get_job_category(self, obj):
        job_categories = JobCategories.objects.all()
        job_category_list = []
        
        for job_category in job_categories:
            job_category_list.append({"value": job_category.name, "label": job_category.name})
    
        return job_category_list

class EmployeeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeExperience
        fields = '__all__'
        
    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return EmployeeExperience.objects.create(**validated_data, employee=employee)
     
class EmployeeAdditionalInformationSerializer(serializers.ModelSerializer): 
    employee_resume = serializers.SerializerMethodField()
    class Meta:
        model = EmployeeAdditionalInformation
        fields = '__all__'   

    def get_employee_resume(self, obj):
        request = self.context.get('request', None)
        if request is None:
            return None  # Avoid KeyError

        user = request.user
        document = EmployeeAdditionalInformation.objects.filter(employee__user=user).first()

        if not document:
            return None  # Return None instead of an empty list for consistency

        protocol = "https" if request.is_secure() else "http"
        current_host = request.get_host()

        def construct_url(field):
            file_field = getattr(document, field, None)
            return f"{protocol}://{current_host}{file_field.url}" if file_field else None

        return construct_url("resume")


    

class EmployeeProfileSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.name', read_only=True)  
    profile_img = serializers.SerializerMethodField()
    cover_img = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeProfile
        fields = '__all__'
        
    def get_profile_img(self, obj):
        request = self.context.get('request', None)
        if request is None:
            return None  # Handle case where request is None

        user = request.user
        profile = EmployeeProfile.objects.filter(employee__user=user).first()
        if profile.profile_pic:
            return request.build_absolute_uri(profile.profile_pic.url)
        return None
    
    def get_cover_img(self, obj):
        request = self.context.get('request', None)
        if request is None:
            return None  # Handle case where request is None

        user = request.user
        profile = EmployeeProfile.objects.filter(employee__user=user).first()
        if profile.cover_photo:
            return request.build_absolute_uri(profile.cover_photo.url)
    #     return None


class EmployeeSerializer(serializers.ModelSerializer):
    profile = EmployeeProfileSerializer()
    languages = EmployeeLanguagesSerializer(many=True)
    technical_skills = EmployeeTechnicalSkillsSerializer(many=True)
    soft_skills = EmployeeSoftSkillsSerializer(many=True)
    educations =  EmployeeEducationSerializer(many=True)
    certifications = EmployeeCertificationsSerializer(many=True)
    work_preferences = EmployeeWorkPreferencesSerializer(many=True)
    preferred_job_categories = EmployeePreferredJobCategorySerializer(many=True)
    experiences = EmployeeExperienceSerializer(many=True)
    additional_information = EmployeeAdditionalInformationSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
    
    def get_online_talent_categories(self, obj):
        return OnlineTalentCategories.objects.all().values_list('category', flat=True)

    def get_offline_job_categories(self, obj):
        return OfflineTalentCategories.objects.all().values_list('category', 'vehicle_option',flat=False)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Replace None values with defaults
        for key, value in data.items():
            if value is None:
                if isinstance(instance._meta.get_field(key), models.CharField):
                    data[key] = ""  # Empty string for CharFields
                elif isinstance(instance._meta.get_field(key), models.IntegerField):
                    data[key] = 0  # Default for IntegerFields
                elif isinstance(instance._meta.get_field(key), models.JSONField):
                    data[key] = {}  # Default for JSONField
                elif isinstance(instance._meta.get_field(key), models.ImageField):
                    data[key] = None  # Keep ImageField as None if no image uploaded
                else:
                    data[key] = None  # Default fallback (optional)

        return data


