# Register your models here.
from django.contrib import admin

from .models import SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active")
