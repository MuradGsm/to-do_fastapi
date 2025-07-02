# To-Do FastAPI Project

## Description
A simple asynchronous REST API for managing tasks (To-Do list) built with FastAPI, SQLAlchemy (async), PostgreSQL, and JWT authentication.

## Features
- User registration and authentication with JWT
- CRUD operations for tasks
- Тasks are linked to specific users
- Filtering tasks by status (completed / not completed)
- Asynchronous database operations
- Proper error handling and access control

## Technologies
- Python 3.11+
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Alembic (for database migrations)
- Docker & Docker Compose

## Getting Started

### 1. Clone the repository
git clone <your-repository-url>
cd to-do-fastapi

### 2. Create a .env file in the project root with your environment variables (example):
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/todo_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 3. Build and run Docker containers
docker-compose up --build

### 4. Run database migrations
docker-compose exec api alembic upgrade head

### 5. Open API docs in your browser
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure
- /app/models/ — SQLAlchemy ORM models
- /app/schemas/ — Pydantic models for request/response validation
- /app/service/ — Business logic and services
- /app/routers/ — FastAPI route definitions
- /app/utils/ — Utility functions
- /app/alembic/ — Database migration scripts
