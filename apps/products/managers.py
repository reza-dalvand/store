from django.db import models


class QuerysetManager(models.QuerySet):
    """create new queryset and chainable queries"""

    def active_products(self, is_published=True, soft_deleted=False):
        return self.filter(is_published=is_published, soft_deleted=soft_deleted)


class ProductManager(models.Manager):
    pass
