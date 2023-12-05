from django.urls import path

from apps.contact.api.v1.apis.contact import ContactUsView

urlpatterns = [path("contact", ContactUsView.as_view(), name="contact-us")]
