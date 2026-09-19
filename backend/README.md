# Elective Recommendation API

FastAPI backend for the Elective Recommendation System.

## Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## Run Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Health check |
| GET | /api/info | Model and project information |
| POST | /api/predict | Get elective recommendation |

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "programming_score": 70,
    "mathematics_score": 70,
    "database_score": 65,
    "ai_score": 60,
    "ml_score": 60,
    "web_score": 65,
    "data_science_score": 60,
    "interest_ai": 3,
    "interest_web": 3,
    "interest_data": 3,
    "interest_programming": 3,
    "interest_cloud": 3,
    "interest_security": 3
  }'
```

## Example Response

```json
{
  "recommended_elective": "Machine Learning",
  "confidence": 86.5,
  "top_recommendations": [
    {"elective": "Machine Learning", "probability": 86.5},
    {"elective": "Artificial Intelligence", "probability": 13.5},
    {"elective": "Data Science", "probability": 0.0}
  ]
}
```

## Model

The API uses a Logistic Regression model trained on synthetic student data (1000 samples, 13 features, 6 classes).

- Accuracy: ~91%
- Macro-F1: ~0.9071

Model files are loaded from the `models/` directory at startup.