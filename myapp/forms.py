from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import widgets


class userloginform(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
  class Meta:
    model = User



class signupform(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'email']
    widgets = {
      'username':forms.TextInput(attrs={'class':'form-control'}),
      'first_name':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
   
    }