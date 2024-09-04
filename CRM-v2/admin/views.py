from django.shortcuts import render
from django.http immport HttpResponse
# Create your views here.

def adminHomeView(r):
    return HttpResponse('<h1>Hello World in admin folder</h1>')