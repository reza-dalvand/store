from django.contrib import admin

from .models import MainSlider


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ("title",)
