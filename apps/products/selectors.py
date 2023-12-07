from typing import List

from django.db.models import Q

from apps.products.models import Product


def get_active_products(category=None, brand=None) -> List[Product]:
    qs = Product.objects.select_related("category", "brand").active_products()
    if category or brand:
        return qs.filter(
            Q(brand__slug__exact=brand) | Q(category__slug__exact=category)
        )
    return qs
