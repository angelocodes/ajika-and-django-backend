# Babysteps

A beginner's Django project for learning Django fundamentals.

## Features

- **Basic Django Setup**: Standard Django project structure
- **Learning Project**: Designed for Django beginners
- **Admin Interface**: Default Django admin panel

## Current Status

This is a basic Django project with minimal functionality, intended as a starting point for learning Django development.

## Setup

1. Navigate to the project directory:
```bash
cd babysteps
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Start the server:
```bash
python manage.py runserver
```

## Usage

- **Home**: `http://localhost:8000/`
- **Admin**: `http://localhost:8000/admin/`

## Tech Stack

- Django 4.0+
- HTML/CSS templates
- SQLite database

## Learning Objectives

This project demonstrates:
- Django project structure
- Basic URL routing
- Template rendering
- Admin interface setup
- Database migrations
