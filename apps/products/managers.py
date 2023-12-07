from django.db import models


class QuerysetManager(models.QuerySet):
    """create new queryset and chainable queries"""

    def active_products(self):
        return self.filter(is_published=True, soft_deleted=False)


class ProductManager(models.Manager):
    pass
