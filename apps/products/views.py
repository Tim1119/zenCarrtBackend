from .models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from zenCartBackend.custom_permissions import IsAdminUserOrReadOnly

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]