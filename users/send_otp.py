from django.core.mail import send_mail

def send_otp_mail(user, otp):
    send_mail(
        subject="obidovdev bilan akkauntingizni tasdiqlang!",
        message=f"Assalomu aleykum @{user.username} ({user.first_name} {user.last_name})\n\nSizning tasdiqlash kodingiz: {otp}",
        from_email="obidovdeveloper@gmail.com",
        recipient_list=[user.email]
    )
    return f"Email sent to {user.email}"