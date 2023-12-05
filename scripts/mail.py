from django.core.mail import send_mail

from config.settings import email


def send_mail_to_users(subject, message, recipient_list):
    email_from = email_settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
