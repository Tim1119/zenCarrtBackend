# Generated by Django 5.0.1 on 2024-01-03 05:24

import apps.products.custom_validators
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Prodcut Name')),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5, validators=[apps.products.custom_validators.validate_discount])),
                ('description', models.TextField(verbose_name='Product Description')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=5, message='Maximum rating is 5'), django.core.validators.MinValueValidator(limit_value=1, message='Minimum rating is 1')], verbose_name='Product Rating')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, validators=[apps.products.custom_validators.validate_non_negative_price])),
                ('amount_in_stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='Minimum amount of product in stock is 0')], verbose_name='Product Rating')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='brands.brand', verbose_name='Product Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category', verbose_name='NProduct Category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
    ]
