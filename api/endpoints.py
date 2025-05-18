from fastapi import APIRouter, HTTPException
from models.schemas import SummarizeRequest, SummarizeResponse, SimilarityRequest, SimilarityResponse
from services.interfaces import ISummarizerService, ISimilarityService
from services.summarizer_service import SummarizerService
from services.similarity_service import SimilarityService
from models.presentation_dtos import SummarizeInputDTO, SummarizeOutputDTO, SimilarityInputDTO, SimilarityOutputDTO

router = APIRouter()

summarizer_service: ISummarizerService = SummarizerService()
similarity_service: ISimilarityService = SimilarityService()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(payload: SummarizeRequest):
    dto_in = SummarizeInputDTO(text=payload.text)
    dto_out = await summarizer_service.summarize_text(dto_in)
    return SummarizeResponse(summary=dto_out.summary)

@router.post("/similarity", response_model=SimilarityResponse)
async def similarity(payload: SimilarityRequest):
    try:
        dto_in = SimilarityInputDTO(query=payload.query, texts=payload.texts)
        dto_out = await similarity_service.find_most_similar(dto_in)
        return SimilarityResponse(closest_text=dto_out.closest_text, score=dto_out.score)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))