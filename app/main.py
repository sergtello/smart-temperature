from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from tinydb import Query
from app import schemas, database
from datetime import datetime, date
from typing import List
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Smart Temperature API"}


@app.get("/readings", response_model=schemas.ReadingOut, response_model_exclude_none=True)
async def get_temperature_readings():
    reading_q = Query()
    temperature_reading = database.temperature_readings_t.all()[-1]
    return temperature_reading


@app.post("/readings", response_model_exclude_none=True,
          status_code=status.HTTP_201_CREATED)
async def post_temperature_readings(temperature_reading: schemas.ReadingRequest):
    new_reading = schemas.ReadingOut(**temperature_reading.dict())
    result_insert = database.temperature_readings_t.insert(json.loads(new_reading.json()))
    return result_insert
