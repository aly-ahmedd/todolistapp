from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    """Retrieve all tasks from the database and render the home page."""
    tasks = Task.query.all()  # Retrieve all tasks from the database
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task to the database."""
    task_content = request.form.get('task')
    if task_content:
        new_task = Task(content=task_content)  # Create a new task
        db.session.add(new_task)  # Add the task to the database
        db.session.commit()  # Commit the changes
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task from the database by ID."""
    task = Task.query.get_or_404(task_id)  # Retrieve the task by ID
    db.session.delete(task)  # Delete the task from the database
    db.session.commit()  # Commit the changes
    return redirect(url_for('index'))

# Route to edit a task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Edit an existing task in the database."""
    task = Task.query.get_or_404(task_id)  # Retrieve the task by ID
    if request.method == 'POST':
        task.content = request.form.get('task')  # Update the task content
        db.session.commit()  # Commit the changes
        return redirect(url_for('index'))
    return render_template('index.html', tasks=Task.query.all(), edit_task=task)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)