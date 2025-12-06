from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
import bcrypt
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="f7a8c2b6d8e3f5a1b9c2d4e6f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="evsu_vehicle_gatepass"
    )

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/user_login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("user_login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/user_portal", response_class=HTMLResponse)
def user_portal(request: Request):
    return templates.TemplateResponse("user_portal.html", {"request": request})

@app.get("/forgot", response_class=HTMLResponse)
def forgot(request: Request):
    return templates.TemplateResponse("forgot_pass.html", {"request": request})

@app.get("/admin_portal", response_class=HTMLResponse)
def admin_page(request: Request):
    return templates.TemplateResponse("admin_portal.html", {"request": request})

@app.get("/admin_login", response_class=HTMLResponse)
def admin_login_page(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})

@app.get("/admin_dashboard", response_class=HTMLResponse)
def admin_dashboard_page(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})

@app.get("/admin_register", response_class=HTMLResponse)
def admin_register_page(request: Request):
    return templates.TemplateResponse("admin_register.html", {"request": request})

@app.get("/terms", response_class=HTMLResponse)
def terms_page(request: Request):
    return templates.TemplateResponse("terms.html", {"request": request})

@app.get("/privacy", response_class=HTMLResponse)
def privacy_page(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})

@app.get("/admin_forgotPass", response_class=HTMLResponse)
def admin_forgotPass_page(request: Request):
    return templates.TemplateResponse("admin_forgotPass.html", {"request": request})

@app.get("/user_dashboard", response_class=HTMLResponse)
def user_dashboard(request: Request):
    return templates.TemplateResponse("user_dashboard.html", {"request": request})

@app.get("/admin_resetPass", response_class=HTMLResponse)
def reset_pass(request: Request):
    email = request.query_params.get("email")
    return templates.TemplateResponse("admin_resetPass.html", {"request": request, "email": email})

@app.get("/gcash_pay", response_class=HTMLResponse)
def reset_pass(request: Request):
    email = request.query_params.get("email")
    return templates.TemplateResponse("payment_instructions.html", {"request": request, "email": email})

@app.post("/submit")
async def submit_registration(
    request: Request,
    fullname: str = Form(...),
    evsu_id: str = Form(...),
    contact_number: str = Form(...),
    role: str = Form(...),
    department: str = Form(...),
    nm: str = Form(...),
    pwd2: str = Form(...),
    pwd3: str = Form(...),
):
    if pwd2 != pwd3:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Passwords do not match."}
        )

    hashed_pwd = bcrypt.hashpw(pwd2.encode(), bcrypt.gensalt()).decode()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (nm,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Email already registered."}
        )

    cursor.execute(
        """
        INSERT INTO users (fullname, evsu_id, contact_number, department, email, password, role)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (fullname, evsu_id, contact_number, department, nm, hashed_pwd, role)
    )
    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)

@app.post("/admin_register_submit")
async def admin_register_submit(
    request: Request,
    fullname: str = Form(...),
    evsu_id: str = Form(...),
    nm: str = Form(...),
    username: str = Form(...),
    pwd2: str = Form(...),
    pwd3: str = Form(...),
    contact_number: str = Form(...),
    department: str = Form(...),
    role: str = Form(...),
):
    if len(fullname) > 50:
        return templates.TemplateResponse(
            "admin_register.html",
            {"request": request, "error": "Full Name must not exceed 50 characters."}
        )

    if not nm.endswith("@evsu.edu.ph"):
        return templates.TemplateResponse(
            "admin_register.html",
            {"request": request, "error": "Email must end with @evsu.edu.ph"}
        )

    if len(username) > 50:
        return templates.TemplateResponse(
            "admin_register.html",
            {"request": request, "error": "Username must not exceed 50 characters."}
        )

    if pwd2 != pwd3:
        return templates.TemplateResponse(
            "admin_register.html",
            {"request": request, "error": "Passwords do not match."}
        )

    hashed_pwd = bcrypt.hashpw(pwd2.encode(), bcrypt.gensalt()).decode()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM admins WHERE email=%s", (nm,))
    if cursor.fetchone():
        conn.close()
        return templates.TemplateResponse(
            "admin_register.html",
            {"request": request, "error": "This email is already registered."}
        )

    cursor.execute("SELECT * FROM admins WHERE username=%s", (username,))
    if cursor.fetchone():
        conn.close()
        return templates.TemplateResponse(
            "admin_register.html",
            {"request": request, "error": "Username is already taken."}
        )

    cursor.execute(
        """
        INSERT INTO admins 
        (fullname, evsu_id, email, username, password, contact_number, department, role)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (fullname, evsu_id, nm, username, hashed_pwd, contact_number, department, role)
    )

    conn.commit()
    conn.close()

    return RedirectResponse(url="/admin_portal", status_code=303)

@app.post("/login_auth")
async def login_auth(request: Request, nm: str = Form(...), pwd: str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (nm,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return templates.TemplateResponse(
            "user_login.html",
            {"request": request, "error": "Account not found."}
        )

    if not bcrypt.checkpw(pwd.encode(), user["password"].encode()):
        return templates.TemplateResponse(
            "user_login.html",
            {"request": request, "error": "Incorrect password."}
        )

    # ✅ Save user email (or name) in session
    request.session["user_email"] = user["email"]  # or user["name"]

    # Redirect to dashboard
    return RedirectResponse(url="/user_dashboard", status_code=303)


@app.get("/user_dashboard")
async def user_dashboard(request: Request):
    user_email = request.session.get("user_email")
    if not user_email:
        # Not logged in → redirect to login page
        return RedirectResponse(url="/login")

    # Pass user to template
    return templates.TemplateResponse(
        "user_dashboard.html",
        {"request": request, "user": user_email}
    )

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login")

@app.post("/admin_login_auth")
async def admin_login_auth(
    request: Request,
    nm: str = Form(...),
    pwd: str = Form(...),
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM admins WHERE username=%s OR email=%s", (nm, nm))
    admin = cursor.fetchone()
    conn.close()

    if not admin:
        return templates.TemplateResponse(
            "admin_login.html",
            {"request": request, "error": "Admin account not found."}
        )

    if not bcrypt.checkpw(pwd.encode(), admin["password"].encode()):
        return templates.TemplateResponse(
            "admin_login.html",
            {"request": request, "error": "Incorrect password."}
        )

    return RedirectResponse(url="/admin_dashboard", status_code=303)

@app.post("/forgot_auth")
async def forgot_auth(request: Request, nm: str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s", (nm,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return RedirectResponse(url=f"/reset_pass?email={nm}", status_code=303)
    else:
        return templates.TemplateResponse(
            "forgot_pass.html",
            {"request": request, "error": "Email not found. Please try again."}
        )
    

@app.post("/admin_forgot_auth")
async def forgot_auth(request: Request, nm: str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admins WHERE email=%s", (nm,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return RedirectResponse(url=f"/admin_resetPass?email={nm}", status_code=303)
    else:
        return templates.TemplateResponse(
            "admin_forgotPass.html",
            {"request": request, "error": "Email not found. Please try again."}
        )

@app.get("/reset_pass", response_class=HTMLResponse)
async def reset_pass(request: Request):
    email = request.query_params.get("email")
    return templates.TemplateResponse("reset_pass.html", {"request": request, "email": email})

@app.post("/reset_auth")
async def reset_auth(
    request: Request,
    pwd1: str = Form(...),
    pwd2: str = Form(...),
):
    email = request.query_params.get("email")

    if not email:
        return templates.TemplateResponse(
            "reset_pass.html",
            {"request": request, "error": "Missing email information."}
        )

    if pwd1 != pwd2:
        return templates.TemplateResponse(
            "reset_pass.html",
            {"request": request, "error": "Passwords do not match.", "email": email}
        )

    hashed_pwd = bcrypt.hashpw(pwd1.encode(), bcrypt.gensalt()).decode()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password=%s WHERE email=%s", (hashed_pwd, email))
    conn.commit()
    conn.close()

    return RedirectResponse(url="/user_login", status_code=303)


@app.post("/admin_reset_auth")
async def reset_auth(
    request: Request,
    pwd1: str = Form(...),
    pwd2: str = Form(...),
):
    email = request.query_params.get("email")

    if not email:
        return templates.TemplateResponse(
            "reset_pass.html",
            {"request": request, "error": "Missing email information."}
        )

    if pwd1 != pwd2:
        return templates.TemplateResponse(
            "reset_pass.html",
            {"request": request, "error": "Passwords do not match.", "email": email}
        )

    hashed_pwd = bcrypt.hashpw(pwd1.encode(), bcrypt.gensalt()).decode()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE admins SET password=%s WHERE email=%s", (hashed_pwd, email))
    conn.commit()
    conn.close()

    return RedirectResponse(url="/admin_login", status_code=303)

