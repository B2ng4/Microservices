from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import asyncio
import logging
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from video_url_get import search_videos_by_discipline

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


@app.get("/get_video_urls")
def get_videos(discipline: str):
    urls = search_videos_by_discipline(discipline)
    return JSONResponse(content={"videos": urls})

