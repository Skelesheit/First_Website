from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class Developer(FlaskForm):
    task = StringField("Условие", validators=[DataRequired()])
    solution = StringField("Решение", validators=[DataRequired()])
    answer = StringField("Ответ", validators=[DataRequired()])
    type_number = IntegerField("номер задания", validators=[DataRequired()])
    submit = SubmitField("Отослать")


class CreatorVariant(FlaskForm):
    number_variant = IntegerField("вариант", validators=[DataRequired()])
    task_1 = IntegerField("номер 1", validators=[DataRequired()])
    task_2 = IntegerField("номер 2", validators=[DataRequired()])
    task_3 = IntegerField("номер 3", validators=[DataRequired()])
    task_4 = IntegerField("номер 4", validators=[DataRequired()])
    task_5 = IntegerField("номер 5", validators=[DataRequired()])
    task_6 = IntegerField("номер 6", validators=[DataRequired()])
    task_7 = IntegerField("номер 7", validators=[DataRequired()])
    task_8 = IntegerField("номер 8", validators=[DataRequired()])
    task_9 = IntegerField("номер 9", validators=[DataRequired()])
    task_10 = IntegerField("номер 10", validators=[DataRequired()])
    task_11 = IntegerField("номер 11", validators=[DataRequired()])
    task_12 = IntegerField("номер 12", validators=[DataRequired()])
    task_13 = IntegerField("номер 13", validators=[DataRequired()])
    task_14 = IntegerField("номер 14", validators=[DataRequired()])
    task_15 = IntegerField("номер 15", validators=[DataRequired()])
    task_16 = IntegerField("номер 16", validators=[DataRequired()])
    task_17 = IntegerField("номер 17", validators=[DataRequired()])
    task_18 = IntegerField("номер 18", validators=[DataRequired()])
    create_var = SubmitField("Отослать")
