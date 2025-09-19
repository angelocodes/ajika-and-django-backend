# Job Board

A Django web application for job postings and company listings.

## Features

- **Job Postings**: Create and manage job listings
- **Company Profiles**: Associate jobs with companies
- **Deadline Tracking**: Set application deadlines
- **Active/Inactive Status**: Control job visibility
- **Admin Interface**: Django admin for management

## Models

### JobPosting
- `title`: CharField (max 200 chars)
- `description`: TextField
- `company`: CharField (max 100 chars)
- `salary`: IntegerField
- `deadline`: DateField (default: today)
- `is_active`: BooleanField (default: False)

## Setup

1. Navigate to the project directory:
```bash
cd job_board
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
