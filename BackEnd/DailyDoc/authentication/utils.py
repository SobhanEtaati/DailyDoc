from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user, request):
    # You can’t send raw integers like user.id in URLs securely. This safely converts the user.id into a base64 string.
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # Generates a time-sensitive token tied to the user’s password hash and last login time.
    token = default_token_generator.make_token(user)

    domain = request.get_host()  # e.g., localhost:8000
    verify_url = f"http://{domain}/auth/verify/{uid}/{token}/"

    subject = "Verify Your Email"
    message = f"Hi {user.first_name},\n\nClick the link below to verify your account:\n{verify_url}"

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
