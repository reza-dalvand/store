from django.contrib import admin

from .models import Basket, BasketDetail


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("user", "is_open")


@admin.register(BasketDetail)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("product", "basket", "final_price", "count")
