from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

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
        user, created = User.objects.get_or_create(email=email, defaults={'username': username}, is_staff=True)

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
        


class EmployerViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)