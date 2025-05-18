from services.interfaces import ISummarizerService
from models.service_dtos import SummarizeServiceInputDTO, SummarizeServiceOutputDTO
from persistence.openai_gateway import OpenAIGateway
from models.persistence_dtos import SummarizePersistenceInputDTO, SummarizePersistenceOutputDTO

class SummarizerService(ISummarizerService):
    def __init__(self):
        self.gateway = OpenAIGateway()

    async def summarize_text(self, dto: SummarizeServiceInputDTO) -> SummarizeServiceOutputDTO:
        persistence_dto = SummarizePersistenceInputDTO(text=dto.text)
        result = await self.gateway.summarize(persistence_dto)
        return SummarizeServiceOutputDTO(summary=result.summary)
