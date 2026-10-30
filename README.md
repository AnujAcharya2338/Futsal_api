# Futsal Booking API

A REST API for booking futsal courts, built with Django REST Framework and JWT authentication.

> **Status: In progress.** Core booking logic and login work. Permissions, payments, tests, and a frontend are planned.

## Features

- Custom user model (phone, role) with JWT login via SimpleJWT
- Futsal venue and booking endpoints; bookings require authentication
- Booking validation: opening hours, full-hour slots, supported game types (5-a-side / 7-a-side), and overlap detection (back-to-back allowed)
- Automatic `total_price` from duration and hourly rate

## Tech stack

Python, Django 6.1, Django REST Framework, SimpleJWT, django-filter, python-decouple, SQLite

## Setup

```bash
git clone https://github.com/AnujAcharya2338/Futsal_api.git
cd Futsal_api
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file next to `manage.py`:

```
SECRET_KEY=your-own-secret-key
DEBUG=True
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/token/` | Log in (returns access and refresh tokens) |
| POST | `/token/refresh/` | Refresh the access token |
| GET, POST | `/futsal/` | List or create venues |
| GET, POST | `/booking/` | List or create bookings (login required) |

Send the token as `Authorization: Bearer <access-token>`. Detail routes (`/futsal/<id>/`, `/booking/<id>/`) are also available.

## Roadmap

- [] Users manage only their own bookings; role-based permissions
- [] Registration endpoint
- [] Tests for booking validation
- [] Availability endpoint and filtering
- [] Payments (Khalti, eSewa)
