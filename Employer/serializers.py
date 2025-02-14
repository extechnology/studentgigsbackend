from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EmployerRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        email = validated_data['email']
        
        if User.objects.filter(email=email).exists():
            # **Raise** the error instead of returning it
            raise serializers.ValidationError({'email': 'Email already exists.'})
        
        user = User(
            email=email,
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class OnlineTalentCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineTalentCategories
        fields = '__all__'

class OfflineTalentCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineTalentCategories
        fields = '__all__'

class EmployerInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class OnlineJobInformationSerializer(serializers.ModelSerializer):
    company = EmployerInfoSerializer(read_only=True)
    class Meta:
        model = OnlineJobInformation
        fields = '__all__'
        
    def create(self, validated_data):
        employer = CompanyInfo.objects.get(user=self.context['request'].user)
        return OnlineJobInformation.objects.create(**validated_data, company=employer)


    
class OfflineJobInformationSerializer(serializers.ModelSerializer):
    company = EmployerInfoSerializer(read_only=True)
    class Meta:
        model = OfflineJobInformation
        fields = '__all__'
        
    def create(self, validated_data):
        employer = CompanyInfo.objects.get(user=self.context['request'].user)
        return OfflineJobInformation.objects.create(**validated_data, company=employer)
        

