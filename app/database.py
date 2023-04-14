from tinydb import TinyDB, Query
from app import schemas

db = TinyDB('storage/database.json')
temperature_readings_t = db.table("TemperatureReadings")
