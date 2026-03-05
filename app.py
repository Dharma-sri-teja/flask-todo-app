from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

todos = []

html = """
<h2>My To-Do List</h2>

<form method="POST">
<input type="text" name="task" placeholder="Enter task">
<input type="submit" value="Add Task">
</form>

<ul>
{% for task in todos %}
<li>{{task}}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        task = request.form["task"]
        todos.append(task)
        return redirect(url_for("home"))
    return render_template_string(html, todos=todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)