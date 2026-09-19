import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

from app.config import MODEL_PATH, ENCODER_PATH

logger = logging.getLogger(__name__)

FEATURE_ORDER = [
    "programming_score",
    "mathematics_score",
    "database_score",
    "ai_score",
    "ml_score",
    "web_score",
    "data_science_score",
    "interest_ai",
    "interest_web",
    "interest_data",
    "interest_programming",
    "interest_cloud",
    "interest_security"
]

TARGET_CLASSES = [
    "Artificial Intelligence",
    "Cloud Computing",
    "Cyber Security",
    "Data Science",
    "Machine Learning",
    "Web Development"
]


class ModelService:
    _instance: Optional["ModelService"] = None
    _model = None
    _encoder = None
    _loaded = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self) -> bool:
        """Load model and encoder from disk."""
        try:
            if not MODEL_PATH.exists():
                logger.error(f"Model file not found: {MODEL_PATH}")
                return False
            if not ENCODER_PATH.exists():
                logger.error(f"Encoder file not found: {ENCODER_PATH}")
                return False

            self._model = joblib.load(MODEL_PATH)
            self._encoder = joblib.load(ENCODER_PATH)
            self._loaded = True
            logger.info("Model and encoder loaded successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            self._loaded = False
            return False

    def is_loaded(self) -> bool:
        return self._loaded and self._model is not None and self._encoder is not None

    def predict(self, student_dict: Dict) -> Dict:
        """
        Make prediction for a student profile.
        Returns dict with recommended_elective, confidence, top_recommendations.
        """
        if not self.is_loaded():
            raise RuntimeError("Model not loaded")

        X = pd.DataFrame([student_dict])[FEATURE_ORDER]

        probs = self._model.predict_proba(X)[0]
        classes = self._encoder.classes_

        prob_pairs = list(zip(classes, probs))
        prob_pairs.sort(key=lambda x: x[1], reverse=True)

        top_elective, confidence = prob_pairs[0]
        top3 = [
            {"elective": cls, "probability": round(prob * 100, 1)}
            for cls, prob in prob_pairs[:3]
        ]

        return {
            "recommended_elective": top_elective,
            "confidence": round(confidence * 100, 1),
            "top_recommendations": top3
        }

    def get_info(self) -> Dict:
        """Return model information."""
        return {
            "project": "Elective Recommendation System",
            "version": "1.0.0",
            "model_type": type(self._model).__name__ if self._model else "Unknown",
            "target_classes": TARGET_CLASSES,
            "features": FEATURE_ORDER
        }


model_service = ModelService()