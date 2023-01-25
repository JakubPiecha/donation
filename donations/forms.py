from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.hashers import check_password
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


class ChangePasswordsForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]


class EditeProfileForm(UserChangeForm):
    validation_pass = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'validation_pass'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(EditeProfileForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['validation_pass']
        valid = check_password(password, self.user.password)
        if not valid:
            raise forms.ValidationError('Błędne hasło')
        return password

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
