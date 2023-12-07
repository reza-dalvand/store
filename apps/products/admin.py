from django.contrib import admin

from .models import (
    Product,
    ProductBrand,
    ProductCategory,
    ProductComment,
    ProductGallery,
)

admin.site.register(ProductGallery)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "soft_deleted", "price")


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "message")
