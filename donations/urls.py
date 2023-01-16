from django.urls import path

from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_donation/', views.AddDonationView.as_view(), name='add_donation'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),


]
