from dataclasses import dataclass
from typing import List

@dataclass
class SummarizePersistenceInputDTO:
    text: str

@dataclass
class SummarizePersistenceOutputDTO:
    summary: str

@dataclass
class SimilarityPersistenceInputDTO:
    query: str
    texts: List[str]