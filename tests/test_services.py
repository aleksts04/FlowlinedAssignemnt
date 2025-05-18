import pytest
from models.service_dtos import SummarizeServiceInputDTO, SimilarityServiceInputDTO
from services.summarizer_service import SummarizerService
from services.similarity_service import SimilarityService

class MockOpenAIGateway:
    async def summarize(self, dto):
        return type("MockOutput", (), {"summary": "Mock summary."})()

    async def get_embedding(self, text):
        if "AI" in text:
            return [1.0, 0.0, 0.0]
        elif "not related" in text:
            return [0.0, 1.0, 0.0]
        else:
            return [0.0, 0.0, 1.0]


@pytest.mark.asyncio
async def test_summarizer_service():
    service = SummarizerService()
    service.gateway = MockOpenAIGateway()
    dto = SummarizeServiceInputDTO(text="Mock text")
    result = await service.summarize_text(dto)
    assert result.summary == "Mock summary."

@pytest.mark.asyncio
async def test_similarity_service():
    service = SimilarityService()
    service.gateway = MockOpenAIGateway()
    dto = SimilarityServiceInputDTO(query="AI", texts=["not related", "AI is smart"])
    result = await service.find_most_similar(dto)
    assert result.closest_text == "AI is smart"
    assert isinstance(result.score, float)

@pytest.mark.asyncio
async def test_summarizer_service_empty_input():
    service = SummarizerService()
    service.gateway = MockOpenAIGateway()
    dto = SummarizeServiceInputDTO(text="")
    result = await service.summarize_text(dto)
    assert isinstance(result.summary, str)

@pytest.mark.asyncio
async def test_similarity_service_empty_query():
    service = SimilarityService()
    service.gateway = MockOpenAIGateway()
    dto = SimilarityServiceInputDTO(query="", texts=["AI is smart", "not related"])
    result = await service.find_most_similar(dto)
    assert result.closest_text in dto.texts
    assert isinstance(result.score, float)
