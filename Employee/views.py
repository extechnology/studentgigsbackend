from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class GoogleAuthView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')

        if not username or not email:
            return Response({'error': 'Username and email are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create the user based on the provided email
        user, created = User.objects.get_or_create(email=email, defaults={'username': username})

        # If the user was just created, you can assign the username or handle further logic here
        if created:
            user.username = username
            user.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
        
        
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

        def get_choices(field):
            choices = getattr(field, 'choices', None)
            if choices:
                return [choice[0] for choice in choices]  # Extract only the first element of each tuple
            return None
        def process_model_fields(model, field_list):
            for field in model._meta.get_fields():
                if field.is_relation or field.name == 'id':
                    continue
                field_list.append({
                    'name': field.name,
                    'type': map_field_type(field),
                    'required': is_field_required(field),
                    'choices': get_choices(field)
                })

        process_model_fields(Employee, employee_fields)
        process_model_fields(EmployeeLanguages, language_fields)
        process_model_fields(EmployeeTechnicalSkills, technical_skill_field)
        process_model_fields(EmployeeSoftSkills, soft_skills_field)
        process_model_fields(EmployeeEducation, education_fields)
        process_model_fields(EmployeeEducationAchievements, achievements_fields)
        process_model_fields(EmployeeCertifications, certifications_fields)
        process_model_fields(EmployeeWorkPreferences, work_preferences_fields)
        process_model_fields(EmployeeExperience, experience_fields)
        
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
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)