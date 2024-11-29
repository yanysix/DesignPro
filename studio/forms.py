from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DesignRequest

class DesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['room_type', 'room_size', 'description', 'style_preferences']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'style_preferences': forms.Textarea(attrs={'rows': 4}),
        }
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
