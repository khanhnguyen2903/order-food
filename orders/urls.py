from django.urls import path
from .views import order_list, update_order_status, order_pay

urlpatterns = [
  path('', order_list, name='order_list'),
  path("update-order-status/", update_order_status, name="update_order_status"),
  path("order_pay/", order_pay, name="order_pay"),
]
