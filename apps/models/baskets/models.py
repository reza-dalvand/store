from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel
from apps.models.products.models import Product
from django.utils.translation import gettext_lazy as _


class Basket(BaseModel):
    user = models.ForeignKey(User, related_name="basket", on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)
    payment_Date = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        return self.user.get_full_name()


class BasketDetail(BaseModel):
    product = models.ForeignKey(
        Product, related_name="products", on_delete=models.CASCADE
    )
    basket = models.ForeignKey(Basket, related_name="details", on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Basket Detail")
        verbose_name_plural = _("Basket Details")

    def __str__(self):
        return f"{self.basket.user.get_full_name()} - {self.product.name}"

    def get_total_amount(self):
        return self.count * self.product.price
