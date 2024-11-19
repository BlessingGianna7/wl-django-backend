# Wildlife Conservation System

A Django-based web application for managing wildlife conservation activities, including animal tracking, guest visits, and guide management.

## Features
- Animal Management (Add, View, Update, Delete animals)
- Guest Management (Track visitor information and visits)
- Guide Management
- Statistics Dashboard
- User Authentication
- Responsive Web Interface

## Technologies Used
- Python 3.12
- Django 5.1.2
- HTML/CSS
- Bootstrap
- SQLite Database

## Setup Instructions

1. Clone the repository

git clone https://github.com/BlessingGianna7/wl-django-backend.git

cd wildlife-conservation-django-backend


2. Create a virtual environment

bash
python -m venv django-env


3. Activate the virtual environment

## On Windows:
bash

django-env\Scripts\activate


## On macOS/Linux:

bash
source django-env/bin/activate


4. Install dependencies

pip install -r requirements.txt


5. Apply migrations

python manage.py migrate


6. Create a superuser (Admin)

python manage.py createsuperuser

7. Run the development server

python manage.py runserver


8. Access the application at `http://127.0.0.1:8000`


## Usage
- Admin Interface: `http://127.0.0.1:8000/admin/`
- Home Page: `http://127.0.0.1:8000/`
- Animals List: `http://127.0.0.1:8000/animals/`
- Guests List: `http://127.0.0.1:8000/guests/`
- Statistics: `http://127.0.0.1:8000/statistics/`

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License
