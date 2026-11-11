from django.shortcuts import render, redirect
from .forms import RegisterForm, VerifyOTPForm
from .models import CustomUser, UserOTP
from django.contrib import messages
from .utils import generate_otp
from .send_otp import send_otp_mail


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            otp = generate_otp()
            UserOTP.objects.create(user=user, otp=otp)
            send_otp_mail(user, otp)
            messages.success(request, 'Siz muvaffaqiyatli ro\'yxatdan o\'tdingiz, iltimos OTP kodni kiriting!')
            return redirect('verify-otp')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def verify_otp_view(request):
    if request.method == 'POST':
        form = VerifyOTPForm(request.POST or None)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            user_otp = UserOTP.objects.filter(otp=otp, is_used=False).last()
            if user_otp:
                user_otp.user.is_active = True
                user_otp.user.save()
                user_otp.is_used = True
                user_otp.save()
                messages.success(request, 'Sizning akkauntingiz tasdiqlandi!')
                return redirect('login')
            else:
                messages.error(request, "OTP kod noto'g'ri yoki eskirgan!")
    else:
        form = VerifyOTPForm()

    context = {
        'form': form
    }
    return render(request, 'users/verify_otp.html', context)