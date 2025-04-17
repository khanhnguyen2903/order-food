from django.shortcuts import render, redirect
from products.firebase_service import FirebaseService
from django.http import JsonResponse
from django.contrib import messages
from firebase_admin import db
from datetime import datetime  # Import datetime để tạo order_id

def menu_list(request):
  # Get all products from firebase
  products = FirebaseService.get_all_products()
  # Lấy dữ liệu giỏ hàng từ session
  # cart = request.session.get('cart', [])

  # # Tổng số lượng món trong giỏ hàng
  # total_quantity = sum(item['quantity'] for item in cart.values())

  # return render(request, 'menu/menu_list.html', {'products' : products, 'total_quantity': total_quantity})
  return render(request, 'menu/menu_list.html', {'products' : products})

def add_to_cart(request):
  if request.method == "POST":
    name = request.POST.get("name")
    price = float(request.POST.get("price"))
    quantity = int(request.POST.get("quantity"))
    note = request.POST.get("note", "")

    cart = request.session.get("cart", [])

    cart.append({
      "name": name,
      "price": price,
      "quantity": quantity,
      "note": note,
    })

    request.session["cart"] = cart
    request.session.modified = True

    return JsonResponse({"cart_count": len(cart)})

  return JsonResponse({"error": "Invalid request"}, status=400)

def view_cart(request):
  cart = request.session.get("cart", [])
  # Đảm bảo mỗi item có đủ thông tin trước khi hiển thị
  for index, item in enumerate(cart):
    if not isinstance(item, dict):  # Tránh lỗi nếu item không phải dict
      continue
    item["id"] = index + 1  # Gán ID mặc định nếu thiếu
    item.setdefault("quantity", 1)
    item.setdefault("price", 0)
    item["total_price"] = item["price"] * item["quantity"]  # Tính thành tiền từng món

  request.session["cart"] = cart  # Cập nhật session nếu có thay đổi
  request.session.modified = True  # Đảm bảo session được lưu lại

  total_price = sum(item['total_price'] for item in cart)
  context = {
    'cart': cart,
    'total_price': total_price,
    'view_cart': True,
  }
  return render(request, "menu/cart.html", context)

def remove_from_cart(request, id):
  cart = request.session.get('cart', {})
  # Giữ lại các sản phẩm không bị xóa
  updated_cart = [item for item in cart if item.get("id") != id]
  request.session["cart"] = updated_cart
  request.session.modified = True  # Đánh dấu session đã thay đổi
  messages.success(request, "Sản phẩm đã được xóa khỏi giỏ hàng.")

  return redirect('view_cart')  # Đảm bảo bạn có một view để hiển thị giỏ hàng

def submit_order(request):
  if request.method == "POST":
    cart = request.session.get("cart", [])  # Lấy giỏ hàng từ session
    total_price = sum(item["quantity"] * item["price"] for item in cart)
    table_number = request.POST.get('table_number')

    if not cart:
      return JsonResponse({"success": False, "message": "Giỏ hàng trống!"})

    # Tạo order_id theo thời gian: YYYYMMDDHHMMSS
    order_id = datetime.now().strftime("%Y%m%d%H%M%S")

    # Gửi dữ liệu lên Firebase Realtime Database
    order_ref = db.reference("orders").push()
    order_ref.set({
        "order_id": order_id,
        "items": cart,
        'table_number': table_number,
        "total_price": total_price,
        "status": "preparing"
    })

    # Xóa giỏ hàng sau khi gửi đơn
    request.session["cart"] = []

    # Thêm thông báo thành công
    messages.success(request, f"Menu của bạn đã được tiếp nhận! Mã đơn hàng: {order_id}")

    return redirect("view_cart")  

  messages.error(request, "Có lỗi xảy ra, vui lòng thử lại!")
  return redirect("view_cart")

def logout(request):
  request.session.flush()  # Xóa toàn bộ session
  return redirect("menu_list")  # Chuyển hướng về trang menu