from django.shortcuts import render, redirect
from .firebase_service import FirebaseService
import firebase_admin
from firebase_admin import credentials, db
from .forms import ProductForm, UpdateProductForm
from django.http import HttpResponse

def product_list(request):
  """Hiển thị danh sách sản phẩm"""
  products = FirebaseService.get_all_products()

  return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
  if request.method == "POST":
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    url_image = request.POST.get("url_image")
    # print(name, price, description, url_image)
    if not all([name, price, description, url_image]):
      return HttpResponse("Thiếu thông tin sản phẩm!", status=400)
    
    # Thêm vào Firebase Realtime Database
    FirebaseService.add_product(name, price, description, url_image)
    return redirect('product_list')
  
  return render(request, "products/add_product.html")

def update_product(request, product_id):
  product = FirebaseService.get_product(product_id)

  if not product:
    return redirect('product_list')  # Nếu sản phẩm không tồn tại, quay lại danh sách
  
  """Cập nhật sản phẩm"""
  if request.method == "POST":
    price = request.POST.get('price')
    description = request.POST.get("description")
    url_image = request.POST.get("url_image")
    
    FirebaseService.update_product(product_id, price, description, url_image)
    return redirect('product_list')
  
  return render(request, 'products/update_product.html', {'product': product, 'product_id': product_id})

def delete_product(request, product_id):
  """Xóa sản phẩm"""
  FirebaseService.delete_product(product_id)
  return redirect('product_list')