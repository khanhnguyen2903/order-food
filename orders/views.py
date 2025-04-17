from django.shortcuts import render, redirect
from firebase_admin import db
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def order_list(request):
  ref = db.reference('orders')  # Lấy dữ liệu từ Firebase
  orders = ref.get() or {}  # Tránh lỗi nếu không có dữ liệu

  # Lọc đơn hàng theo trạng thái nếu có
  status_filter = request.GET.get('status', 'all')
  if status_filter != 'all':
    orders = {k: v for k, v in orders.items() if v.get('status') == status_filter}

  return render(request, 'orders/order_list.html', {'orders': orders, 'status_filter': status_filter})

@csrf_exempt
def update_order_status(request):
  if request.method == "POST":
    try:
      order_id = request.POST.get("order_id")
      if not order_id:
        return JsonResponse({"success": False, "message": "Thiếu order_id"})

      # Lấy tất cả đơn hàng từ Firebase
      ref = db.reference('orders')
      orders = ref.get() or {}

      # Tìm order_data có order_id tương ứng
      matched_order_key = None
      order_data = None

      for key, value in orders.items():
        if value.get("order_id") == order_id:
          matched_order_key = key
          order_data = value
          break

      if not order_data:
        return JsonResponse({"success": False, "message": "Không tìm thấy đơn hàng trong Firebase"})

      current_status = order_data.get("status")

      # Xác định trạng thái mới
      if current_status == "preparing":
        new_status = "prepared"
      elif current_status == "prepared":
        new_status = "unpaid"
      elif current_status == "unpaid":
        new_status = "paid"
      else:
        return JsonResponse({"success": False, "message": "Trạng thái không hợp lệ"})

      # Cập nhật trạng thái của đơn hàng lên Firebase
      order_ref = ref.child(matched_order_key)
      order_ref.update({"status": new_status})

      return redirect('order_list')
    except Exception as e:
      return JsonResponse({"success": False, "message": str(e)})

  return JsonResponse({"success": False, "message": "Phương thức không hợp lệ"})

def order_pay(request):
  if request.method == "POST":
    try:
      order_id = request.POST.get("order_id")
      if not order_id:
        return JsonResponse({"success": False, "message": "Thiếu order_id"})

      # Truy vấn tất cả đơn hàng từ Firebase
      ref = db.reference('orders')
      orders = ref.get() or {}

      # matched_order_key = None
      order_data = None

      for key, value in orders.items():
        if value.get("order_id") == order_id:
          # matched_order_key = key
          order_data = value
          print(order_data)
          break

      if not order_data:
        return JsonResponse({"success": False, "message": "Không tìm thấy đơn hàng trong Firebase"})

      return render(request, 'orders/order_payment.html', {'order': order_data})
    except Exception as e:
      return JsonResponse({"success": False, "message": str(e)})

  return JsonResponse({"success": False, "message": "Phương thức không hợp lệ"})
