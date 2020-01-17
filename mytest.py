from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

notes = []

# @app.route('/hh2', methods = ["POST"])
# def hh2():
#     name = request.form.get("name")
#     return render_template("hh2.html", name = name)

@app.route('/',  methods = ["POST", "GET"])
def hh():
    note = request.form.get("name")
    print(note)
    notes.append(note)
    return render_template("hh.html", notes = notes)


    