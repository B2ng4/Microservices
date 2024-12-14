from db import *
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import select, distinct
from models import Group

def get_db():
    db = Session_chat()
    try:
        yield db
    finally:
        db.close()



def get_unique_years():
    with Session_chat(autoflush=False, bind=engine) as session:
        query = select(distinct(Group.created_at)).order_by(Group.created_at.desc())
        result = session.execute(query)
        years = result.scalars().all()
        return years

print(get_unique_years())