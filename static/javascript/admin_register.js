document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("adminRegisterForm");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        const email = form.nm.value;
        if (!email.endsWith("@evsu.edu.ph")) {
            e.preventDefault();
            alert("Email must end with @evsu.edu.ph");
            return false;
        }

        const pwd2 = form.pwd2.value;
        const pwd3 = form.pwd3.value;
        if (pwd2 !== pwd3) {
            e.preventDefault();
            alert("Passwords do not match");
            return false;
        }

    });
});
