from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('form-model/', EmployeeFormModelsAPIView.as_view()),
    path('user/register/', RegisterView.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/google-auth/', GoogleAuthView.as_view(), name='google-auth'),
]

