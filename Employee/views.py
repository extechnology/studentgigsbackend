from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class EmployeeFormModelsAPIView(APIView):
    def get(self, request):
        employee_fields = []
        language_fields = []
        technical_skill_field = []
        soft_skills_field = []
        education_fields = []
        achievements_fields = []
        certifications_fields = []
        work_preferences_fields = []
        experience_fields = []
        
        field_type_mapping = {
            'CharField': 'text',
            'IntegerField': 'number',
            'FloatField': 'number',
            'DateField': 'date',
            'DateTimeField': 'datetime-local',
            'EmailField': 'email',
            'BooleanField': 'checkbox',
            'TextField': 'textarea'
        }
        
        def map_field_type(field):
            field_type = field.get_internal_type()
            return field_type_mapping.get(field_type, 'text') 

        
        def is_field_required(field):
            if hasattr(field, 'blank'):
                return not field.blank
            return False  

        for field in Employee._meta.get_fields():
    
            if field.is_relation:
                continue  

            employee_fields.append({
                'name': field.name,
                'type': map_field_type(field),
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
            })
        
        # Get field names and types for EmployeeLanguages model
        for field in EmployeeLanguages._meta.get_fields():
    
            if field.is_relation:
                continue  

            language_fields.append({
                'name': field.name,
                'type': map_field_type(field),
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)
            })
            
        for field in EmployeeTechnicalSkills._meta.get_fields():
    
            if field.is_relation:
                continue  

            technical_skill_field.append({
                'name': field.name,
                'type': map_field_type(field),
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
            
        for field in EmployeeSoftSkills._meta.get_fields():
    
            if field.is_relation:
                continue  

            soft_skills_field.append({
                'name': field.name,
                'type': map_field_type(field),
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
        
        for field in EmployeeEducation._meta.get_fields():
    
            if field.is_relation:
                continue  

            education_fields.append({
                'name': field.name,
                'type': map_field_type(field),
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
            
        for field in EmployeeEducationAchievements._meta.get_fields():
    
            if field.is_relation:
                continue  

            achievements_fields.append({
                'name': field.name,
                'type': map_field_type(field),
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
            
        for field in EmployeeCertifications._meta.get_fields():
    
            if field.is_relation:
                continue  

            certifications_fields.append({
                'name': field.name,
                'type': map_field_type(field),  
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
        
        for field in EmployeeWorkPreferences._meta.get_fields():
    
            if field.is_relation:
                continue  

            work_preferences_fields.append({
                'name': field.name,
                'type': map_field_type(field),  
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
            
        for field in EmployeeExperience._meta.get_fields():
    
            if field.is_relation:
                continue  

            experience_fields.append({
                'name': field.name,
                'type': map_field_type(field),  
                'required': is_field_required(field),
                'choices': getattr(field, 'choices', None)  
                
            })
            
        return Response({
            'employee_fields': employee_fields,
            'language_fields': language_fields,
            'technical_skill_field': technical_skill_field,
            'soft_skills_field': soft_skills_field,
            'education_fields': education_fields,
            'achievements_fields': achievements_fields,
            'certifications_fields': certifications_fields,
            'work_preferences_fields': work_preferences_fields,
            'experience_fields': experience_fields,  
        })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer