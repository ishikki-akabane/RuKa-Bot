from RUKA.database.sql import BASE, Session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, unique=True)

    def __init__(self, user_id):
        self.user_id = user_id
