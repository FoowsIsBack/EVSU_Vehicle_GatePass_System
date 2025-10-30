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
# Login UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/17e7edb7-111c-4221-bc7f-f280303831d8" />

# Register UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/e72f72d6-d208-45d8-8059-b13ba71ed3ff" />

# Forgot Password UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/6bec2f05-ef80-46f7-92d4-3ac6033ddc07" />

# Reset Password UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/5c3927a6-27ac-48df-9da0-f8fa209113be" />
