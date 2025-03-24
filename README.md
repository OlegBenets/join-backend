Join Backend Documentation

Overview
The Join Backend is a RESTful API built with Django and Django REST Framework (DRF) that serves as the backend for the Join Task Management application. It provides endpoints for user authentication, task management, and contact management.

Features

- User authentication with token-based login

- Management of tasks, subtasks, and contacts

- Role-based access control and permissions

- REST API endpoints for CRUD operations

Installation & Setup
To set up the Join Backend, follow these steps:

1. Clone the repository:
Download the project from GitHub using:
git clone https://github.com/OlegBenets/join-backend

2. Navigate into the project directory:
cd join-backend

3. Create and activate a virtual environment:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Run database migrations:
python manage.py migrate

6. Create a superuser (optional for admin access):
python manage.py createsuperuser

7. Start the development server:
python manage.py runserver

The API will be available at: http://127.0.0.1:8000/api/


API Endpoints
The following endpoints are available:

Authentication:

- POST /api/auth/signup/ - Register a new user

- POST /api/auth/login/ - Login and obtain an authentication token

Tasks:

- GET /api/tasks/ - Retrieve all tasks

- POST /api/tasks/ - Create a new task

- GET /api/tasks/{id}/ - Retrieve task details

- PUT /api/tasks/{id}/ - Update a task

- DELETE /api/tasks/{id}/ - Delete a task

Contacts:

- GET /api/contacts/ - Retrieve all contacts

- POST /api/contacts/ - Create a new contact

Authentication
The API uses token-based authentication. After logging in, users receive a token that must be included in the request headers:

Authorization: Token <your_token>

Project Structure

- models.py - Defines database models for tasks, subtasks, and contacts

- serializers.py - Handles data serialization

- views.py - Defines API views

- urls.py - Configures API routes

- permissions.py - Implements role-based access control

- api/ - Contains API modules

Permissions & Access Control

- Only authenticated users can manage tasks, subtasks, and contacts.

- Admin users have full access to all resources.