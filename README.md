Flask Task Manager

A simple web application built with Flask to demonstrate core backend fundamentals — routing, templates, form handling, and basic data storage. Built as part of the Alfido Tech Python Developer Track (Task 4: Flask Mini Project).

## Features

- View all tasks on a clean home page
- Add new tasks via a form (GET & POST handling)
- Delete tasks
- Styled with Bootstrap for a clean UI
- In-memory data storage (no database required)

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Jinja2 templates, Bootstrap 5
- **Storage:** In-memory Python list

## Project Structure

```
flask_mini_project/
│
├── app.py                 # Main Flask application (routes & logic)
├── templates/
│   ├── index.html          # Home page — displays task list
│   └── add.html            # Form page — add a new task
└── README.md
```

## Routes

| Route            | Method    | Description                          |
|-------------------|-----------|---------------------------------------|
| `/`               | GET       | Displays the home page with all tasks |
| `/add`            | GET, POST | Shows the add-task form / saves a new task |
| `/delete/<task_id>` | GET     | Deletes a task by its index           |

## Getting Started

### Prerequisites
- Python 3.x installed
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/eswarprasadreddy/flask-task-manager.git
cd flask-task-manager
```

2. Install Flask
```bash
pip install flask
```

3. Run the app
```bash
python app.py
```

4. Open your browser and go to:
```
http://127.0.0.1:5000
```

## How It Works

- The home route (`/`) renders `index.html`, looping through the `tasks` list using Jinja2 templating.
- The `/add` route handles both displaying the form (`GET`) and processing the submission (`POST`) — a common Flask pattern for forms.
- Task deletion is handled by index, wrapped in a try-except block to avoid errors if an invalid ID is requested.
- Bootstrap is loaded via CDN for styling, so no extra CSS setup is needed.

## Notes

- Data is stored in memory, so the task list resets every time the server restarts. This keeps the project simple and focused on demonstrating Flask fundamentals rather than database integration.
- This project was built as part of a learning track and is intended as a demonstration of Flask basics (routing, templates, forms).

## Author

Eshwar
