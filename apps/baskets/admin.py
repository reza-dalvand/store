from django.contrib import admin

from .models import Basket, BasketDetail

# Register your models here.
admin.site.register(Basket)
admin.site.register(BasketDetail)
