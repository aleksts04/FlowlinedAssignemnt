from dataclasses import dataclass
from typing import List

@dataclass
class SummarizeInputDTO:
    text: str

@dataclass
class SummarizeOutputDTO:
    summary: str

@dataclass
class SimilarityInputDTO:
    query: str
    texts: List[str]

@dataclass
class SimilarityOutputDTO:
    closest_text: str
    score: float