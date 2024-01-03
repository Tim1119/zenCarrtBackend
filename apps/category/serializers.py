from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("pkid","id","name","slug","description","logo","created_at","updated_at")



