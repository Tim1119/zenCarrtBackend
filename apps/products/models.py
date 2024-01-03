from django.db import models
from django.contrib.auth import get_user_model 
from apps.brands.models import Brand
from apps.category.models import Category
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
import uuid
from .custom_validators import validate_non_negative_price,validate_discount

User = get_user_model()

class Product(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255,verbose_name=_('Prodcut Name'))
    discount_percent = models.DecimalField(max_digits=5,decimal_places=2, validators=[validate_discount])
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,verbose_name=_('Product Brand'))
    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name=_('NProduct Category'))
    description = models.TextField(verbose_name=_('Product Description'))
    rating = models.IntegerField(verbose_name=_('Product Rating'),validators=[MaxValueValidator(limit_value=5,message='Maximum rating is 5'),MinValueValidator(limit_value=1,message='Minimum rating is 1')])
    price = models.DecimalField(max_digits=7,decimal_places=2,validators=[validate_non_negative_price])
    amount_in_stock =  models.IntegerField(verbose_name=_('Product Rating'),validators=[MinValueValidator(limit_value=0,message='Minimum amount of product in stock is 0')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-created_at"]

    def __str__(self):
        return self.name