# ⚙️ Meta Back-End Developer Capstone Project

Proyecto final del **Certificado Profesional de Desarrollador Back-End de Meta**, enfocado en el desarrollo de una API REST robusta para la gestión de reservas de restaurante.

Este proyecto demuestra habilidades en desarrollo backend utilizando **Python, Django, Django REST Framework, MySQL y autenticación basada en tokens**, siguiendo buenas prácticas de arquitectura y diseño de APIs.

---

## 🎓 Certificación

Este proyecto forma parte del programa:

**Meta Back-End Developer Professional Certificate**  
by Meta Platforms

---

## 🚀 Descripción del Proyecto

El sistema permite gestionar operaciones clave de un restaurante:

- Gestión de usuarios y autenticación
- Creación y administración de reservas
- Administración de menús
- Control de acceso basado en roles
- API REST completamente funcional

---

## 🧠 Objetivo

Construir una API backend escalable que permita:

- Manejo de datos persistentes
- Seguridad en endpoints
- Separación de responsabilidades
- Integración con clientes frontend o herramientas como Postman

---

## 🛠️ Stack Tecnológico

| Área                 | Tecnología                     |
|----------------------|-------------------------------|
| Backend             | Python                        |
| Framework           | Django                        |
| API                 | Django REST Framework         |
| Base de datos       | MySQL / SQLite                |
| Autenticación       | Token Authentication / JWT    |
| Control de versiones| Git / GitHub                  |

---

## ⚙️ Funcionalidades Principales

### 🔐 Autenticación y Autorización

- Registro de usuarios
- Login mediante token
- Protección de endpoints
- Control de acceso por roles:
  - Administrador
  - Usuario (cliente)

---

### 📋 Gestión de Menú

- Crear, editar y eliminar platillos
- Listado de productos disponibles
- Filtrado y ordenamiento

---

### 📅 Sistema de Reservas

- Crear reservas
- Validación de disponibilidad
- Consulta de reservas por usuario
- Administración de reservas (admin)

---

### 🧾 Gestión de Pedidos (Opcional)

- Crear órdenes
- Ver historial de pedidos
- Estado de pedidos

---

## 🔌 Endpoints Principales

### 🔐 Autenticación

- `POST /api/users/` → Registro  
- `POST /api/token/login/` → Login  

---

### 🍽️ Menú

- `GET /api/menu-items/` → Listar menú  
- `POST /api/menu-items/` → Crear platillo (admin)  
- `PUT /api/menu-items/{id}` → Actualizar  
- `DELETE /api/menu-items/{id}` → Eliminar  

---

### 📅 Reservas

- `GET /api/bookings/` → Listar reservas  
- `POST /api/bookings/` → Crear reserva  

---

## 🗄️ Base de Datos

Modelos principales:

- User
- MenuItem
- Booking

Relaciones:

- Un usuario puede tener múltiples reservas  
- Los administradores gestionan el menú  

---

## 🔄 Flujo de Uso

1. Usuario se registra o inicia sesión  
2. Obtiene token de autenticación  
3. Consume endpoints protegidos  
4. Realiza reservas o consulta el menú  
5. Admin gestiona datos del sistema  

---

## 🚀 Instalación y Ejecución

### 1. Clonar repositorio


git clone https://github.com/tu-repositorio


### 2. Crear entorno virtual

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```
### 3. Instalacion de django en la maquina virtual
```bash

pip install django
```
### 4. Instalacion de djangorestframework en la maquina virtual
```bash

pip install djangorestframework
```

### 5. Instalacion de djoser en la maquina virtual
```bash
pip install djoser
```

### 6. Instalacion de mysql en la maquina virtual
```bash

pip install mysqlclient
```

### 7. Instalar dependencias
```bash

pip install -r requirements.txt

```

### 8. Migraciones
```bash

python manage.py makemigrations
python manage.py migrate
```

### 9. Ejecutar servidor
```bash

python manage.py runserver
```

### 🧪 Testing

Puedes probar la API usando:

* Postman
* Insomnia
* cURL

## 📈 Habilidades Demostradas
* Desarrollo de APIs REST
* Uso de Django REST Framework
* Autenticación y autorización
* Modelado de bases de datos
* Manejo de rutas y endpoints
* Buenas prácticas de backend

## 👨‍💻 Autor
```bash
Juan Carlos Reynoso Zúñiga
```
```bash
Back-End Developer
```

<img width="1917" height="942" alt="image" src="https://github.com/user-attachments/assets/e781922d-a4ec-40a1-8a16-735d1ce2d49b" />

<img width="1919" height="937" alt="image" src="https://github.com/user-attachments/assets/7bd55ee6-9e14-4e7c-93e1-cdec07f487a1" />

<img width="1910" height="942" alt="image" src="https://github.com/user-attachments/assets/863d231b-2b81-4561-afb3-e99c66ba2911" />


<img width="1919" height="947" alt="image" src="https://github.com/user-attachments/assets/44a9793e-c543-4a5f-91e6-4acbf72ba6a2" />

<img width="1914" height="947" alt="image" src="https://github.com/user-attachments/assets/d99948ee-8469-41c2-be1e-8dfb1cbd0cb5" />

<img width="1919" height="952" alt="image" src="https://github.com/user-attachments/assets/c0911de2-04ed-4cfa-9674-6281cca0f7b5" />

<img width="1915" height="939" alt="image" src="https://github.com/user-attachments/assets/05474e3d-0686-43d5-8f30-8a50f6136361" />

<img width="1916" height="948" alt="image" src="https://github.com/user-attachments/assets/fb133f53-eb33-483b-8489-a00cd30aded8" />

<img width="1911" height="934" alt="image" src="https://github.com/user-attachments/assets/c3b3a4ba-ebc7-45e4-87d9-db65d71f448a" />

<img width="1919" height="954" alt="image" src="https://github.com/user-attachments/assets/076c7baa-f028-498d-83ba-af025e9f3496" />

<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/56344eb3-6417-4a9b-b49a-0ae17c1344a0" />

<img width="1915" height="950" alt="image" src="https://github.com/user-attachments/assets/802c8f9b-c0e4-49ef-bbdc-f693a912e668" />

<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/74e14c76-4576-44f4-925a-bab6ca8b1383" />

<img width="1918" height="942" alt="image" src="https://github.com/user-attachments/assets/17290527-650a-4e84-8de7-a1808c8fbeb5" />



