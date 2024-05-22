Certainly! Here's a complete README file for your GitHub repository:

```markdown
# Recipe API

## Overview
 Recipe API is a recipe sharing platform built using Django Rest Framework (DRF). It provides a set of RESTful APIs for managing recipes, user profiles, authentication, and more.

## Features
- CRUD operations for recipes
- User authentication (register, login, logout)
- User profile management (view profile, update profile, change password)
- Email notification queue for recipe likes
- Pagination for list APIs
- Integration with Celery for asynchronous task handling
- Docker support for containerization

## Installation
```
1. Clone the repository:
   ```bash
   git clone https://github.com/anjanprasad112/recipe-api.git
   ```

2. Install dependencies:
   ```bash
   cd recipe-api
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
OR
2. Create a `.env` file in the root directory and add your environment variables:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase
   # Add other environment variables as needed
   ```

3. Build and start the Docker containers:
   ```bash
   docker-compose up --build

## Usage
1. Run the development server:
   ```bash
   python manage.py runserver
   ```
2. Access the API documentation at [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/) to explore available endpoints and schemas.

## Configuration
- Database settings: Configure your database settings in `settings.py`.
- Email settings: Configure your email backend settings in `settings.py`.
- Celery settings: Configure Celery settings in `settings.py`.
- Environment variables: Set environment variables for sensitive data such as database credentials, email credentials, etc.

## Testing
- Run tests using:
  ```bash
  python manage.py test
  ```

