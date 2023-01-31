from django.urls import path

from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_donation/', views.AddDonationView.as_view(), name='add_donation'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('confirmation/', views.ConfirmationView.as_view(), name='confirmation'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('confirm-taken/<int:pk>', views.ConfirmTakenDonationView.as_view(), name='confirm-taken-donation'),
    path('edite-profile/<int:pk>', views.EditProfileView.as_view(), name='edite-profile'),
    path('change-password/', views.PasswordsChangeView.as_view(), name='change-password'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]
