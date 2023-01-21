from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy

from donations.models import CustomUser, Donation


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput())

    class Meta:
        fields = ("username", 'password')


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = (
            'quantity', 'categories', 'institution', 'address', 'phone_number', 'city', 'zip_code', 'pick_up_date',
            'pick_up_time', 'pick_up_comment', 'user')
