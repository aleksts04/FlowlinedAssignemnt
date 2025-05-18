from abc import ABC, abstractmethod
from models.service_dtos import SummarizeServiceInputDTO, SummarizeServiceOutputDTO, SimilarityServiceInputDTO, SimilarityServiceOutputDTO

class ISummarizerService(ABC):
    @abstractmethod
    async def summarize_text(self, dto: SummarizeServiceInputDTO) -> SummarizeServiceOutputDTO:
        pass

class ISimilarityService(ABC):
    @abstractmethod
    async def find_most_similar(self, dto: SimilarityServiceInputDTO) -> SimilarityServiceOutputDTO:
        pass
