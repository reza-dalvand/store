from django.db import models


class AdditionalQueryset(models.QuerySet):
    """create new query set and chainable queries"""

    def active_products(self, is_published=True, soft_deleted=False):
        return self.filter(is_published=is_published, soft_deleted=soft_deleted)


class ProductManager(models.Manager):
    pass
