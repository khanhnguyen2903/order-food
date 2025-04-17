from django.urls import path
from .views import product_list, add_product, update_product, delete_product

urlpatterns = [
  path('', product_list, name='product_list'),
  path('add/', add_product, name='add_product'),
  path('update/<str:product_id>/', update_product, name='update_product'),
  path('delete/<str:product_id>/', delete_product, name='delete_product'),
]