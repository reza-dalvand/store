from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel


class ProductBrand(BaseModel):
    name = models.CharField(_("name"), max_length=255)
    slug = models.SlugField(_("slug"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(ProductBrand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductCategory(BaseModel):
    parent = models.ForeignKey(
        "ProductCategory", null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=255)
    slug = models.SlugField(_("slug"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(
        ProductCategory,
        null=True,
        blank=True,
        related_name="products_category",
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        ProductBrand,
        null=True,
        blank=True,
        related_name="products_brand",
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("name"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255)
    image = models.ImageField(_("image"), upload_to="products")
    short_desc = models.TextField(_("short description"), null=True, blank=True)
    long_desc = models.TextField(_("long description"), null=True, blank=True)
    is_published = models.BooleanField(_("is products published"), default=False)
    soft_deleted = models.BooleanField(_("is products soft deleted"), default=False)
    price = models.IntegerField(_("price"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class ProductGallery(BaseModel):
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        related_name="product_gallery",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(_("image"), upload_to="galleries", null=True, blank=True)

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    def __str__(self):
        return self.product.name


class ProductComment(models.Model):
    product = models.ForeignKey(
        Product, related_name="comments", on_delete=models.CASCADE
    )
    full_name = models.CharField(_("full_name"), max_length=200)
    email = models.EmailField(_("email address"))
    message = models.TextField(_("message"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.full_name
