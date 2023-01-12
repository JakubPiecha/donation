from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView

from donations.models import Donation, Institution


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['bags'] = sum(Donation.objects.all().values_list('quantity', flat=True))
        data['count_institutions'] = Donation.objects.all().values_list('institution').distinct().count()
        data['institutions'] = Institution.objects.all()
        print(data)
        return data


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')



