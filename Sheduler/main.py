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










