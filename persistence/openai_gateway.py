import os
from openai import OpenAI
from models.persistence_dtos import SummarizePersistenceInputDTO, SummarizePersistenceOutputDTO
from cachetools import TTLCache

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple in-memory cache (keyed by input text)
summary_cache = TTLCache(maxsize=100, ttl=300)
embedding_cache = TTLCache(maxsize=100, ttl=300)

class OpenAIGateway:
    async def summarize(self, dto: SummarizePersistenceInputDTO) -> SummarizePersistenceOutputDTO:
        if dto.text in summary_cache:
            return SummarizePersistenceOutputDTO(summary=summary_cache[dto.text])

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following text in about 30 words."},
                {"role": "user", "content": dto.text}
            ]
        )
        summary = response.choices[0].message.content.strip()
        summary_cache[dto.text] = summary
        return SummarizePersistenceOutputDTO(summary=summary)

    async def get_embedding(self, text: str):
        if text in embedding_cache:
            return embedding_cache[text]

        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        embedding = response.data[0].embedding
        embedding_cache[text] = embedding
        return embedding