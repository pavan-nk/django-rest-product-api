# Django REST Product API (JWT Authentication)

This is a backend-only REST API built with Django and Django REST Framework.
The project is deployed live on Render.

---

## Live Base URL

https://django-rest-product-api.onrender.com

Note: This is an API backend. Opening the root URL (/) will return 404.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- Gunicorn
- Render (Deployment)

---

## Authentication (JWT)

### Step 1: Get Token

POST /api/token/

Request Body:
{
  "username": "your_username",
  "password": "your_password"
}

Response:
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}

---

### Step 2: Access Protected APIs

GET /api/products/

Headers:
Authorization: Bearer JWT_ACCESS_TOKEN

If token is missing, API returns:
Authentication credentials were not provided

---

## Features

- Secure JWT authentication
- Protected REST endpoints
- CRUD operations for products
- Production deployment with Gunicorn
- Environment-based configuration

---

## Deployment

The application is deployed on Render using:

gunicorn demo.wsgi:application

---

## Status

Live and working
