from django.urls import path

from store import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    path('add-product/', views.add_product, name='add-product'),
]
