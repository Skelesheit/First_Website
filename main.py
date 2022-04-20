from flask import Flask, render_template, redirect, request

from data import db_session

from forms import Developer
from constructor import Constructor, create_task

db_session.global_init("db/EGE.db")
Constructor = Constructor(end_test_number_ege=11,
                          number_ege=18,
                          end_test_number_oge=19,
                          number_oge=25)
app = Flask(__name__)
app.config["SECRET_KEY"] = "skinkinkatoonbaton"


@app.route("/", methods=["POST", "GET"])
def show_base_template():
    id = 6
    ans = Constructor.find_number_id(id)
    file = 'example.jpg'
    answer = list()
    answer.append(ans)
    return render_template("result.html",
                           tasks=answer,
                           file=file,
                           mood="training",
                           constructor=Constructor)


app.run(debug=True)
