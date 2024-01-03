from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/products-brands/', include('apps.brands.urls')),
    path('api/products-categories/', include('apps.category.urls')),
    path('api/products/', include('apps.products.urls')),
]
