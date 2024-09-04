from django.urls import path
from . import views

urlpatterns = [
    path('generator-certificate', views.generate_certificate_view, name='generate_certificate_url')
]