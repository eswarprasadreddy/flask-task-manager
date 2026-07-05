from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (list) acting as our simple "database"
tasks = []

# ---------- HOME PAGE (GET) ----------
@app.route("/")
def home():
    """Displays the home page with the current list of tasks."""
    return render_template("index.html", tasks=tasks)


# ---------- ADD TASK (GET form + POST submit) ----------
@app.route("/add", methods=["GET", "POST"])
def add_task():
    """GET: shows the form. POST: adds the submitted task to the list."""
    if request.method == "POST":
        task_name = request.form.get("task_name")
        if task_name:  # basic validation
            tasks.append(task_name)
        return redirect(url_for("home"))
    return render_template("add.html")


# ---------- DELETE TASK ----------
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Deletes a task by its index in the list, with error handling."""
    try:
        tasks.pop(task_id)
    except IndexError:
        pass  # task already removed or invalid id, just ignore
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)