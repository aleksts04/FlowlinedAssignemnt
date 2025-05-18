from pydantic import BaseModel
from typing import List

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str

class SimilarityRequest(BaseModel):
    query: str
    texts: List[str]

class SimilarityResponse(BaseModel):
    closest_text: str
    score: float