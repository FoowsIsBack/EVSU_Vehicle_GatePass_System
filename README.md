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
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
# Login UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/17e7edb7-111c-4221-bc7f-f280303831d8" />

# Register UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/c081849a-09ff-423e-a27e-b202ad38a4e3" />
