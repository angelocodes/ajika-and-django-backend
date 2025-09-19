# Restaurant API

A Django application for managing restaurant menu items with both Django REST Framework API endpoints and custom JSON responses.

## Features

- **Menu Item Management**: Create, read, update, and delete menu items
- **RESTful API**: JSON-based API endpoints
- **Admin Interface**: Django admin panel for easy management
- **Web UI**: Simple web interface for viewing menu items

## Models

### Item
- `name`: CharField (max 250 chars)
- `description`: TextField
- `price`: IntegerField

## API Endpoints

- `GET /` - List all menu items (DRF Response)
- `GET /serialized/` - List all menu items (JSON Response)
- `GET /detail/<int:pk>/` - Get specific menu item by ID
- `GET /ui/` - Web UI for viewing menu items

## Setup

1. Navigate to the project directory:
```bash
cd restaurant_api
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

4. Start the server:
```bash
python manage.py runserver
```

## Usage

- **API List**: `http://localhost:8000/` (DRF JSON response)
- **API Serialized**: `http://localhost:8000/serialized/` (Custom JSON response)
- **Item Detail**: `http://localhost:8000/detail/{id}/`
- **Web UI**: `http://localhost:8000/ui/`
- **Admin**: `http://localhost:8000/admin/`

## Tech Stack

- Django 4.0+
- Django REST Framework
- SQLite (default database)
