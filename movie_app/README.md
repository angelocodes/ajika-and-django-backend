# Movie App

A Django application for movie catalog and management (under development).

## Features

- **Movie Listings**: Display collection of movies
- **Movie Details**: Detailed information about each movie
- **Admin Interface**: Django admin for movie management

## Current Status

This project is in early development stages. Models and core functionality are being implemented.

## Setup

1. Navigate to the project directory:
```bash
cd movie_app
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

- **Home**: `http://localhost:8000/`
- **Admin**: `http://localhost:8000/admin/`

## Tech Stack

- Django 4.0+
- HTML/CSS templates
- SQLite database

## Future Plans

- Movie model with title, description, release date, etc.
- Image uploads for movie posters
- User ratings and reviews
- Search and filtering functionality
