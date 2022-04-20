from constructor import Constructor
from data import db_session

db_session.global_init("db/EGE.db")
Constructor = Constructor(end_test_number_ege=11,
                          number_ege=18,
                          end_test_number_oge=19,
                          number_oge=25)
L = {
    4: 1,
    8: 1
}
ans = Constructor.find_numbers(L)
for task in ans:
    filename_task = task.task
    filename_solution = task.solution
    filename_answer = task.answer
    print(filename_answer, filename_solution, filename_answer)
print("========")
answer = Constructor.find_number_id(id=4)
print(answer.task, answer.answer)
