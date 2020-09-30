import cahsper

# https://docs.python.org/3/library/dataclasses.html
# https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json/7032311
from dataclasses import dataclass
from cahsper import db

@dataclass
class Users(db.Model):
    __tablename__ = 'users'

    name: str
    created_at: int = 0

    # Non-primary-key https://teratail.com/questions/194531#reply-288604
    name = db.Column(db.String(32), name='name', primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.BigInteger(), name='created_at', unique=False, nullable=False, default=0)

    @classmethod
    def find_by_name(cls, _name: str):
        return cls.query.filter(cls.name == _name).all()

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

