from rest_framework.routers import DefaultRouter
from .views import BrandViewSet
from django.urls import path,include

router = DefaultRouter()
router.register('brands',BrandViewSet,basename='brands')


urlpatterns = [
    path('',include(router.urls))
]