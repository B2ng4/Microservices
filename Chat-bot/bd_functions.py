from auth.models import Student
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
        session.close()
        return years


def get_groups(year:str):
    with Session_chat(autoflush=False, bind=engine) as session:
        query = select(Group.name).where(Group.created_at == year)
        result = session.execute(query)
        group_names = [row[0] for row in result.all()]
        session.close()
        return group_names


def get_uuid_group(group:str):
    with Session_chat(autoflush=False, bind=engine) as session:
        query = select(Group.code).where(Group.name == group)
        result = session.execute(query)
        session.close()
        return result

def check_user_exists(tg_id: str):
    with Session_chat(autoflush=False, bind=engine) as session:
        query = select(Student).where(Student.tg_id == tg_id)
        result = session.execute(query).scalar_one_or_none()
        return bool(result)



