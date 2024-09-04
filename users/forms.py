from django.forms import Form, ModelForm
from .models import *

class CustomUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

