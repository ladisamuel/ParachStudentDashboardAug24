from django.urls import path, include
from . import *

urlpatterns = [
    path('', include('CRM.adminUrls'))
]
