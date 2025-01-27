from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from .views import *

router = routers.DefaultRouter()


urlpatterns = [
    
    path('',include(router.urls)),
   
]

