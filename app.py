from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET"])
def homepage():
    return render_template("todolist.html", tasks=tasks)

@app.route("/", methods=["POST"])
def addtask():
    task = request.form.get("txtTask")
    tasks.append(task)
    return redirect(url_for("homepage"))

if __name__=="__main__":
    app.run(debug=True)