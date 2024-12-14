from sqlalchemy.dialects.postgresql import UUID
from db import *


class Group(Base):
    __tablename__ = 'Группы'
    __table_args__ = {'extend_existing': True}

    code = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    created_at = Column(Integer)

