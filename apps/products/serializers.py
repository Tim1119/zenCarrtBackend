from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(read_only=True, many=True, source='review_set')

    class Meta:
        model = Product
        fields = ("pkid","id","name","brand","category","description","rating","price","amount_in_stock","created_at","updated_at")



