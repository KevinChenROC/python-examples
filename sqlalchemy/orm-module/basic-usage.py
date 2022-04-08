from sqlalchemy import Column, Integer, String, text
from sqlalchemy.sql.expression import or_
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import Session, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
session.add(User(name='ed', fullname='Ed Jones', nickname='edsnickname'))
session.add(User(name='kevin', fullname='Kevin Chen', nickname='kchen'))
session.add(User(name='Bon', fullname='Bon Bon', nickname='BB'))
session.commit()


# basic query usage
query = session.query(User)
kevin = query.filter(User.name == "kevin").first()
print(kevin)
kevin.name='KEVIN'
session.commit()
# re-query the DB because kevin.name is changed.
print(kevin)

# for row in query.filter(or_(User.name == "kevin", User.name == "Bon")):
#     print(row)

# for row in query.order_by(text('id')):
#     print(row)

# for row in query.order_by(User.id):
#     print(row)
