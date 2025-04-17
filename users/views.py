from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth
import requests

FIREBASE_API_KEY = "AIzaSyBJH7mYtBWLhJh_p16nt0XwefDJCIjBDU8"

def register(request):
  if request.method == "POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
      user = auth.create_user(email=email, password=password)
      messages.success(request, "Đăng ký thành công! Vui lòng đăng nhập.")
      # Lưu email vào session để chuyển sang trang login
      request.session["registered_email"] = email  
      return redirect("login")
    except Exception as e:
      # messages.error(request, f"Đăng ký thất bại: {e}")
      print(e)
  return render(request, "users/register.html")

def login(request):
  request.session.pop("registered_email", None)
  if request.method == "POST":
    email = request.POST.get("email")
    password = request.POST.get("password")

    payload = {
      "email": email,
      "password": password,
      "returnSecureToken": True
    }
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    response = requests.post(url, json=payload)

    if response.status_code == 200:
      user_data = response.json()
      request.session["user_id"] = user_data.get("localId")  # Lưu user ID vào session
      request.session["id_token"] = user_data.get("idToken")  # Lưu token xác thực
      request.session ['email_user'] = email
      return redirect("menu_list")  # Chuyển đến trang đặt món
    else:
      messages.error(request, "Email hoặc mật khẩu không đúng!")

  return render(request, "users/login.html")

