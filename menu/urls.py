from django.urls import path
from .views import menu_list, add_to_cart, view_cart, remove_from_cart, submit_order, logout

urlpatterns = [
  path('', menu_list, name='menu_list'),
  path("add_to_cart/", add_to_cart, name="add_to_cart"),
  path("cart/", view_cart, name="view_cart"),
  path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
  path('submit_order', submit_order, name='submit_order'),
  path('logout', logout, name='logout')
]