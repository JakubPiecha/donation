from django.urls import path, reverse_lazy

from . import views
from django.contrib.auth import views as auth_views

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
    path('reset-password/', views.PasswordsResetView.as_view(), name='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset-password-done.html'), name='reset_password-done'),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset-password-confirm.html', success_url=reverse_lazy('donations:reset-password-complete')
        ), name='reset-password-confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset-password-complete.html'), name='reset-password-complete'),

]
