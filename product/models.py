from django.db import models

from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager


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
    brand = models.ForeignKey('Brand',related_name='product_brand' , on_delete=models.SET_NULL,null=True,blank=True)
    category =models.ForeignKey('Category',related_name='product_category' , on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
    
    

class ProductImanges(models.Model):
    product =models.ForeignKey(Product,related_name='product_image' , on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='product_image/')

    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"))

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"))

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    user = models.ForeignKey(User,related_name='user_review' ,verbose_name=_("User"), on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    rate = models.IntegerField(_("Rate"),validators=[MinValueValidator(0),MaxValueValidator(5)])
    review = models.TextField(_("Review"),max_length=500)
    created_at = models.DateTimeField(_("Created At"),default=timezone.now)
    
    def __str__(self):
        return str(self.user)