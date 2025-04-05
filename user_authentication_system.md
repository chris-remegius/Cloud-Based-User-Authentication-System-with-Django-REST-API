
# Cloud-Based User Authentication System with Django REST API

This documentation explains the steps to set up a **Cloud-Based User Authentication System** using **Django** and **Django REST Framework** with **JWT (JSON Web Token)** authentication. The system is built to register users, authenticate them, and provide a token-based authentication for accessing protected API endpoints.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation and Setup](#installation-and-setup)
3. [Creating a Django Project](#creating-a-django-project)
4. [Install Dependencies](#install-dependencies)
5. [Configure Authentication System](#configure-authentication-system)
6. [Testing the API](#testing-the-api)
7. [Conclusion](#conclusion)

## Prerequisites
To follow this tutorial, you need:

- Python 3.8 or above
- Django 4.x
- Django REST Framework
- Djoser (for authentication)
- Postman (or any API testing tool)

## Installation and Setup

1. **Create a virtual environment** to isolate your project dependencies:

```bash
python -m venv venv
```

2. **Activate the virtual environment**:

   - On Windows:
   ```bash
   venv\Scriptsctivate
   ```

3. **Install required dependencies**:

```bash
pip install django djangorestframework djoser
```

## Creating a Django Project

1. **Start a new Django project**:

```bash
django-admin startproject cloud_auth
```

2. **Navigate to the project directory**:

```bash
cd cloud_auth
```

3. **Create a Django app** for handling the authentication logic:

```bash
python manage.py startapp core
```

4. **Add `core` and `rest_framework` to `INSTALLED_APPS`** in `cloud_auth/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Add this line
    'djoser',  # Add this line
    'core',  # Add this line
]
```

## Install Dependencies

1. Install the Django REST Framework and Djoser for easy user management:

```bash
pip install djangorestframework djoser
```

2. In `cloud_auth/settings.py`, configure the REST Framework and Djoser settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.JWTAuthentication',
    ],
}

DJOSER = {
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SEND_CONFIRMATION_EMAIL": False,
    "USER_CREATE_FIELDS": ['username', 'password', 'email'],
}
```

## Configure Authentication System

1. **Add URL patterns** in `core/urls.py`:

```python
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('api/auth/', include('djoser.urls')),  # Djoser URLs
    path('api/auth/', include('djoser.urls.jwt')),  # JWT URLs
]
```

2. **Create a basic view** for `index` in `core/views.py`:

```python
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return Response({"message": "Welcome to the User Authentication System"})
```

3. **Apply migrations** to set up the database and user model:

```bash
python manage.py migrate
```

## Testing the API

### Register a New User

#### Endpoint:
```bash
POST http://127.0.0.1:8000/api/auth/users/
```

#### Headers:
- `Content-Type: application/json`

#### Body (example):
```json
{
  "username": "testuser",
  "password": "testpassword123",
  "email": "test@example.com"
}
```

Response:

```json
{
  "username": "testuser",
  "id": 1
}
```

### Login to Get JWT Token

#### Endpoint:
```bash
POST http://127.0.0.1:8000/api/auth/jwt/create/
```

#### Headers:
- `Content-Type: application/json`

#### Body (example):
```json
{
  "username": "testuser",
  "password": "testpassword123"
}
```

Response:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOi..."
}
```

Copy the `access` token for future API calls.

### Access Protected Route

#### Endpoint:
```bash
GET http://127.0.0.1:8000/api/protected/
```

#### Headers:
- `Authorization: Bearer <your_access_token>`

Response (when token is valid):

```json
{
  "message": "Hello testuser, you're authenticated!"
}
```

## Conclusion

You have successfully set up a user authentication system with JWT in Django using Django REST Framework and Djoser. You can now easily create, login, and protect your API routes with token-based authentication.

The next steps involve adding additional user management features like password reset, email confirmation, etc., as needed.

For the full source code, check out the [GitHub Repository](https://github.com/your-username/your-repository).

---
