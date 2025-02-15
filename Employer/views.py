from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from itertools import chain

class EmployerRegisterView(APIView):
    def post(self, request):
        serializer = EmployerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
        



class TalentCategoriesApiView(APIView):
    def get(self, request):
        categories = OnlineTalentCategories.objects.all()
        serializer = OnlineTalentCategoriesSerializer(categories, many=True)
        
        offline_categories = OfflineTalentCategories.objects.all()
        
        offline_serializer = OfflineTalentCategoriesSerializer(offline_categories, many=True)
        
        online = []
        offline = []
        
        for category in serializer.data:
            online.append({
                'label': category['category'],
                'value': category['category']
            })
        
        for category in offline_serializer.data:
            offline.append({
                'label': category['category'],
                'value': category['category'],
                'vehicle_option': category['vehicle_option']
            })
        
        return Response(
            {
                'online': online,
                'offline': offline
            }
        )

class EmployerInfoViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = EmployerInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)  # ✅ Correct way to filter by user
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        employer_instance, created = CompanyInfo.objects.get_or_create(user=request.user)

        # Check if the required fields have values
        is_exist = bool(
            employer_instance.company_name and employer_instance.phone_number and employer_instance.email
            and employer_instance.street_address and employer_instance.city and employer_instance.state
            and employer_instance.postal_code and employer_instance.country
        )

        data = {
            'is_exist': is_exist,
            'employer': self.serializer_class(employer_instance, context={'request': request}).data  # Added request context
        }

        return Response(data, status=status.HTTP_200_OK)

    
    def put(self, request, *args, **kwargs):
        id = request.query_params.get('pk')
        employer = CompanyInfo.objects.get(id=id)
        serializer = EmployerInfoSerializer(employer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OnlineJobInformationViewSet(viewsets.ModelViewSet):
    queryset = OnlineJobInformation.objects.all()
    serializer_class = OnlineJobInformationSerializer
    permission_classes = [IsAuthenticated]


class OfflineJobInformationViewSet(viewsets.ModelViewSet):
    queryset = OfflineJobInformation.objects.all()
    serializer_class = OfflineJobInformationSerializer
    permission_classes = [IsAuthenticated]
    

class JobsApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        online_jobs_instance  = OnlineJobInformation.objects.filter(company__user=request.user)
        offline_jobs_instance = OfflineJobInformation.objects.filter(company__user=request.user)
        employer = CompanyInfo.objects.get(user=request.user)
        employer_data = EmployerInfoSerializer(employer).data
        
    
        # Serialize data
        online_jobs_data = OnlineJobInformationSerializer(online_jobs_instance, many=True, context={'request': request}).data
        offline_jobs_data = OfflineJobInformationSerializer(offline_jobs_instance, many=True, context={'request': request}).data

    
        # Merge both lists
        all_jobs = list(chain(online_jobs_data, offline_jobs_data))
    
        return Response({
            "jobs": all_jobs
            })
        
    def delete(self, request, *args, **kwargs):
        id = request.query_params.get('pk')
        job_type = request.query_params.get('type')
        if job_type == 'online':
            job = OnlineJobInformation.objects.get(id=id)
        elif job_type == 'offline':
            job = OfflineJobInformation.objects.get(id=id)
        else:
            return Response({"error": "Invalid job type"}, status=status.HTTP_400_BAD_REQUEST)
        
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployerSliderApiView(APIView):
    def get(self, request):
        sliders = EmployerSlider.objects.all()
        serializer = EmployerSliderSerializer(sliders,context={'request': request}, many=True)
        return Response(serializer.data)
    

class EmployerJobApplicationApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        applications = EmployerJobApplication.objects.filter(employee__user = request.user)
        serializer = EmployerJobApplicationSerializer(applications, many=True)
        return Response(serializer.data)