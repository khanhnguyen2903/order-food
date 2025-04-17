from firebase_admin import db
from OrderFoodFirebase.firebase import *

class FirebaseService:
  ref = db.reference('products')  # Thư mục trong Firebase

  @staticmethod
  def add_product(name, price, description, url_image):
    """Thêm sản phẩm mới"""
    new_product = FirebaseService.ref.push({
      'name': name,
      'price': price,
      'description': description,
      'url_image' : url_image
    })
    return new_product.key  # Trả về ID của sản phẩm

  @staticmethod
  def update_product(product_id, price=None, description=None, url_image=None):
    """Cập nhật sản phẩm"""
    product_ref = FirebaseService.ref.child(product_id)
    updates = {}
    # if name:
    #   updates['name'] = name
    if price:
      updates['price'] = price
    if description:
      updates['description'] = description
    if url_image:
      updates['url_image'] = url_image
    product_ref.update(updates)

  @staticmethod
  def delete_product(product_id):
    """Xóa sản phẩm"""
    FirebaseService.ref.child(product_id).delete()

  @staticmethod
  def get_all_products():
    """Lấy danh sách tất cả sản phẩm"""
    return FirebaseService.ref.get() or {}

  @staticmethod
  def get_product(product_id):
    """Lấy thông tin sản phẩm cụ thể"""
    return FirebaseService.ref.child(product_id).get()
