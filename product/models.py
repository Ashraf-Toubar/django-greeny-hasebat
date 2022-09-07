from django.db import models

from django.utils.translation import gettext as _

FLAG_OPTION = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    subtitle = models.CharField(_("Subtitle"), max_length=500)
    sku = models.IntegerField(_("SKU"))
    desc = models.TextField(_("Description"),max_length=10000)
    price = models.FloatField(_("Price"))
    flag = models.CharField(_("Flag"), max_length=10,choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity"))


class ProductImanges(models.Model):
    pass

class Brand(models.Model):
    pass

class Category(models.Model):
    pass


class ProductReview(models.Model):
    pass