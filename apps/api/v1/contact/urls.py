from django.urls import path

from .api import ContactUsView

app_name = "contact"


urlpatterns = [path("contact", ContactUsView.as_view(), name="contact-us")]
