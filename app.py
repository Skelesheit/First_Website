import json

from flask import Flask, render_template, request

from data import db_session

from forms import Developer, CreatorVariant
from constructor import Constructor, create_task, create_author_variant

app = Flask(__name__)
app.config["SECRET_KEY"] = "SkinkinKatoonBaton"
# ЕГЭ-шка, сколько всего заданий и последнее тестовое
END_TEST_NUMBER_EGE = 11
NUMBER_EGE = 18
# ОГЭ-шка, то же самое
END_TEST_NUMBER_OGE = 19
NUMBER_OGE = 25

Constructor = Constructor(end_test_number_ege=11,
                          number_ege=18,
                          end_test_number_oge=19,
                          number_oge=25)


@app.route("/", methods=["POST", "GET"])
def show_start_template():
    return render_template("start_page.html")


# Sennin Mode
@app.route("/saninmode", methods=["GET", "POST"])
def turn_on_sanin_mod():
    loader = Developer()
    if loader.validate_on_submit():
        task = loader.task.data
        solution = loader.solution.data
        answer = loader.answer.data
        type_number = loader.type_number.data
        repeats = {task, solution, answer}
        if len(repeats) == 3 and type_number > 0:
            create_task(task=task,
                        solution=solution,
                        answer=solution,
                        type_number=type_number)
        else:
            raise Exception("Повтор имени файла, неккоретная работа!")

    return render_template("developer_mod.html", requester=loader)


# Rikudō Sennin Mode
@app.route("/rikudosaninmode", methods=["GET", "POST"])
def turn_on_rikudo_sanin_mod():
    creator = CreatorVariant()
    if creator.validate_on_submit():
        numbers = [creator.task_1.data, creator.task_2.data,
                   creator.task_3.data, creator.task_4.data,
                   creator.task_5.data, creator.task_6.data,
                   creator.task_7.data, creator.task_8.data,
                   creator.task_9.data, creator.task_9.data,
                   creator.task_10.data, creator.task_11.data,
                   creator.task_12.data, creator.task_13.data,
                   creator.task_14.data, creator.task_15.data,
                   creator.task_16.data, creator.task_17.data,
                   creator.task_18.data, creator.number_variant.data]
        create_author_variant(numbers)
    return render_template("creator_variant.html", requester=creator)


@app.route("/classes/<index>", methods=["POST", "GET"])
def choose_class(index):
    return render_template(f"{index}class.html")


@app.route("/EGE", methods=["POST", "GET"])
def show_ege():
    return render_template("EGEclass.html")


@app.route("/OGE", methods=["POST", "GET"])
def show_oge():
    return render_template("OGEclass.html")


@app.route("/vars/<index>", methods=["POST", "GET"])
def show_var(index):
    with open(f"db/vars/var{index}.json") as file:
        numbers = json.load(file)
    answer = list()
    for task in numbers:
        req = Constructor.find_number_id(numbers[task])
        answer.append(req)
    return render_template("result.html", tasks=answer,
                           mode="control", var=index)


@app.route("/end/<number_var>", methods=["POST", "GET"])
def show_results(number_var):
    with open(f"db/vars/var{number_var}.json") as file:
        numbers = json.load(file)
    answer = list()
    for task in numbers:
        req = Constructor.find_number_id(numbers[task])
        answer.append(req)
    return render_template("end.html", tasks=answer)


@app.route("/find_task", methods=["POST", "GET"])
def find_task():
    id_task = int(request.form["find_field"])
    ans = Constructor.find_number_id(id_task)
    answer = list()
    answer.append(ans)
    return render_template("result.html",
                           tasks=answer,
                           mode="find")


@app.route("/find_tasks", methods=["POST", "GET"])
def find_tasks():
    id_tasks = dict()
    for i in range(1, 20):
        id_tasks[i] = int(request.form["number_field_" + str(i)])
    answer = list(Constructor.find_numbers(id_tasks))
    return render_template("result.html",
                           tasks=answer,
                           mode="control")


@app.route("/create_var", methods=["POST", "GET"])
def create_var():
    numbers = int(request.form["create_field_var"])
    return render_template("create_new_var.html",
                           numbers=numbers)


@app.route("/save_var/<numbers>", methods=["POST", "GET"])
def save_var(numbers):
    var = dict()
    var[1] = request.form.get("field_" + str(1))
    print(var[1])
    for task_id in range(1, int(numbers) + 1):
        var[task_id] = int(request.form[f"field_{task_id}"])
    print(var)
    return render_template("EGEclass.html")


@app.route("/find_var", methods=["POST", "GET"])
def find_var():
    variant_id = int(request.form["find_field_var"])
    tasks = Constructor.find_var(variant_id)
    return render_template("result.html",
                           tasks=tasks,
                           mode="control",
                           var=variant_id)


def main():
    db_session.global_init("db/EGE.db")
    # create_test()
    app.run(debug=True)


if __name__ == "__main__":
    main()
