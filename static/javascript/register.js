document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("registerForm");
    const email = document.getElementById("email");
    const pwd2 = document.getElementById("pwd2");
    const pwd3 = document.getElementById("pwd3");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        [email, pwd2, pwd3].forEach(input => input.classList.remove("error"));

        if (pwd2.value !== pwd3.value) {
            pwd2.classList.add("error");
            pwd3.classList.add("error");
            return;
        }

        const formData = new FormData(form);
        const res = await fetch("/submit", {
            method: "POST",
            body: formData
        });

        const data = await res.json().catch(() => ({}));

        if (data.error) {
            if (data.error.includes("Email")) {
                email.classList.add("error");
            }
            if (data.error.includes("Password")) {
                pwd2.classList.add("error");
                pwd3.classList.add("error");
            }
            return;
        }

        window.location.href = "/";
    });
});
