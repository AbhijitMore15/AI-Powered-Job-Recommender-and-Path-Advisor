# app/models/compare_models.py
from pydantic import BaseModel
from typing import List, Optional, Dict

class CompareRequest(BaseModel):
    career_1: str
    career_2: str
    prefer: Optional[str] = None  # optional user preference e.g. "growth", "salary", "ease"

class CareerSummary(BaseModel):
    career_name: str
    difficulty: Optional[str]
    salary_midpoint: Optional[float]
    demand_level: Optional[str]
    required_skills: List[str]
    optional_skills: List[str]

class ComparisonEntry(BaseModel):
    which_is_easier: str
    which_has_more_demand: str
    salary_difference: float
    overlap_score: float
    shared_skills: List[str]
    unique_to_career_1: List[str]
    unique_to_career_2: List[str]
    recommendation: str
    explanation: str

class CompareResponse(BaseModel):
    career_1: CareerSummary
    career_2: CareerSummary
    comparison: ComparisonEntry
