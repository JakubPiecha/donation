from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from donations.forms import RegistrationForm, CustomLoginForm, DonationForm
from donations.models import Donation, Institution, CustomUser, Category


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


class AddDonationView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('donations:login')
    form_class = DonationForm
    success_url = reverse_lazy('donations:confirmation')
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(AddDonationView, self).get_context_data(**kwargs)
        context['institutions'] = Institution.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        print(self.object)
        return super(AddDonationView, self).form_valid(form)


class LoginPageView(View):
    template_name = 'login.html'
    form_class = CustomLoginForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form_class(data=request.POST)
        username = request.POST.get('username')
        user = CustomUser.objects.filter(email=username)
        if not user:
            return redirect('donations:register')
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('donations:home')
        return render(request, self.template_name, context={'form': form})


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('donations:login')


class ConfirmationView(TemplateView):
    template_name = 'form-confirmation.html'


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'profile.html')

