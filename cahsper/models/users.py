import cahsper

from typing import List, Optional
from cahsper import db

class Users(db.Model):
    __tablename__ = 'users'

    name: str
    created_at: int = 0

    # Non-primary-key https://teratail.com/questions/194531#reply-288604
    name = db.Column(db.String(32), name='name', primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.BigInteger(), name='created_at', unique=False, nullable=False, default=0)

    @classmethod
    def find_by_name(cls, _name: str) -> Optional['Users']:
        return cls.query.filter(cls.name == _name).one_or_none()

    @classmethod
    def get_all(cls) -> List['Users']:
        return db.session.query(cls).all()

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'created_at': self.created_at
        }

