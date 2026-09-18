import joblib
import pandas as pd
import numpy as np

# Load model and encoder once at import
_model = joblib.load("models/elective_recommendation_model.pkl")
_encoder = joblib.load("models/label_encoder.pkl")

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

def recommend(student_dict):
    """
    student_dict: dict with keys matching FEATURE_ORDER (values numeric)
    Returns dict with:
        - top_elective
        - confidence
        - top3: list of (elective, probability)
    """
    # Build DataFrame with correct column order
    X = pd.DataFrame([student_dict])[FEATURE_ORDER]

    # Predict probabilities
    probs = _model.predict_proba(X)[0]  # shape (n_classes,)

    # Get class labels
    classes = _encoder.classes_

    # Pair and sort
    prob_pairs = list(zip(classes, probs))
    prob_pairs.sort(key=lambda x: x[1], reverse=True)

    top_elective, confidence = prob_pairs[0]
    top3 = [(cls, round(prob * 100, 1)) for cls, prob in prob_pairs[:3]]

    return {
        "top_elective": top_elective,
        "confidence": round(confidence * 100, 1),
        "top3": top3,
        "all_probs": {cls: round(prob * 100, 1) for cls, prob in prob_pairs}
    }


if __name__ == "__main__":
    # quick sanity test
    sample = {
        "programming_score": 85,
        "mathematics_score": 90,
        "database_score": 70,
        "ai_score": 88,
        "ml_score": 80,
        "web_score": 60,
        "data_science_score": 65,
        "interest_ai": 5,
        "interest_web": 2,
        "interest_data": 3,
        "interest_programming": 4,
        "interest_cloud": 2,
        "interest_security": 2
    }
    res = recommend(sample)
    print("Recommended Elective:", res["top_elective"])
    print("Confidence:", res["confidence"], "%")
    print("Top 3:")
    for i, (cls, prob) in enumerate(res["top3"], 1):
        print(f"{i}. {cls} — {prob}%")