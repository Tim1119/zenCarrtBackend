from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
import uuid

# Create your models here.
class Category(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name=_('Name of Category'),max_length=255,unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(verbose_name=_('Category Description'))
    logo = models.ImageField(verbose_name=_('Category Logo'),upload_to='category-logos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ["-created_at"]


    def __str__(self):
        return self.name
