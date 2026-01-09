# Translation Web Application
## Live Demo
 [Try the live Translation Web App](https://translation-web-app-production.up.railway.app)

## Overview

This project is a Django-based web application that allows users to translate text into multiple languages and optionally generate audio using text-to-speech technology.  
It is designed as a standalone backend project and is linked from a static portfolio website.
---
## Features

- Text translation between multiple languages
- Optional audio generation (Text-to-Speech)
- Clean and responsive user interface
- Django-based backend logic
---
## Technologies Used

- Python
- Django
- deep-translator
- gTTS
- HTML / CSS
- Git & GitHub
---
## Project Structure
```text 
translation_webapp/
│
├── translation_app/                 # Django project root
│   │
│   ├── static/                       # Static assets (CSS, JS, images)
│   │
│   ├── translation_app/             # Django project configuration
│   │   ├── __init__.py
│   │   ├── settings.py              # Project settings
│   │   ├── urls.py                  # Main URL routing
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── translator/                  # Translation application module
│   │   ├── migrations/              # Database migrations
│   │   ├── templates/               # HTML templates
│   │   │   └── translator/
│   │   │       └── translation.html   # Translation UI page
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py                  # App URL routing
│   │   └── views.py                 # Translation + Text-to-Speech logic
│   │
│   ├── db.sqlite3                   # Local development database
│   ├── manage.py                    # Django management script
│   ├── requirements.txt             # Python dependencies
│   ├── README.md                    # Project documentation
│   └── .gitignore                   # Git ignored files
│
└── venv/                            # Python virtual environment (ignored by git)

```
## Installation & Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies from `requirements.txt`

## Running the Application

```bash
python manage.py runserver
```
