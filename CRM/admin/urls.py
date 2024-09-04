from django.urls import path
from . import views
urlpatterns = [
    path('', views.adminHomeView, name=adminHomeUrl),
]
