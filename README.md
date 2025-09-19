# Ajika and Django Backend

A collection of Django backend projects showcasing various web application functionalities built with Django framework.

## Projects

### 🥗 Restaurant API
A REST API for managing restaurant menu items with CRUD operations.
- **Tech Stack**: Django, Django REST Framework
- **Features**: Menu item management, API endpoints
- **Location**: `restaurant_api/`

### 💼 Job Board
A job posting platform for companies to post jobs and job seekers to browse.
- **Tech Stack**: Django, HTML/CSS
- **Features**: Job listings, company profiles, deadline tracking
- **Location**: `job_board/`

### 🔗 Lincon (Link in Bio)
A link-in-bio application for creating personalized profile pages with multiple links.
- **Tech Stack**: Django, HTML/CSS
- **Features**: Custom profiles, background themes, link management
- **Location**: `lincon/`

### 🔗 Lishorty (Link Shortener)
A URL shortening service with click tracking.
- **Tech Stack**: Django, HTML/CSS
- **Features**: URL shortening, click analytics, custom slugs
- **Location**: `lishorty/`

### 🎬 Movie App
A movie catalog application (under development).
- **Tech Stack**: Django, HTML/CSS
- **Features**: Movie listings (planned)
- **Location**: `movie_app/`

### ✈️ Trip Planner
A travel planning application with trip notes and photo uploads.
- **Tech Stack**: Django, HTML/CSS, Image uploads
- **Features**: Trip management, notes with ratings, photo attachments
- **Location**: `trip/`

### 👶 Babysteps
A beginner's Django project for learning purposes.
- **Tech Stack**: Django
- **Features**: Basic Django setup
- **Location**: `babysteps/`

## Getting Started

### Prerequisites
- Python 3.8+
- Django 4.0+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/angelocodes/ajika-and-django-backend.git
cd ajika-and-django-backend
```

2. For each project, navigate to the project directory and install dependencies:
```bash
cd <project_name>
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

Each project follows Django's standard structure:
- `config/` - Django settings and configuration
- `<app_name>/` - Main application code
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `migrations/` - Database migrations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Angelo Codes** - [GitHub](https://github.com/angelocodes)
