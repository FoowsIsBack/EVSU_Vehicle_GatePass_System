function togglePasswordVisibility(inputId, iconId) {
  const passwordInput = document.getElementById(inputId);
  const togglePassword = document.getElementById(iconId);

  if (!passwordInput || !togglePassword) {
    console.error("Missing element:", inputId, iconId);
    return;
  }

  togglePassword.addEventListener("click", function () {
    const isPassword = passwordInput.getAttribute("type") === "password";
    passwordInput.setAttribute("type", isPassword ? "text" : "password");

    togglePassword.src = isPassword
      ? "/static/icons/openPass.png"
      : "/static/icons/closePass.png";
  });
}

document.addEventListener("DOMContentLoaded", function () {
  togglePasswordVisibility("pwd1", "togglePassword1");
  togglePasswordVisibility("pwd2", "togglePassword2");
  togglePasswordVisibility("pwd3", "togglePassword3");
});
