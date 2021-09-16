from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    
    
# "commit as you go"
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()
    
# without context manager
conn = engine.connect() 
result = conn.execute(text("select x from some_table"))
print(result.all())
conn.close()

# autocommit
with engine.begin() as conn:
    result=conn.execute(text("select * from some_table where x > :x"), {"x":1.5})
    print(result.all())
    
# ORM usage
with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y":11}, {"x": 13, "y": 15}]
    )
    session.commit()
