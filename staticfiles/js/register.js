const btnRegister = document.querySelector(".btn");
const emailInput = document.querySelector("#email");
const passwordInput = document.querySelector("#password");

document.addEventListener("DOMContentLoaded", () => {
  emailInput.value = "abc@gmail.com";
  passwordInput.placeholder = "Password tối thiểu 6 ký tự";
});

btnRegister.addEventListener("click", (event) => {
  const emailValue = emailInput.value.trim();
  const passwordValue = passwordInput.value.trim();
  validate(emailValue, passwordValue, event);
});

const validate = (email, password, event) => {
  if (email === "" || password === "") {
    alert("Email và Password không được để trống");
  } else if (email == "abc@gmail.com") {
    alert("Bạn hãy nhập email khác");
    event.preventDefault();
  } else if (password.length < 6) {
    alert("Bạn hãy nhập password có tối thiểu 6 ký tự");
    event.preventDefault();
  }
};
