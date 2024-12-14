from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import *
from db import *
import logging
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
app = FastAPI()

origins = [
    "*",
    "http://localhost",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class StudentRegistration(BaseModel):
    tg_id: str
    name: str
    group_uuid: str

@app.post("/register")
async def create_student(student: StudentRegistration, db: Session = Depends(get_db)):
    try:
        new_student = Student(
            tg_id=student.tg_id,
            name=student.name,
            group_uuid=student.group_uuid
        )
        db.add(new_student)
        db.commit()
        return JSONResponse(
            status_code=200,
            content={"message": f"Succesfully"}
        )
    except Exception as e:
        db.rollback()
        logging.error(f"Error creating student: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"message": f"Error creating student: {str(e)}"}
        )

