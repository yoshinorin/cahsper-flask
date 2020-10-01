import cahsper

# https://docs.python.org/3/library/dataclasses.html
# https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json/7032311
from dataclasses import dataclass
from cahsper import db

@dataclass
class Comments(db.Model):
    __tablename__ = 'comments'

    id: int = 0
    user_name: str
    comment: str
    created_at: int = 0

    id = db.Column(db.BigInteger(), name='id', primary_key=True, unique=True, nullable=False)
    user_name = db.Column(db.String(32), name='user_name', unique=False, nullable=False) #, db.ForeignKey('users.name')
    comment = db.Column(db.String(255), name='comment', unique=False, nullable=False)
    created_at = db.Column(db.BigInteger(), name='created_at', unique=False, nullable=False, default=0)

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

