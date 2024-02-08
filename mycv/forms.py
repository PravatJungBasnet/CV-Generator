from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class generate(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields='__all__'
        

class Signup(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields={'username','email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        


        