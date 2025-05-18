from services.interfaces import ISimilarityService
from models.service_dtos import SimilarityServiceInputDTO, SimilarityServiceOutputDTO
from persistence.openai_gateway import OpenAIGateway
from persistence.utils import cosine_similarity
import numpy as np
from models.persistence_dtos import SimilarityPersistenceInputDTO

class SimilarityService(ISimilarityService):
    def __init__(self):
        self.gateway = OpenAIGateway()

    async def find_most_similar(self, dto: SimilarityServiceInputDTO) -> SimilarityServiceOutputDTO:
        persistence_dto = SimilarityPersistenceInputDTO(query=dto.query, texts=dto.texts)
        query_emb = await self.gateway.get_embedding(persistence_dto.query)
        text_embs = [await self.gateway.get_embedding(t) for t in persistence_dto.texts]
        sims = [cosine_similarity(query_emb, emb) for emb in text_embs]
        max_index = int(np.argmax(sims))
        return SimilarityServiceOutputDTO(closest_text=dto.texts[max_index], score=float(sims[max_index]))