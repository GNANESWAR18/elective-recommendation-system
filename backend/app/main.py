from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.config import CORS_ORIGINS, API_PREFIX
from app.schemas import StudentProfile, PredictResponse, HealthResponse, InfoResponse
from app.model_service import model_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Elective Recommendation API",
    description="API for recommending university electives based on student academic performance and interests",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Elective Recommendation API...")
    success = model_service.load()
    if not success:
        logger.warning("Model could not be loaded. API will return errors for prediction endpoints.")


@app.get(f"{API_PREFIX}/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="ok",
        model_loaded=model_service.is_loaded()
    )


@app.get(f"{API_PREFIX}/info", response_model=InfoResponse, tags=["Info"])
async def get_info():
    """Get model and project information."""
    if not model_service.is_loaded():
        raise HTTPException(status_code=503, detail="Model not loaded")
    return model_service.get_info()


@app.post(f"{API_PREFIX}/predict", response_model=PredictResponse, tags=["Prediction"])
async def predict(profile: StudentProfile):
    """
    Get elective recommendation for a student profile.
    """
    if not model_service.is_loaded():
        raise HTTPException(status_code=503, detail="Model not loaded. Please ensure model files exist.")
    
    try:
        student_dict = profile.model_dump()
        result = model_service.predict(student_dict)
        return PredictResponse(**result)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)