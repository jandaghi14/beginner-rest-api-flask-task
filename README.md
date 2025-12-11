# Flask Task Management REST API

A beginner-level REST API built with Flask that demonstrates full CRUD operations for task management.

## Features

- **CREATE**: Add new tasks with titles
- **READ**: Retrieve all tasks
- **UPDATE**: Change task completion status
- **DELETE**: Remove tasks by ID

## Technologies Used

- Python 3
- Flask
- In-memory data storage

## API Endpoints

### Get All Tasks
```
GET /api/tasks
```

### Create New Task
```
POST /api/tasks
Content-Type: application/json

{
  "title": "Task name"
}
```

### Update Task Status
```
PUT /api/tasks/<id>
Content-Type: application/json

{
  "completed": true
}
```

### Delete Task
```
DELETE /api/tasks/<id>
```

## How to Run

1. Install Flask:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

3. Server runs on: `http://127.0.0.1:5000`

## Testing with curl

**Get all tasks:**
```bash
curl http://127.0.0.1:5000/api/tasks
```

**Create a task:**
```bash
curl -X POST http://127.0.0.1:5000/api/tasks -H "Content-Type: application/json" -d "{\"title\": \"Buy groceries\"}"
```

**Update task:**
```bash
curl -X PUT http://127.0.0.1:5000/api/tasks/1 -H "Content-Type: application/json" -d "{\"completed\": true}"
```

**Delete task:**
```bash
curl -X DELETE http://127.0.0.1:5000/api/tasks/2
```

## What I Learned

- Building REST APIs with Flask
- HTTP methods (GET, POST, PUT, DELETE)
- JSON request/response handling
- API routing and URL parameters
- Testing APIs with curl
- Professional API design patterns

## Future Improvements

- Add database persistence (SQLite)
- Implement user authentication
- Add data validation
- Deploy to production server