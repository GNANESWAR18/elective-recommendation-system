import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "elective_recommendation_model.pkl"
ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

API_PREFIX = "/api"