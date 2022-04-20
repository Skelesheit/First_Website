import sqlalchemy as db
from .db_session import SqlAlchemyBase


class Variant(SqlAlchemyBase):
    __tablename__ = "variants"
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    filename = db.Column(db.String, unique=True, nullable=False)
