
# 📑 Task Manager REST API
This is the solution for the ByteCraft Club Backend challenge
which is RESTful API for managing tasks. Users are be able to perform basic operations like creating, updating, deleting, and listing tasks. The project includes authentication using simpleJWT 3rd-party package for Django REST Framework and authorization to ensure that users can only access and manipulate their tasks.

## ⏬ Features

- User Registration and Authentication: Users should be able to register, log in, and receive an authentication token for secure API access.

- Task Management:
   - Create a new task.
   - Update an existing task
   - Delete a task.
   - Retrieve a list of tasks associated with the authenticated user.

- Authorization:
   - Users should only be able to manage their own tasks.


## 🚀 Run Locally

Clone the project

```bash
  git clone https://github.com/Chouaib-Djerdi/ByteCraft-Backend-Solution
```

Go to the project directory

```bash
  cd task_manager
```

Install dependecies

```bash
  pip install -r requirements.txt
```

Make Migrations

```bash
  python manage.py makemigrations
```

Migrate

```bash
  python manage.py migrate
```

Start Server

```bash
  python manage.py runserver
```

