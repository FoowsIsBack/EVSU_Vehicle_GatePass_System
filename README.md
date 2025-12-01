# Tech Stack
[![tect_stack](https://skillicons.dev/icons?i=html,css,js,fastapi,mysql)](https://skillicons.dev)

# Run local

## Clone the project
```sh
git clone https://github.com/FoowsIsBack/EVSU_Vehicle_GatePass_System
```

## Install dependencies
```sh
pip install -r requirements.txt
```

## Run server
```sh
uvicorn main:app --reload
```
## MySQL
```sql
CREATE DATABASE evsu_vehicle_gatepass;

USE evsu_vehicle_gatepass;

CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    fullname VARCHAR(50) NOT NULL,
    evsu_id VARCHAR(15) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    department VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(50),
    evsu_id VARCHAR(50),
    email VARCHAR(50),
    username VARCHAR(50),
    password TEXT,
    contact_number VARCHAR(11),
    department VARCHAR(100),
    role VARCHAR(100)
);

```
# Main
<img width="1619" height="832" alt="image" src="https://github.com/user-attachments/assets/7b02f55c-264c-47ed-9b66-a52f21c71ba4" />

# User Register UI
<img width="516" height="806" alt="image" src="https://github.com/user-attachments/assets/ba7e4c81-8d97-4ccf-a75b-3ff628e97334" />

> [!NOTE]
> **Note: I added a scrollbar because the form content is too long to fit on the screen.**

# User Portal UI
<img width="1649" height="841" alt="image" src="https://github.com/user-attachments/assets/2967956d-a4bb-4616-abf0-c230c7fa0a22" />

# Admin Portal UI
<img width="1649" height="859" alt="image" src="https://github.com/user-attachments/assets/331afdce-2f18-4ca6-b57f-e1ce01d59954" />

# User Login UI
<img width="702" height="710" alt="image" src="https://github.com/user-attachments/assets/aaf5699d-780c-43d1-a781-e2d9b8d913a6" />

# User Forgot Acc UI
<img width="731" height="487" alt="image" src="https://github.com/user-attachments/assets/fc165311-0247-45b2-a32e-dcb500457206" />

# User Reset Password UI
<img width="720" height="689" alt="image" src="https://github.com/user-attachments/assets/e8ea864c-3aad-4244-882e-77d02c8926be" />

> [!NOTE]
> This link lets you access the Admin Portal:
> **http://localhost/admin_portal**

# Admin Register UI
<img width="1080" height="877" alt="image" src="https://github.com/user-attachments/assets/decbef34-e4ea-4185-a29d-33f4cf00f557" />

> [!NOTE]
> **Note: I added a scrollbar because the form content is too long to fit on the screen.**

# Admin Login UI
<img width="782" height="713" alt="image" src="https://github.com/user-attachments/assets/34a23327-dc06-41d9-a639-0dcf4fed54d5" />

# Admin Forgot Acc UI
<img width="730" height="485" alt="image" src="https://github.com/user-attachments/assets/cd5c6ab3-3e66-41ba-81db-6598e83977bb" />

# Admin Reset Password UI
<img width="719" height="686" alt="image" src="https://github.com/user-attachments/assets/e5918fe1-1a35-4551-b1f1-6ae93079e66d" />
