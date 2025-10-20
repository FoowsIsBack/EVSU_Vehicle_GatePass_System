const passwordInput = document.getElementById("pwd");
const togglePassword = document.getElementById("togglePassword");

togglePassword.addEventListener("click", function () {
  const type = passwordInput.getAttribute("type") === "password" ? "text" : "password";
  passwordInput.setAttribute("type", type);

  if (type === "text") {
    togglePassword.src = "/static/icons/openPass.png";
  } else {
    togglePassword.src = "/static/icons/closePass.png";
  }
});
