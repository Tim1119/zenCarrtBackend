from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from .models import Category
from .serializers import CategorySerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from zenCartBackend.custom_permissions import IsAdminUserOrReadOnly



class CategoryViewSet(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
