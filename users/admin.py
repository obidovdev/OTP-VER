from django.contrib import admin

from .models import UserOTP , CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active',)

@admin.register(UserOTP)
class UserOTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at', 'is_used',)