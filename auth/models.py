

from pydantic import BaseModel
from db import *


class Student(Base):
    __tablename__ = "Студенты"
    tg_id = Column(String, primary_key=True)
    name = Column(String)
    group_uuid = Column (String)

class StudentRegistration(BaseModel):
    tg_id :str
    name:str
    group_uuid:str

Base.metadata.create_all(bind=engine)
