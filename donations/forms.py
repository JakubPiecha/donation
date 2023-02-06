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
        if 'validation_pass' in self.cleaned_data:
            password = self.cleaned_data['validation_pass']
            valid = check_password(password, self.user.password)
            if not valid:
                raise forms.ValidationError('Błędne hasło')
        else:
            raise forms.ValidationError('To pole jest wymagane')
        return self.cleaned_data

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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=3000, required=True)


