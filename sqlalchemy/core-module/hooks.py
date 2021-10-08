from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


url = "sqlite:///:memory:"
engine = create_engine(url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


@event.listens_for(User, "before_insert")
def before_insert(mapper, connection, user):
    print(f"before insert: {user.name}")


@event.listens_for(User, "after_insert")
def after_insert(mapper, connection, user):
    print(f"after insert: {user.name}")


try:
    session = scoped_session(Session)
    user = User(name="bob", age=18)
    session.add(user)
    session.commit()
except SQLAlchemyError as e:
    session.rollback()
finally:
    session.close()
