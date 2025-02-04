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
router.register(r'employee-education', EmployeeEducationViewSet)
router.register(r'employee-languages', EmployeeLanguagesViewSet)
router.register(r'employee-technical-skills', EmployeeTechnicalSkillsViewSet)
router.register(r'employee-soft-skills', EmployeeSoftSkillsViewSet)
router.register(r'employee-work-preferences', EmployeeWorkPreferencesViewSet)


urlpatterns = [
    path('form-model/', EmployeeFormModelsAPIView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('employee-field-of-study/', FieldOfStudyApiView.as_view()),
    path('employee-preferred-job-category/', EmployeePreferredJobCategoryAPIView.as_view()),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/google-auth/', GoogleAuthView.as_view(), name='google-auth'),
    
    path('',include(router.urls)),

]

