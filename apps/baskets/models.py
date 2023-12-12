from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.products.models import Product
from apps.users.models import User


class Basket(BaseModel):
    user = models.ForeignKey(User, related_name="basket", on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)
    payment_Date = models.DateTimeField(blank=True, null=True)

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
    final_price = models.PositiveIntegerField(null=True, blank=True)
    count = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = _("Basket Detail")
        verbose_name_plural = _("Basket Details")

    def __str__(self):
        return f"{self.basket.user.get_full_name()} - {self.product.name}"

    def get_total_amount(self):
        return self.count * self.product.price
