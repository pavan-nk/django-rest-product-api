# Django REST Product API

A backend-only REST API built using Django and Django REST Framework with JWT authentication.
The project is deployed live on Render.

---

## 🚀 Features

- JWT-based authentication (login & protected APIs)
- Secure, token-protected endpoints
- CRUD APIs for product management
- User-specific data access
- Production deployment using Gunicorn
- Environment-based configuration

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite (development)
- Gunicorn
- Render (Deployment)

---

## 🔐 Authentication Flow (JWT)

### Step 1: Obtain Access Token

**POST**
/api/token/

css
Copy code

Request body (JSON):
{
"username": "your_username",
"password": "your_password"
}

makefile
Copy code

Response:
{
"access": "JWT_ACCESS_TOKEN",
"refresh": "JWT_REFRESH_TOKEN"
}

yaml
Copy code

---

### Step 2: Access Protected Endpoints

Add the token in request headers:

Authorization: Bearer JWT_ACCESS_TOKEN

cpp
Copy code

Example protected endpoint:

GET /api/products/

python
Copy code

If token is missing or invalid, the API returns:
Authentication credentials were not provided.

yaml
Copy code

---

## 📦 API Endpoints

- POST `/api/token/` — get JWT token
- GET `/api/products/` — list products (protected)
- POST `/api/products/` — create product (protected)

---

## 🌍 Live Deployment

Base URL:
https://django-rest-product-api.onrender.com

yaml
Copy code

Note: This is an API-only backend. The root URL (`/`) may return 404, which is expected.

---

## 📁 Project Purpose

This project demonstrates backend development skills including:
- REST API design
- Authentication & authorization
- Secure deployment
- Real-world production debugging

---

## 👤 Author

Pavan
