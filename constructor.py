from data import db_session
from data.task import Task
from data.variant import Variant
from random import shuffle
import json


class Constructor:
    def __init__(self, end_test_number_ege: int,
                 number_ege: int,
                 end_test_number_oge: int,
                 number_oge: int
                 ):
        self.END_TEST_NUMBER_EGE = end_test_number_ege
        self.NUMBER_EGE = number_ege
        self.END_TEST_NUMBER_OGE = end_test_number_oge
        self.NUMBER_EGE = number_ege

    def create_variant(self):
        variant = list()
        for number in range(1, self.number_of_tasks + 1):
            print(number)

    def find_numbers(self, number_of_types: dict):
        answer = list()
        db_sess = db_session.create_session()
        for type_number in number_of_types:
            if type_number > self.NUMBER_EGE:
                raise Exception("АЧЁ такая цифра большая!?")
            request = db_sess.query(Task).filter(Task.type_number == type_number).all()
            shuffle(request)
            for i in range(number_of_types[type_number]):
                answer.append(request[i])
        return answer

    def find_number_id(self, id: int) -> 'Task':
        db_sess = db_session.create_session()
        request = db_sess.query(Task).filter(Task.id == id).first()
        return request

    def create_variant(self, numbers: list):
        pass

    def find_var(self, id: int):
        tasks = list()
        db_sess = db_session.create_session()
        request = db_sess.query(Variant).filter(Variant.id == id).first()
        with open("db/vars/" + str(request.filename), "r") as file:
            variant = json.load(file)
        for number in variant:
            task = self.find_number_id(int(variant[number]))
            tasks.append(task)

        return tasks


def create_task(task, solution, answer, type_number) -> None:
    example = Task()
    example.task = task
    example.solution = solution
    example.answer = answer
    example.type_number = type_number
    db_sess = db_session.create_session()
    db_sess.add(example)
    db_sess.commit()


def create_author_variant(examples: list) -> None:
    standart_var = examples[-1]
    tasks = dict()
    for i in range(len(examples) - 1):
        tasks[i + 1] = examples[i]
    print(tasks)
    with open("db/vars/var" + str(standart_var) + ".json", "w") as file:
        json.dump(tasks, file)
