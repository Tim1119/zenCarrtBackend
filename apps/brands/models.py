from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
import uuid


class Brand(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name=_('Brand Name'),max_length = 255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField()
    logo = models.ImageField(verbose_name=_('Brand Logo'),upload_to='brand-logos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ["-created_at"]

    def __str__(self):
        return self.name








   