from django.urls import path
from .views import EmailValidationView, LoginView, LogoutView, PasswordReset, RegistrationView, UsernameValidationView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register',RegistrationView.as_view(), name='register'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('reset-password',csrf_exempt(PasswordReset.as_view()), name='reset-password'),
]
