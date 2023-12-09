from django.contrib import admin

from .models import ContactUs


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "subject", "is_read")
