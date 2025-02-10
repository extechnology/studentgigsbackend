from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()


urlpatterns = [
    
    path('',include(router.urls)),
    
    # Employer Register
    path('register/',EmployerRegisterView.as_view()),
    
    
    
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Google Authentication
    path('api/google-auth/', GoogleAuthView.as_view(), name='google-auth'),
    
   
]

