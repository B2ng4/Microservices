
from db import *

class Group(Base):
    __tablename__ = 'Группы'
    __table_args__ = {'extend_existing': True}

    code = Column(String, primary_key=True)
    name = Column(String)
    created_at = Column(Integer)

class Student(Base):
    __tablename__ = 'Студенты'
    __table_args__ = {'extend_existing': True}

    tg_id = Column(String, primary_key=True)
    name = Column(String)
    group_uuid = Column(String)

