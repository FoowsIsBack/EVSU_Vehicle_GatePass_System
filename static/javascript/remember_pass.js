document.addEventListener("DOMContentLoaded", function() {
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("pwd1");
    const rememberCheckbox = document.getElementById("savepass");

    const savedEmail = localStorage.getItem("savedEmail");
    const savedPassword = localStorage.getItem("savedPassword");

    if (savedEmail && savedPassword) {
        emailInput.value = savedEmail;
        passwordInput.value = savedPassword;
        rememberCheckbox.checked = true;
    }

    rememberCheckbox.addEventListener("change", function() {
        if (this.checked) {
            localStorage.setItem("savedEmail", emailInput.value);
            localStorage.setItem("savedPassword", passwordInput.value);
        } else {
            localStorage.removeItem("savedEmail");
            localStorage.removeItem("savedPassword");
        }
    });

    emailInput.addEventListener("input", () => {
        if (rememberCheckbox.checked) {
            localStorage.setItem("savedEmail", emailInput.value);
        }
    });
    passwordInput.addEventListener("input", () => {
        if (rememberCheckbox.checked) {
            localStorage.setItem("savedPassword", passwordInput.value);
        }
    });
});