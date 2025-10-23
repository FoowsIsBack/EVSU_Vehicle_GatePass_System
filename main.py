from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
import hashlib

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="evsu_vehicle_gatepass"
    )

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/submit")
async def submit_registration(
    nm: str = Form(...),
    pwd2: str = Form(...),
    pwd3: str = Form(...),
):
    if pwd2 != pwd3:
        return {"error": "Passwords do not match"}

    hashed_pwd = hashlib.sha256(pwd2.encode()).hexdigest()[:15]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = %s", (nm,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return {"error": "Email already registered"}

    cursor.execute(
        "INSERT INTO users (email, password) VALUES (%s, %s)",
        (nm, hashed_pwd)
    )
    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)

@app.post("/login_auth")
async def login_auth(
    nm: str = Form(...),
    pwd: str = Form(...),
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (nm,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return {"error": "Account not found"}

    entered_hash = hashlib.sha256(pwd.encode()).hexdigest()[:15]

    if entered_hash != user["password"]:
        return {"error": "Incorrect password"}

    return RedirectResponse(url="/dashboard", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
