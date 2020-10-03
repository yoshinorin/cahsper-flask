import cahsper

from cahsper import db

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

    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'comment': self.comment,
            'created_at': self.created_at
        }

