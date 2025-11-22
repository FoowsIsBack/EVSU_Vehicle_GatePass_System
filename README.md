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
<img width="1619" height="851" alt="image" src="https://github.com/user-attachments/assets/3b937ddb-20f6-493e-9fcf-e4e210fcc601" />

# User Register UI
<img width="1766" height="946" alt="image" src="https://github.com/user-attachments/assets/35a7b762-1ba2-4fcd-a29b-80adc7033233" />

```sh
Note: I added a scrollbar because the content in my form is too long to fit on the screen
```

# User Portal UI
<img width="1649" height="859" alt="image" src="https://github.com/user-attachments/assets/3d6ca804-8123-4328-9fb2-e905d8c9a0cf" />

# User Login UI
<img width="799" height="743" alt="image" src="https://github.com/user-attachments/assets/aa4760aa-e70f-4184-aa2e-bed7ec58caf2" />

# User Forgot Acc UI
<img width="936" height="371" alt="image" src="https://github.com/user-attachments/assets/8d67a7ca-56ef-4e12-8665-21294566160d" />

# User Reset Password UI
<img width="936" height="704" alt="image" src="https://github.com/user-attachments/assets/1265bae0-2da4-4a20-92cd-ee2098a8c784" />

# Admin Portal
<img width="1649" height="859" alt="image" src="https://github.com/user-attachments/assets/331afdce-2f18-4ca6-b57f-e1ce01d59954" />

```sh
Note: http://localhost/admin_portal is the link you can use to access the Admin Portal.
```
