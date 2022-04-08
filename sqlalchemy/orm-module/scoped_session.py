# set up a scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

some_engine = create_engine('sqlite:///:memory:', echo=True)
session_factory = sessionmaker(bind=some_engine)
Session = scoped_session(session_factory)

# now all calls to Session() will create a thread-local session
some_session = Session()
# call again to get the same session
another_session = Session() 

print(some_session is another_session)

# you can now use some_session to run multiple queries, etc.

# remember to close it when you're finished!
Session.remove()

# you get a different thread-local session after calling remove
another_session = Session()
print(some_session is another_session)