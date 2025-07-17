# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import asyncio

app = FastAPI()

# Allow CORS if accessing from browser/frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable to store the latest simulated data
latest_data = {}

# Function to simulate data
def generate_data():
    return {
        "fuel_level_percent": round(random.uniform(0, 100), 2),
        "proximity_distance_meters": round(random.uniform(0.1, 5.0), 2),
        "seat_belt_worn": random.choice(["Yes", "No"])
    }

# Background task to keep updating data every 30 seconds
@app.on_event("startup")
async def start_simulation():
    global latest_data
    while True:
        latest_data = generate_data()
        print("Generated new data:", latest_data)
        await asyncio.sleep(30)  # wait 30 seconds before generating again

# API endpoint to get the latest data
@app.get("/generate-data")
def get_latest_data():
    return latest_data
