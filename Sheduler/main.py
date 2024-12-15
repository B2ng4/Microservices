from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import  *
from parsing_shedule import parse_shedule_on_week

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


@app.get("/get_shedule")
async def get_shedule(group_uuid: str):  # Параметр будет передан через URL
    # Здесь ваш код для обработки group_uuid
    print(group_uuid)
    shedule_on_week = (parse_shedule_on_week(group_uuid))
    return shedule_on_week











