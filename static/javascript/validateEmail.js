document.getElementById("registerForm").addEventListener("submit", function(event) {
    const email = document.getElementById("email").value.trim();
    const error = document.getElementById("emailError");

    if (!email.endsWith("@evsu.edu.ph")) {
        error.style.display = "block";
        event.preventDefault();
    } else {
        error.style.display = "none";
    }
});
