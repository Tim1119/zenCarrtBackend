from .models import Brand
from .serializers import BrandSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from zenCartBackend.custom_permissions import IsAdminUserOrReadOnly



class BrandViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUserOrReadOnly]
