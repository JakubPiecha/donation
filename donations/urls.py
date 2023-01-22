from django.urls import path

from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_donation/', views.AddDonationView.as_view(), name='add_donation'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('confirmation/', views.ConfirmationView.as_view(), name='confirmation'),


]
