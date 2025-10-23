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
## MYSQL
```sql
CREATE DATABASE evsu_vehicle_gatepass;

USE evsu_vehicle_gatepass;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
# Login UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/125f67ed-e6c8-423b-a5df-0a7a5338bc5e" />

# Register UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/238ec10d-2d9c-4cde-aa2c-5f09977b2954" />
