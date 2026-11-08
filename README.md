
# SWYNEX Database and CRUD API

A task management REST API built using Python, FastAPI, SQLite, and SQLAlchemy as part of the SWYNEX Backend Developer Internship.

## Features

- Create new tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update existing tasks
- Delete tasks
- Persistent SQLite database storage
- SQLAlchemy ORM integration
- Request validation using Pydantic
- Automatic interactive API documentation with Swagger UI
- HTTP error handling for tasks that do not exist

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
SWYNEX-Database-and-CRUD/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/komalkowshikkanuri-dotcom/SWYNEX-Database-and-CRUD.git

cd SWYNEX-Database-and-CRUD
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## API Documentation

Interactive Swagger documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Health check |
| POST | /tasks/ | Create a task |
| GET | /tasks/ | Retrieve all tasks |
| GET | /tasks/{task_id} | Retrieve a task by ID |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Sample Request

### Create a Task

POST /tasks/

Request body:

```json
{
  "title": "Learn FastAPI",
  "description": "Complete SWYNEX Task 2",
  "completed": false
}
```

Example response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete SWYNEX Task 2",
  "completed": false
}
```

## Database

The application uses SQLite for persistent data storage.

SQLAlchemy manages database interactions through an ORM.

The database file `tasks.db` is created locally when the application starts and is excluded from version control.

## Validation and Error Handling

- Task titles must contain between 1 and 100 characters.
- Missing tasks return HTTP 404.
- Invalid request data returns HTTP 422.
- Successful creation returns HTTP 201.
- Successful deletion returns HTTP 204.

## Learning Outcomes

- Integrating FastAPI with a relational database.
- Working with SQLAlchemy ORM.
- Implementing RESTful CRUD operations.
- Validating API requests using Pydantic.
- Managing database sessions.
- Testing APIs through Swagger UI.

## Internship

Developed as part of Task 2: Database and CRUD, under the Backend Developer Internship at SWYNEX Technologies.
