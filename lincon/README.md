# Lincon (Link in Bio)

A Django application for creating personalized link-in-bio profile pages.

## Features

- **Custom Profiles**: Create unique profile pages with custom slugs
- **Multiple Links**: Add multiple links to each profile
- **Background Themes**: Choose from blue, green, or yellow backgrounds
- **Clean UI**: Simple and responsive design

## Models

### Profile
- `name`: CharField (max 100 chars)
- `slug`: SlugField (unique URL identifier)
- `bg_color`: CharField (choices: blue, green, yellow)

### Link
- `text`: CharField (max 200 chars, display text)
- `url`: URLField (target URL)
- `profile`: ForeignKey to Profile

## Setup

1. Navigate to the project directory:
```bash
cd lincon
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
- **Profile URLs**: `http://localhost:8000/{slug}/`
- **Admin**: `http://localhost:8000/admin/`

## Tech Stack

- Django 4.0+
- HTML/CSS templates
- SQLite database
