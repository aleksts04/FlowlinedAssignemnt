# AI Text Utility Microservice

This project is a lightweight AI-driven text utility microservice built with FastAPI. It provides two main features via REST API endpoints:

- Summarization: Generates a concise summary (~30 words) from a block of text.
- Semantic Similarity: Finds the most semantically similar text from a list, based on a given query.

## Features

- Asynchronous endpoints using FastAPI
- Layered architecture with clear separation of concerns
- OpenAI API integration for summarization and embeddings
- In-memory caching using TTLCache to reduce redundant OpenAI calls
- Structured JSON logging with loguru
- Per-IP rate limiting with slowapi
- Full Docker support with Docker Compose
- Unit and integration tests using pytest

## How to Build, Run, and Test

### Prerequisites

- Python 3.10+
- Docker and Docker Compose
- OpenAI API Key

### Setup

1. Clone the repository:

2. Create a `.env` file in the root of the project:

   ```
   OPENAI_API_KEY=your_openai_key_here
   ```

3. Build and run the service using Docker Compose:

   ```bash
   docker compose up --build
   ```

### Running Tests

To run all unit and integration tests:

```bash
pip install -r requirements.txt
pytest
```

## API Endpoints

- `POST /api/summarize`: Accepts a block of text and returns a ~30-word summary.
- `POST /api/similarity`: Accepts a query and a list of texts. Returns the most similar text and a similarity score.
- `GET /health`: Returns service status and uptime.

## Architectural Decisions

- FastAPI was chosen for its performance, built-in support for async, and automatic documentation via OpenAPI.
- DTOs (Data Transfer Objects) are used to separate concerns across layers: presentation (request/response), service, and persistence.
- OpenAI API is accessed via the official Python SDK to ensure compatibility and maintainability.
- TTLCache from `cachetools` is used for simple in-memory caching of summaries and embeddings, reducing API calls.
- SlowAPI provides per-IP rate limiting to prevent abuse and control usage.
- Loguru outputs structured JSON logs to stdout, suitable for cloud or container environments.

## Cost Mitigation Strategies for OpenAI Usage

- Repeated summarization and embedding requests are cached in memory for 5 minutes to avoid redundant API calls.
- Input validation and minimal payload design help reduce unnecessary usage.
- Rate limiting ensures the number of API calls per client remains within reasonable bounds.
- Unit tests use mock objects for OpenAI to avoid consuming tokens during development and CI.
