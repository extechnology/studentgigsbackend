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
        # print(employee,self.context['request'].user)
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
        
    # def create(self, validated_data):
    #     employee = Employee.objects.get(user=self.context['request'].user)
    #     return EmployeeWorkPreferences.objects.create(**validated_data, employee=employee)

class EmployeePreferredJobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePreferredJobCategory
        fields = '__all__'
    
    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return EmployeePreferredJobCategory.objects.create(**validated_data, employee=employee)

class EmployeeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeExperience
        fields = '__all__'
     
class EmployeeAdditionalInformationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EmployeeAdditionalInformation
        fields = '__all__'   


class EmployeeSerializer(serializers.ModelSerializer):
    # online_talent_categories = serializers.SerializerMethodField()
    # offline_job_categories = serializers.SerializerMethodField()
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


