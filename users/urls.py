from django.urls import path
from .views import register_view, verify_otp_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('verify-otp/', verify_otp_view, name='verify-otp'),
]