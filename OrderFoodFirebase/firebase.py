import firebase_admin
from firebase_admin import credentials, db
import os, json
from django.conf import settings

# Kiểm tra biến môi trường
firebase_creds_json = os.getenv('FIREBASE_CREDENTIALS')
if firebase_creds_json:
  # Chạy trên Render: dùng biến môi trường
  cred = credentials.Certificate(json.loads(firebase_creds_json))
else:
  # Chạy local: dùng file JSON
  # Đường dẫn tuyệt đối tới file firebase_config.json
  firebaseKey_path = os.path.join(settings.BASE_DIR, 'firebase_config.json')
  # Load credentials từ file JSON
  cred = credentials.Certificate(firebaseKey_path)

# Link database từ Firebase (Realtime DB chứ không phải Firestore)
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://djangodemo-82034-default-rtdb.asia-southeast1.firebasedatabase.app/' 
})

# if not firebase_admin._apps:
#   cred_json = os.environ.get("FIREBASE_CREDENTIALS")
#   if cred_json:
#     # Dùng biến môi trường
#     cred_dict = json.loads(cred_json)
#     cred = credentials.Certificate(cred_dict)
#     firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://djangodemo-82034-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Thay bằng URL Firebase của bạn
#     })
# # Khởi tạo Firebase
# # cred = credentials.Certificate(FIREBASE_CREDENTIALS)
# # firebase_admin.initialize_app(cred, {
# #     'databaseURL': 'https://djangodemo-82034-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Thay bằng URL Firebase của bạn
# # })

# db = firestore.client()