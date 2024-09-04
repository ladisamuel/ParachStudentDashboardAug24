from django.shortcuts import render

# Create your views here.
def generate_certificate_view(r):
    template = 'index.html'
    return render(r, template)