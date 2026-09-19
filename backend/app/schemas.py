from pydantic import BaseModel, Field
from typing import List, Optional


class StudentProfile(BaseModel):
    programming_score: int = Field(..., ge=0, le=100, description="Programming score (0-100)")
    mathematics_score: int = Field(..., ge=0, le=100, description="Mathematics score (0-100)")
    database_score: int = Field(..., ge=0, le=100, description="Database score (0-100)")
    ai_score: int = Field(..., ge=0, le=100, description="AI score (0-100)")
    ml_score: int = Field(..., ge=0, le=100, description="ML score (0-100)")
    web_score: int = Field(..., ge=0, le=100, description="Web Development score (0-100)")
    data_science_score: int = Field(..., ge=0, le=100, description="Data Science score (0-100)")
    interest_ai: int = Field(..., ge=1, le=5, description="AI interest (1-5)")
    interest_web: int = Field(..., ge=1, le=5, description="Web Development interest (1-5)")
    interest_data: int = Field(..., ge=1, le=5, description="Data Science interest (1-5)")
    interest_programming: int = Field(..., ge=1, le=5, description="Programming interest (1-5)")
    interest_cloud: int = Field(..., ge=1, le=5, description="Cloud Computing interest (1-5)")
    interest_security: int = Field(..., ge=1, le=5, description="Cyber Security interest (1-5)")

    class Config:
        extra = "forbid"


class RecommendationItem(BaseModel):
    elective: str
    probability: float


class PredictResponse(BaseModel):
    recommended_elective: str
    confidence: float
    top_recommendations: List[RecommendationItem]


class HealthResponse(BaseModel):
    model_config = {"protected_namespaces": ()}
    status: str
    model_loaded: bool


class InfoResponse(BaseModel):
    model_config = {"protected_namespaces": ()}
    project: str
    version: str
    model_type: str
    target_classes: List[str]
    features: List[str]