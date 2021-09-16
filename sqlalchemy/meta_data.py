from sqlalchemy import MetaData, create_engine
from sqlalchemy.sql.expression import insert, select, update,text
from sqlalchemy.sql.functions import user
from sqlalchemy.util.langhelpers import _update_argspec_defaults_into_env

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
metadata_obj = MetaData()

from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

from sqlalchemy import ForeignKey
address_table = Table(
    "address",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False)
)

metadata_obj.create_all(engine)

insert_stmt = insert(user_table).values(name="patrick", fullname="patrick chen")
update_stmt = update(user_table).values(fullname="Username: " + user_table.c.name)
select_stmt = select(user_table).where(user_table.c.name == "patrick")

with engine.begin() as conn:
    conn.execute(insert_stmt)
    conn.execute(update_stmt)
    result = conn.execute(select_stmt)
    print(result.all())


