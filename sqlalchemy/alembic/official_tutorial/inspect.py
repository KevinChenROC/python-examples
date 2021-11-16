from sqlalchemy import create_engine
from sqlalchemy import inspect
db_uri = 'sqlite:///test'
engine = create_engine(db_uri)
inspector = inspect(engine)
# Get table information
print(inspector.get_table_names())