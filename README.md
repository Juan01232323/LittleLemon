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

### 4. Instalacion de djoser en la maquina virtual
```bash
pip install djoser
```

### 4. Instalacion de mysql en la maquina virtual
```bash

pip install mysqlclient
```

### 4. Instalar dependencias
```bash

pip install -r requirements.txt

```

### 5. Migraciones
```bash

python manage.py makemigrations
python manage.py migrate
```

### 6. Ejecutar servidor
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
