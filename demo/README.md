# Django REST Product API

A backend REST API built using Django and Django REST Framework with JWT authentication.
This project demonstrates secure APIs, authentication, and clean backend structure.

---

## 🚀 Features
- JWT Authentication (Access & Refresh tokens)
- Secure API endpoints
- Product CRUD operations
- Django Admin panel
- Clean, internship-ready backend project

---

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development database)

---

## 📂 Project Structure
demo/
│
├── demo/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
│
├── myapp/
│ ├── migrations/
│ ├── admin.py
│ ├── api_views.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ ├── views.py
│
├── manage.py
├── db.sqlite3
├── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment
```bash
python -m venv venv

2️⃣ Activate virtual environment (Windows)
venv\Scripts\activate

3️⃣ Install dependencies
pip install django djangorestframework djangorestframework-simplejwt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver

🔐 Authentication (JWT)
Get token
POST /api/token/


Request body:

{
  "username": "your_username",
  "password": "your_password"
}

Use token in requests

Add header:

Authorization: Bearer <access_token>

📡 API Endpoints
Method	Endpoint	Description
POST	/api/token/	Get JWT token
POST	/api/token/refresh/	Refresh token
GET	/api/products/	List products
POST	/api/products/	Create product
PUT	/api/products/{id}/	Update product
DELETE	/api/products/{id}/	Delete product
