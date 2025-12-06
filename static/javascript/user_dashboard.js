window.onload = function () {
    document.getElementById("panel").style.display = "block";
};

function togglePanel() {
    var panel1 = document.getElementById("panel");
    var panel2 = document.getElementById("tracker");
    var panel3 = document.getElementById("payment");
    var btn1 = document.getElementById("btn1");
    var btn2 = document.getElementById("btn2");
    var btn3 = document.getElementById("btn3");

    panel1.style.display = "block";
    btn1.classList.add("active");

    panel2.style.display = "none";
    btn2.classList.remove("active");

    panel3.style.display = "none";
    btn3.classList.remove("active");
}

function toggleTracker() {
    var panel1 = document.getElementById("panel");
    var panel2 = document.getElementById("tracker");
    var panel3 = document.getElementById("payment");
    var btn1 = document.getElementById("btn1");
    var btn2 = document.getElementById("btn2");
    var btn3 = document.getElementById("btn3");

    panel2.style.display = "block";
    btn2.classList.add("active");

    panel1.style.display = "none";
    btn1.classList.remove("active");

    panel3.style.display = "none";
    btn3.classList.remove("active");
}

function togglePayment() {
    var panel1 = document.getElementById("panel");
    var panel2 = document.getElementById("tracker");
    var panel3 = document.getElementById("payment");
    var btn1 = document.getElementById("btn1");
    var btn2 = document.getElementById("btn2");
    var btn3 = document.getElementById("btn3");

    panel3.style.display = "block";
    btn3.classList.add("active");

    panel1.style.display = "none";
    btn1.classList.remove("active");

    panel2.style.display = "none";
    btn2.classList.remove("active");
}


const buttons = document.querySelectorAll(".nav-btn");

buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        buttons.forEach(b => b.classList.remove("active"));

        btn.classList.add("active");
    });
});