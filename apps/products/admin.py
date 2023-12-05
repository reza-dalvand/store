from django.contrib import admin

from .models import (
    Product,
    ProductBrand,
    ProductCategory,
    ProductComment,
    ProductGallery,
)

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
admin.site.register(ProductGallery)
admin.site.register(ProductComment)
