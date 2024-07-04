from dataclasses import fields
from multiprocessing import AuthenticationError
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-reg', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-reg', 'placeholder': 'Enter email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-reg', 'placeholder': 'Enter phone'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input-reg', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'input-reg', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-log', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-log', 'placeholder': 'Enter password'}))


class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-profile', 'placeholder': 'Enter username'}))
    avatar = forms.FileField(widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = ['username', 'avatar']