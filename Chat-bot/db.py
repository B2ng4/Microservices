from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus



DATABASE_URL = f'postgresql://timofey:12345678A@188.225.35.151:5432/vezdeChifra'

engine = create_engine(DATABASE_URL)
Session_chat = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
