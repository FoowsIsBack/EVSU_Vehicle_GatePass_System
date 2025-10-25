const form = document.getElementById("resetForm");
const pwd1 = document.getElementById("pwd1");
const pwd2 = document.getElementById("pwd2");

form.addEventListener("submit", (e) => {
    if (pwd1.value !== pwd2.value) {
        e.preventDefault();
        pwd1.classList.add("error");
        pwd2.classList.add("error");
        } else {
            pwd1.classList.remove("error");
            pwd2.classList.remove("error");
            }
        });