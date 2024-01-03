from rest_framework import serializers
from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Brand 
        fields = '__all__'


    def get_products(self,obj):
        return obj.product_set.all()

   
