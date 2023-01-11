from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')



