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

# Login UI
<img width="1460" height="906" alt="image" src="https://github.com/user-attachments/assets/17e7edb7-111c-4221-bc7f-f280303831d8" />

# User Register UI
<img width="1766" height="946" alt="image" src="https://github.com/user-attachments/assets/35a7b762-1ba2-4fcd-a29b-80adc7033233" />

# User Login UI
<img width="936" height="704" alt="image" src="https://github.com/user-attachments/assets/a52772b1-6583-4d58-8c2a-1465ac3301c1" />

# User Forgot Acc UI
<img width="936" height="371" alt="image" src="https://github.com/user-attachments/assets/8d67a7ca-56ef-4e12-8665-21294566160d" />

# User Reset Password UI
<img width="936" height="704" alt="image" src="https://github.com/user-attachments/assets/1265bae0-2da4-4a20-92cd-ee2098a8c784" />
