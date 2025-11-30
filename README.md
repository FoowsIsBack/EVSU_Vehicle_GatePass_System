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

# User Login UI
<img width="722" height="695" alt="image" src="https://github.com/user-attachments/assets/6dcb9597-b6d9-48de-a4cc-21e87fddbb98" />

# User Forgot Acc UI
<img width="649" height="496" alt="image" src="https://github.com/user-attachments/assets/79b360c0-39f9-4499-bc9a-c5adec7866f6" />

# User Reset Password UI
<img width="949" height="686" alt="image" src="https://github.com/user-attachments/assets/25276f7c-989d-41dd-bef9-ecf18a9abb94" />

# Admin Portal UI
<img width="1649" height="859" alt="image" src="https://github.com/user-attachments/assets/331afdce-2f18-4ca6-b57f-e1ce01d59954" />

> [!NOTE]
> This link lets you access the Admin Portal:
> **http://localhost/admin_portal**

# Admin Register UI
<img width="1080" height="877" alt="image" src="https://github.com/user-attachments/assets/decbef34-e4ea-4185-a29d-33f4cf00f557" />

> [!NOTE]
> **Note: I added a scrollbar because the form content is too long to fit on the screen.**

# Admin Login UI
<img width="663" height="675" alt="image" src="https://github.com/user-attachments/assets/5db48ef2-73d3-4966-a564-ed80fa54d9eb" />


