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
<img width="799" height="743" alt="image" src="https://github.com/user-attachments/assets/4aec5d13-846f-4a41-a36d-a8078450cac1" />

# User Forgot Acc UI
<img width="654" height="625" alt="image" src="https://github.com/user-attachments/assets/437d8bf0-f43e-406e-a197-5f3d2ba15a15" />

# User Reset Password UI
<img width="936" height="704" alt="image" src="https://github.com/user-attachments/assets/1265bae0-2da4-4a20-92cd-ee2098a8c784" />

# Admin Portal
<img width="1649" height="859" alt="image" src="https://github.com/user-attachments/assets/331afdce-2f18-4ca6-b57f-e1ce01d59954" />

> [!NOTE]
> This link lets you access the Admin Portal:
> **http://localhost/admin_portal**

