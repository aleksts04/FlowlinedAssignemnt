from dataclasses import dataclass
from typing import List

@dataclass
class SummarizeServiceInputDTO:
    text: str

@dataclass
class SummarizeServiceOutputDTO:
    summary: str

@dataclass
class SimilarityServiceInputDTO:
    query: str
    texts: List[str]

@dataclass
class SimilarityServiceOutputDTO:
    closest_text: str
    score: float