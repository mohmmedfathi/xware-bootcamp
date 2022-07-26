from dataclasses import fields
from email.mime import image
from pyexpat import model
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Create_Student(forms.Form):
    username = forms.CharField(max_length=100,min_length=1)
    email = forms.CharField(max_length=100,min_length=1)
    
    password = forms.CharField(max_length=100,min_length=5)



class Create_User_Model_Form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['password'] = make_password(
            cleaned_data['password']
        )
        return cleaned_data
        