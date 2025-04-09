# To-Do List Web Application

## Overview
This project is a simple and intuitive web application designed to help users organize their tasks efficiently and improve productivity. The application is accessible from any device with a web browser.

## Features
- Add, edit, and delete tasks
- Responsive design for different screen sizes
- Accessible from any device with a web browser

## Technologies Used
### Front-End
- **HTML**: Structure of the web pages
- **CSS**: Styling of the web pages
- **JavaScript**: Adding dynamic behavior to the web pages
- **Jinja2 Templating**: Rendering dynamic content in HTML

### Back-End
- **Flask**: Micro web framework for Python
- **SQLite**: Lightweight database for storing tasks
- **SQLAlchemy**: ORM (Object-Relational Mapping) library for interacting with the SQLite database

## Installation Instructions
### Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy

### Steps
1. **Clone the repository**:
    ```bash
    git clone <[repository-url](https://github.com/aly-ahmedd/todolistapp.git)>
    cd todo-list-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000`

## Usage
### Adding a Task
- Enter the task in the input field and click the "Add Task" button.

### Editing a Task
- Click the "Edit" link next to the task, modify the content, and click "Update Task".

### Deleting a Task
- Click the "Delete" link next to the task.

## Test Cases
### Example Test Case
1. **Action**: Click on the "Add Task" button after entering a task.
   - **Expected Result**: The task is added to the list and displayed on the home page.

2. **Action**: Click on the "Edit" link next to a task, modify the content, and click "Update Task".
   - **Expected Result**: The task content is updated and displayed on the home page.

3. **Action**: Click on the "Delete" link next to a task.
   - **Expected Result**: The task is removed from the list and no longer displayed on the home page.

## Screenshots
### Home Page
!Home Page

### Add Task
!Add Task

### Edit Task
!Edit Task

### Delete Task
!Delete Task

## Screencast
A short screencast demonstrating the application can be found in [other document in](https://atlas.pebblepad.co.uk/atlasspa/#/viewer/3361129/17424526780000000/38rHfM7zph7WmfH6HG4zn3gmxM?historyId=BUC2yblTgG&navId=F12D2AEC1ABAB99EA6E5505DC424190F) pebblepad.

## Lessons Learned
- Importance of responsive design for accessibility
- Effective use of Flask and SQLAlchemy for web development
- Value of thorough documentation and testing

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please contact [Aly Ahmed] at [aly.ahmed@iu-study.org].

