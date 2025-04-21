// // Cấu hình Firebase
// const firebaseConfig = {
//   apiKey: "AIzaSyBJH7mYtBWLhJh_p16nt0XwefDJCIjBDU8",
//   authDomain: "djangodemo-82034.firebaseapp.com",
//   databaseURL:
//     "https://djangodemo-82034-default-rtdb.asia-southeast1.firebasedatabase.app",
//   projectId: "djangodemo-82034",
//   storageBucket: "djangodemo-82034.firebasestorage.app",
//   messagingSenderId: "641628217223",
//   appId: "1:641628217223:web:41310310bd066774d03d22",
//   measurementId: "G-CYQBY7YFRK",
// };

// // Khởi tạo Firebase
// // Kiểm tra nếu Firebase chưa được khởi tạo
// if (!firebase.apps.length) {
//   firebase.initializeApp(firebaseConfig);
// }
// // const app = firebase.initializeApp(firebaseConfig);
// const database = firebase.database();

// // Xử lý khi nhấn nút "Lưu Lại"
// document.getElementById("saveProduct").addEventListener("click", function () {
//   const name = document.getElementById("name").value.trim();
//   const price = document.getElementById("price").value.trim();
//   const description = document.getElementById("description").value.trim();
//   const url_image = document.getElementById("imageUrl").value.trim();

//   // Kiểm tra dữ liệu nhập vào
//   if (!name || !price) {
//     alert("Vui lòng nhập tên món ăn và giá bán!");
//     return;
//   }

//   // Đẩy dữ liệu lên Firebase
//   const newProductRef = database.ref("products").push();
//   newProductRef
//     .set({
//       name: name,
//       price: parseFloat(price),
//       description: description,
//       url_image: url_image,
//     })
//     .then(() => {
//       alert("Thêm sản phẩm thành công!");
//       document.getElementById("productForm").reset(); // Xóa dữ liệu sau khi thêm
//     })
//     .catch((error) => {
//       alert("Lỗi: " + error.message);
//     });
// });
