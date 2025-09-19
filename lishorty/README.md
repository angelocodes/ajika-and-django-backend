# Lishorty (Link Shortener)

A Django application for shortening URLs with click tracking.

## Features

- **URL Shortening**: Convert long URLs to short, memorable links
- **Custom Slugs**: Create custom short URLs
- **Click Analytics**: Track number of clicks for each link
- **Auto-generated Slugs**: Automatic slug generation from link name

## Models

### Link
- `name`: CharField (max 100 chars, unique)
- `url`: URLField (max 200 chars, original URL)
- `slug`: SlugField (unique short identifier)
- `clicks`: PositiveIntegerField (click counter)

## Setup

1. Navigate to the project directory:
```bash
cd lishorty
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
- **Short URLs**: `http://localhost:8000/{slug}/`
- **Admin**: `http://localhost:8000/admin/`

## Tech Stack

- Django 4.0+
- HTML/CSS templates
- SQLite database
