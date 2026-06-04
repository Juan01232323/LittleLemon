# LittleLemon API: Reservation Management System

![Meta](https://img.shields.io/badge/Meta-0467DF?style=for-the-badge&logo=meta&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-Django--REST--Framework-red?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=jsonwebtokens)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

##  Project Description

The system allows you to manage key restaurant operations:

- User management and authentication
- Reservation creation and management
- Menu management
- Role-based access control
- Fully functional REST API

---

##  Objective

To build a scalable backend API that allows:

- Persistent data management
- Endpoint security
- Separation of responsibilities
- Integration with frontend clients or tools like Postman

---

##  Technology Stack

| Área                 | Tecnología                     |
|----------------------|-------------------------------|
| Backend             | Python                        |
| Framework           | Django                        |
| API                 | Django REST Framework         |
| Base de datos       | MySQL / SQLite                |
| Autenticación       | Token Authentication / JWT    |
| Control de versiones| Git / GitHub                  |

---

##  Main Features

###  Authentication and Authorization

- User registration
- Token login
- Endpoint protection
- Access control by role:

- Administrator

- User (client)

---

###  Menu Management

- Create, edit, and delete dishes
- List of available products
- Filtering and sorting

---

###  Reservation System

- Create reservations
- Availability check
- View reservations by user
- Reservation management (admin)

---

###  Order Management (Optional)

- Create orders
- View order history
- Order status

---

##  Main Endpoints

###  Authentication

- `POST /restaurant/users/` → Registration
- `POST /restaurant/token/login/` → Login

---

###  Menu

- `GET /restaurant/menu-items/` → List menu

- `POST /restaurant/menu-items/` → Create dish (admin)

- `PUT /restaurant/menu-items/{id}` → Update

- `DELETE /restaurant/menu-items/{id}` → Delete

---

###  Reservations

- `GET /restaurant/bookings/` → List reservations

- `POST /restaurant/bookings/` → Create reservation

---

##  Database

Models Main components:

- User
- Menu Item
- Booking

Relationships:

- A user can have multiple reservations
- Administrators manage the menu

---

##  Usage Flow

1. User registers or logs in

2. Obtains authentication token

3. Consumes protected endpoints

4. Makes reservations or views the menu

5. Admin manages system data

---

##  Installation and Execution

### 1. Clone repository

git clone https://github.com/your-repository

### 2. Create virtual environment

```bash
python -m venv env

source env/bin/activate # Linux/Mac
env\Scripts\activate # Windows
```
### 3. Install Django in the virtual machine
```bash

pip install Django
```
### 4. Installing Django Rest Framework on the Virtual Machine
```bash

pip install djangorestframework
```

### 5. Installing djoser on the Virtual Machine
```bash
pip install djoser
```

### 6. Installing MySQL on the Virtual Machine
```bash

pip install mysqlclient
```

### 7. Installing Dependencies
```bash

pip install -r requirements.txt

```

### 8. Migrations
```bash

python manage.py makemigrations
python manage.py migrate
```

### 9. Running the Server
```bash

python manage.py runserver
```

###  Testing

You can test The API using:

* Postman
* Insomnia
* cURL

##  Demonstrated Skills
* REST API Development
* Using Django REST Framework
* Authentication and Authorization
* Database Modeling
* Route and Endpoint Management
* Backend Best Practices

##  Author
```Bash
Juan Carlos Reynoso Zúñiga
```
```Bash
Back-End Developer
```
<img width="1917" height="942" alt="image" src="https://github.com/user-attachments/assets/e781922d-a4ec-40a1-8a16-735d1ce2d49b" />

<img width="1919" height="937" alt="image" src="https://github.com/user-attachments/assets/7bd55ee6-9e14-4e7c-93e1-cdec07f487a1" />



<img width="1919" height="947" alt="image" src="https://github.com/user-attachments/assets/44a9793e-c543-4a5f-91e6-4acbf72ba6a2" />

<img width="1914" height="947" alt="image" src="https://github.com/user-attachments/assets/d99948ee-8469-41c2-be1e-8dfb1cbd0cb5" />


<img width="1915" height="939" alt="image" src="https://github.com/user-attachments/assets/05474e3d-0686-43d5-8f30-8a50f6136361" />

<img width="1916" height="948" alt="image" src="https://github.com/user-attachments/assets/fb133f53-eb33-483b-8489-a00cd30aded8" />

<img width="1911" height="934" alt="image" src="https://github.com/user-attachments/assets/c3b3a4ba-ebc7-45e4-87d9-db65d71f448a" />

<img width="1919" height="954" alt="image" src="https://github.com/user-attachments/assets/076c7baa-f028-498d-83ba-af025e9f3496" />

<img width="1910" height="942" alt="image" src="https://github.com/user-attachments/assets/863d231b-2b81-4561-afb3-e99c66ba2911" />

<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/56344eb3-6417-4a9b-b49a-0ae17c1344a0" />

<img width="1915" height="950" alt="image" src="https://github.com/user-attachments/assets/802c8f9b-c0e4-49ef-bbdc-f693a912e668" />

<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/74e14c76-4576-44f4-925a-bab6ca8b1383" />

<img width="1918" height="942" alt="image" src="https://github.com/user-attachments/assets/17290527-650a-4e84-8de7-a1808c8fbeb5" />


<img width="1919" height="944" alt="image" src="https://github.com/user-attachments/assets/9e147700-cb6b-4c30-9924-7b2ba9b1c9aa" />

<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/846e27a7-28b6-4da3-a778-77eabcf49b4f" />


<img width="1919" height="945" alt="image" src="https://github.com/user-attachments/assets/eba3974c-03f4-4974-ab20-28732127e4e5" />


<img width="1919" height="939" alt="image" src="https://github.com/user-attachments/assets/7a9f285e-a30b-4c24-b05c-6a6bae633f2e" />
<img width="1919" height="952" alt="image" src="https://github.com/user-attachments/assets/9fbb59b1-e739-4f32-b902-6a72fc4d5c17" />
<img width="1919" height="947" alt="image" src="https://github.com/user-attachments/assets/7bd31d27-ae4e-422b-ab19-665c2a01cdd7" />

<img width="1918" height="946" alt="image" src="https://github.com/user-attachments/assets/edb17046-38ca-49f2-8f22-e760b0e2b5e1" />




