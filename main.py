# filename: main.py
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/generate-data")
def generate_data():
    data = {
        "fuel_level_percent": round(random.uniform(0, 100), 2),         # 0% to 100%
        "proximity_distance_meters": round(random.uniform(0.1, 5.0), 2),# 0.1m to 5m
        "seat_belt_worn": random.choice(["Yes", "No"])                  # Yes or No
    }
    return data
