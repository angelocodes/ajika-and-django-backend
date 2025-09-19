# Trip Planner

A Django application for planning and documenting travel experiences.

## Features

- **Trip Management**: Create and manage travel itineraries
- **Trip Notes**: Add detailed notes for each trip
- **Photo Uploads**: Attach images to trip notes
- **Rating System**: Rate trip experiences (1-5 stars)
- **User Authentication**: Personal trip planning
- **Activity Types**: Categorize notes by activity type

## Models

### Trip
- `city`: CharField (max 100 chars)
- `country`: CharField (max 2 chars, country code)
- `start_date`: DateField
- `end_date`: DateField
- `owner`: ForeignKey to User

### Note
- `trip`: ForeignKey to Trip
- `name`: CharField (max 200 chars)
- `description`: TextField
- `type`: CharField (choices: sightseeing, hiking, beach, etc.)
- `img`: ImageField (uploaded to 'notes/')
- `rating`: PositiveSmallIntegerField (1-5)

## Setup

1. Navigate to the project directory:
```bash
cd trip
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
- **Login**: `http://localhost:8000/accounts/login/`

## Tech Stack

- Django 4.0+
- HTML/CSS templates
- Image uploads
- User authentication
- SQLite database
