import sqlalchemy
from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = "tasks"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    task = sqlalchemy.Column(sqlalchemy.String, unique=True)
    solution = sqlalchemy.Column(sqlalchemy.String, unique=True)
    answer = sqlalchemy.Column(sqlalchemy.String, unique=True)
    type_number = sqlalchemy.Column(sqlalchemy.Integer, index=True, nullable=False)

