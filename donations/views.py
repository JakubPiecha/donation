from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from donations.models import Donation, Institution


# Create your views here.
class HomeView(View):

    def get(self, request):
        bags = sum(Donation.objects.all().values_list('quantity', flat=True))
        count_institutions = Donation.objects.all().values_list('institution').distinct().count()
        foundations = Institution.objects.filter(type=1).order_by('-id')
        pagination_foundations = Paginator(foundations, 5)
        page_1 = request.GET.get('page1')
        try:
            foundations = pagination_foundations.page(page_1)
        except PageNotAnInteger:
            foundations = pagination_foundations.page(1)
        except EmptyPage:
            foundations = pagination_foundations.page(pagination_foundations.num_pages)
        organizations = Institution.objects.filter(type=2).order_by('-id')
        pagination_organizations = Paginator(organizations, 5)
        page_2 = request.GET.get('page2')
        try:
            organizations = pagination_organizations.page(page_2)
        except PageNotAnInteger:
            organizations = pagination_organizations.page(1)
        except EmptyPage:
            organizations = pagination_organizations.page(pagination_organizations.num_pages)
        rebounds = Institution.objects.filter(type=3).order_by('-id')
        pagination_rebounds = Paginator(rebounds, 5)
        page_3 = request.GET.get('page3')
        try:
            rebounds = pagination_rebounds.page(page_3)
        except PageNotAnInteger:
            rebounds = pagination_rebounds.page(1)
        except EmptyPage:
            rebounds = pagination_rebounds.page(pagination_rebounds.num_pages)
        context = {'bags': bags, 'count_institutions': count_institutions, 'rebounds': rebounds,
                   'foundations': foundations, 'organizations': organizations, }
        return render(request, 'index.html', context)


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')
